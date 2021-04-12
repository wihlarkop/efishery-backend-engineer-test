const fs = require('fs');
const path = require('path')


const json_file = path.join(__dirname, '../../../auth.json')

function create_user(phone, name, password, register_at, role = 'user') {
    const user_data = {
        'phone': phone,
        'name': name,
        'password': password,
        'created_at': register_at,
        'role': role
    }


    fs.readFile(json_file, 'utf8', function readFileCallback(err, data) {
        if (err) {
            console.log(err);
        } else {

            const user = JSON.parse(data); //now it an object
            user.user.push(user_data); //add some data
            const json = JSON.stringify(user, null, 2); //convert it back to json
            fs.writeFile(json_file, json, 'utf8', function (err, data) {
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
    const data = fs.readFileSync(json_file, 'utf8');
    const JSONData = JSON.parse(data);
    let selectedItem;
    JSONData.user.forEach(function (item) {
        if (item.phone === phone) {
            selectedItem = item
        }
    })
    return selectedItem;
}


module.exports = {
    check_user_status,
    create_user
}