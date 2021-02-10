from flask import Flask, json, jsonify
from flask_cors import CORS, cross_origin


import meta_cli.cli as data


app = Flask(__name__)
# CORS(app)


@app.route("/therapists", methods=['GET'])
@cross_origin()
def therapists():
    list_of_therapists = []
    for i in data.get_recent_table().all():
        # print(i)
        photo = 'Нет фото' if i.photo[0] == 'Нет фото' else i.photo[0]['thumbnails']['large']['url']
        item = {"name": i.name, "methods": i.methods, "photo": photo, "id": i.id}
        list_of_therapists.append(item)
    return jsonify({'list': list_of_therapists})


if __name__ == '__main__':
    app.debug = True
    app.run()

