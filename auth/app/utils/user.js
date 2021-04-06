const fs = require('fs');


function create_user(phone, name, password, register_at, role = 'user') {
    const user_data = {
        'phone': phone,
        'name': name,
        'password': password,
        'created_at': register_at,
        'role': role
    }

    fs.readFile('../../../auth.json', 'utf8', function readFileCallback(err, data) {
        if (err) {
            console.log(err);
        } else {

            const user = JSON.parse(data); //now it an object
            user.user.push(user_data); //add some data
            const json = JSON.stringify(user, null, 2); //convert it back to json
            fs.writeFile('../../../auth.json', json, 'utf8', function (err, data) {
                if (err) {
                    console.error(err);
                    return
                }
                console.log("Successfully Insert Data");
            });
        }
    })

    return user_data
}


function check_user_status(phone) {
    fs.readFile('../../../auth.json', 'utf8', function readFileCallback(err, data) {
        if (err) {
            console.log(err);
        } else {
            const users = JSON.parse(data)

            users.user.forEach(function (item) {
                if (item.phone === phone) {
                    console.log(users.user)
                    return users.user
                } else {
                    return null
                }
            })
        }
    })
}

module.exports = {
    check_user_status,
    create_user
}