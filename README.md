# Backend Engineer Test

This code is for backend engineer test.

### Built With

Fetch App

* [Python](https://www.python.org/)
* [FastAPI](https://github.com/tiangolo/fastapi)
* [Uvicorn](https://github.com/encode/uvicorn)
* [Python-dotenv](https://github.com/theskumar/python-dotenv)
* [Requests](https://github.com/psf/requests)
* [PyJWT](https://github.com/jpadilla/pyjwt)

Auth App

* [NodeJs / NPM](https://www.npmjs.com/)
* [ExpressJS](https://github.com/expressjs/express)
* [jsonwebtoken](https://www.npmjs.com/package/jsonwebtoken)

## Getting Started

*Note fetch api aggregate not already finish (min, max, avg, median, mean)

Clone this project

```
git clone https://github.com/wihlarkop/backend-engineer-test.git
```

## Installation

### Fetch App

Go to directory repo

```bash
cd backend-engineer-test
```

Create virtual environment

```bash
python -m venv env
```

Activate virtualenv

if you use wsl / linux use this command:

```bash
source env/bin/activate
```

if you use windows use this command:

```bash
env\Scripts\activate
```

then install requirements

```bash
pip install -r requirements.txt
```

create .env file inside the folder

```
DEBUG=True
PORT=must-define
RELOAD=True
ENABLE_API_DOCS=True
SECRET_KEY=must-define

CORS_ALLOW_ORIGINS=*
CORS_ALLOW_METHODS=*
CORS_ALLOW_HEADERS=*

RESOURCE_URL=https://stein.efishery.com/v1/storages/5e1edf521073e315924ceab4/list

BASE_URL_CONVERTER=https://free.currconv.com
API_KEY_CONVERTER=must-define
```

change all value must-define with value you want

### Auth App

go to directory

```bash
cd auth
```

create .env and add to .env

```
SECRET_KEY=must-define
PORT=5020
```

then install package needed

```bash
npm install
```

## Running

### Fetch App

```bash
python main.py
```

open http://localhost:your-port/api/v1/doc

### Auth App

```bash
npm start
```

open one of the api:</br>
http://localhost:port/api/v1/register</br>
http://localhost:port/api/v1/login</br>
http://localhost:port/api/v1/payload


*Note: SECRET_KEY must be same for auth and fetch*

you need register first for to get everything data, if you want register for admin, you need open auth.json file then
change your account role to "admin"

## Diagram

### Context Diagram

![Context Diagram](https://raw.githubusercontent.com/wihlarkop/backend-engineer-test/main/context_diagram.jpg)

### Deployment Diagram

![Deployment Diagram](https://raw.githubusercontent.com/wihlarkop/backend-engineer-test/main/deployment_diagram.jpg)
