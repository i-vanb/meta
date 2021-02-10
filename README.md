# meta

## Create Postgresql DB and add your data instead of mine in ./meta_cli/cli.py:
> POSTGRES_USERNAME = 'yours'  
> POSTGRES_DATABASE_NAME = 'yours'  
> POSTGRES_DATABASE_PASSWORD = 'yours'  

clone repository
> $ cd meta  
> $ pip install .  
After the installation "meta" command is available.  
Every time you run "meta" it takes data from airtable that is editable on  
https://airtable.com/invite/l?inviteId=invJ9l7xcv0w8a8kg&inviteToken=9b81a1082b8efc369d65ccb843138fa5285c2fe5a999d0a9dd6c7a900cd35589  

### Now you can run Flask  
> $ cd meta  
> $ python app.py  

And Vue  
> $ cd client  
> $ npm install  
> $ npm run serve  

### Go ahead to http://localhost:8080
