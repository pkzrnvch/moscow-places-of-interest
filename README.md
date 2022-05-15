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
python manage.py load_place https://somewebsite.com/filename.json
```
json file should have the following format:
```json
{
    "title": "Эйфелева башня в Москве",
    "imgs": [
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/8868d171420b5221f8f50af5e95a7b12.jpeg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/46cb25cf1719bf546c8bbcf1b51ba4f4.jpeg"
    ],
    "description_short": "Вы можете поехать в Париж и отстоять огромную очередь, чтобы посетить главную его достопримечательность — великолепную Эйфелеву башню. А можете просто сесть в метро и, не выезжая за пределы МКАД, прикоснуться к точной её копии.",
    "description_long": "<p><strong>Эйфелева башня в Москве</strong> находится недалеко от станции метро «Авиамоторная» на территории одного из производственных предприятий — завода «Москабельмет». Соорудили точную копию мировой архитектурной знаменитости сами рабочие этого завода. Высота заводской башни — 15 метров (для справки — высота оригинальной, парижской Эйфелевой башни составляет 324 метра).</p><p>Однако всех желающих прикоснуться к частичке Парижа может ждать не совсем приятный сюрприз. Дело в том, что дизайнерское чудо, созданное из металлоконструкций, находится на территории режимного предприятия, а потому увидеть, а тем более потрогать его собственными руками не так просто. Чтобы попасть на территорию завода «Москабельмет», необходимо иметь при себе соответствующий пропуск. Оформлением таких пропусков занимается администрация предприятия, и как правило пропуски выдаются только его сотрудникам.</p><p>Однако всё же существуют способы осуществить свою мечту. О том, как это сделать, не нарушая закон, можно проконсультироваться у самой администрации предприятия либо поискать соответствующую информацию на тематических форумах, специализирующихся на московских достопримечательностях.</p>",
    "coordinates": {
        "lng": "37.71241599999999",
        "lat": "55.74669399999998"
    }
}
```

### Project Goals

The code is written for educational purposes on online-course for web-developers [Devman](https://dvmn.org).