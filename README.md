# CODERUSH_APIS 
this is project development for support Arab developer community 🔥


## API Reference

#### Get all items

```http
  GET /api/v1/posts
```



#### Get item

```http
  GET /api/v1/posts/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |

#### Allow Method 
```http
    POST() / DELETE() / PUT()
```
##### login is **Required**


## SETUP Database
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.YOU_DB_ENGINE',
        'NAME': 'DB_NAME',
        'USER': 'UESRNAME',
        'PASSWORD': 'PASSWORD',
        'HOST': 'YOUR_HOST',
        'PORT': 'YOUR_POSRT',
    }
}
```
## Examples
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'coderush',
        'USER': 'postgres',
        'PASSWORD': '123',
        'HOST': 'localhost',
        'PORT': '5432',

    }
}
```
## Run Locally

Clone the project

```bash
  git clone https://github.com/islam-kamel/CODERUSH_APIS.git
```

Go to the project directory

```bash
  cd CODERUSH_APIS
```

Install dependencies

```bash
  pip install -r requirements.txt
```
Setup Database tables

```bash
  python3 manage.py makemigrtions
  python3 manage.py migrate
```
Create Super User

```bash
  python3 manage.py createsuperuser
```

Start the server

```bash
  python3 manage.py runserver
```

## Running Tests

To run tests, run the following command

```bash
  coverage run --omit='*/env/* manage.py run test
```

## Upcoming features 🧑‍💻

- Authentication System 🗃️
- Badge System 📛
- Tags System 🏷️
- Comments System 📝
- Notification reltime System 🔔
- Chat app include in projects 💬
- Light/dark mode toggle 🌚
- Cross platform 📱


## Done

- [x] Post System 🎉


## License

[MIT](https://github.com/islam-kamel/CODERUSH_APIS/blob/main/LICENSE)