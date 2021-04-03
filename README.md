# Backend Engineer Test

This code is for backend engineer test.

### Built With

* [Python](https://www.python.org/)
* [FastAPI](https://github.com/tiangolo/fastapi)
* [Uvicorn](https://github.com/encode/uvicorn)
* [Python-dotenv](https://github.com/theskumar/python-dotenv)
* [Requests](https://github.com/psf/requests)
* [PyJWT](https://github.com/jpadilla/pyjwt)

## Getting Started

Clone this project

```
git clone https://github.com/wihlarkop/backend-engineer-test.git
```

## Installation

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

## Running

```bash
python main.py
```

open http://localhost:your-port/api/v1/doc

you need register first for to get everything data
