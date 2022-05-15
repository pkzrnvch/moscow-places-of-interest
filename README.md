# Places of interest in Moscow

Website with the map containing the most interesting places to visit in Moscow and beyond.

Website demo is available [here](http://pkzrnvch.pythonanywhere.com/).
Test data is taken from [KudaGo](https://kudago.com).

### How to install

- Clone repository
- Install dependencies `pip install -r requirements.txt`
- Create database file and apply migrations `python3 manage.py migrate`
- Run server `python3 manage.py runserver`
- [Open in browser](http://127.0.0.1:8000/)

### Environment variables

Some of the project settings are taken from environment variables. Create an `.env` file in the project directory to set them:

- `DEBUG` — set True to see the debug information in case of en error
- `SECRET_KEY` — project secret key
- `ALLOWED_HOSTS` — list of allowed hosts
  
Example of an `.env` file:
```
SECRET_KEY='SECRET_KEY'
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1,mysite.pythonanywhere.com
```

### Adding places

You can add new locations from the admin panel or by using a management command:

```
python manage.py load_place filename.json
```

### Project Goals

The code is written for educational purposes on online-course for web-developers [Devman](https://dvmn.org).