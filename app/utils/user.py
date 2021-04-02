import json


def check_user_status(phone: int):
    auth_db = open('auth.json', 'r')
    db = json.load(auth_db)
    user = db['user']

    for item in user:
        if item.get('phone') == phone:
            return phone
        else:
            pass

    auth_db.close()


def create_user(phone: int, name: str, password: str):
    with open('auth.json', 'r+') as auth_db:
        db = json.load(auth_db)

        user_data = {
            "phone": phone,
            "name": name,
            "password": password
        }

        db['user'].append(user_data)

        auth_db.seek(0)

        json.dump(db, auth_db, indent=2)

        auth_db.close()

        return user_data
