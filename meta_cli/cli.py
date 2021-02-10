import click
import requests
from sqlalchemy import create_engine, Column, Integer, String, JSON, DateTime, func, ARRAY
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


POSTGRES_USERNAME = 'postgres'
POSTGRES_DATABASE_NAME = 'postgres'
POSTGRES_DATABASE_PASSWORD = '1234567'


engine = create_engine(
    f'postgresql://{POSTGRES_USERNAME}:{POSTGRES_DATABASE_PASSWORD}@localhost:5432/{POSTGRES_DATABASE_NAME}'
    , echo=False
)
Session = sessionmaker(bind=engine)
session = Session()


Base = declarative_base()


class Psychotherapist(Base):
    __tablename__ = 'psychotherapists'
    id = Column(Integer, primary_key=True)
    id_therapist = Column(String)
    name = Column(String)
    methods = Column(ARRAY(String))
    photo = Column(JSON)


class Data(Base):
    __tablename__ = 'airtable'
    id = Column(Integer, primary_key=True)
    fetched_data = Column(JSON)
    date = Column(DateTime(timezone=True), default=func.now())


Base.metadata.create_all(engine)


def add_row(raw_data):
    id_therapist = raw_data['id']

    adding_therapist = raw_data['fields']
    methods = adding_therapist.setdefault('Методы', ['методы неизвестны'])
    photo = adding_therapist.setdefault('Фотография', ['Нет фото'])

    name = raw_data['fields']['Имя']
    data = Psychotherapist(id_therapist=id_therapist, name=name, methods=methods, photo=photo)
    session.add(data)
    session.commit()


def set_draft(fetched):
    data = Data(fetched_data=fetched)
    session.add(data)
    session.commit()


def get_therapists():
    api_key = "keypFmrut9G8khYGf"
    endpoint = "https://api.airtable.com/v0/app3GhNbhFYcpuxH0/Psychotherapists?&view=Grid%20view"
    headers = {
        "Authorization": f"Bearer {api_key}"
    }
    r = requests.get(endpoint, headers=headers)
    res = r.json()
    return res


def get_recent_table():
    therapists_table = session.query(Psychotherapist)
    return therapists_table


def update_psychotherapist_list():
    raw_data_query = session.query(Data)
    raw_data_count = raw_data_query.count()
    current_raw_data = raw_data_query[-1].fetched_data['records']
    prev_raw_data = None if raw_data_count < 2 else raw_data_query[-2].fetched_data['records']
    therapists_table = session.query(Psychotherapist)

    if therapists_table.count() == 0:
        list(map(lambda item: add_row(item), current_raw_data))
        print('The data is up-to-date now')
    else:
        if not current_raw_data == prev_raw_data:
            raw_data_ids = []
            for i in current_raw_data:

                if not i['fields']:
                    continue

                raw_data_ids.append(i['id'])
                therapist_instance = therapists_table.filter(Psychotherapist.id_therapist == i['id'])
                if therapist_instance.value('name'):
                    if not therapist_instance.value('name') == i['fields']['Имя']:
                        therapist_instance.first().name = i['fields']['Имя']
                        session.commit()
                    if i['fields'].get('Методы'):
                        if not therapist_instance.value('methods') == i['fields'].get('Методы'):
                            therapist_instance.first().methods = i['fields'].get('Методы')
                            session.commit()
                    else:
                        if not therapist_instance.value('methods')[0] == 'методы неизвестны':
                            therapist_instance.first().methods = ['методы неизвестны']
                    #
                    if i['fields'].get('Фотография'):
                        if not therapist_instance.value('photo') == i['fields'].get('Фотография'):
                            therapist_instance.first().photo = i['fields'].get('Фотография')
                            session.commit()
                    else:
                        if not therapist_instance.value('photo')[0] == 'Нет фото':
                            therapist_instance.first().photo = ['Нет фото']
                else:
                    print('needs to be added in table like a new item')
                    add_row(i)
            # deleting rows that wasn't found in recent raw_data
            for k in therapists_table.all():
                if k.id_therapist not in raw_data_ids:
                    removed_value = therapists_table.filter(Psychotherapist.id_therapist == k.id_therapist).first()
                    session.delete(removed_value)
                    session.commit()
                    # print(f'id {k.id_therapist} is now removed')
            print('The data is up-to-date now')
        else:
            print('The data is checked. No changes.')


@click.command()
def cli():
    data = get_therapists()
    set_draft(data)
    update_psychotherapist_list()


