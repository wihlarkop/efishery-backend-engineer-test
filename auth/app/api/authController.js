const token = require('../utils/token')
const users = require('../utils/user')


function get_payload_data(req, res) {
    const author = req.headers.authorization

    const data = token.get_payload(author)

    return res.json(data)

}

function login(req, res) {
    const phone = req.body.phone
    const password = req.body.password


    if (password == null || password.length === 0) {
        res.json('Please Check Your Data')
    }

    if (phone === "" || phone == null || phone.length === 0) {
        res.json('Please Check Your Data')
    }

    const user_status = users.check_user_status(phone)


    if (user_status === null) {
        res.json('User Does Not Exist')
    }

    if (user_status.password !== password) {
        res.json('Invalid Password')
    }

    const access_token = token.generate_access_token(user_status.phone,
        user_status.name,
        user_status.password,
        user_status.register_at,
        user_status.role
    )

    const result = {
        'phone': user_status.phone,
        'name': user_status.name,
        'access_token': access_token
    }

    return res.json(result)
}

function register(req, res) {
    const phone = req.body.phone
    const name = req.body.name
    const now_time = Date.now()


    if (name === "" || name == null || name.length === 0) {
        res.json('Please Check Your Data')
    }

    if (phone === 0 || phone == null || phone.length === 0) {
        res.json('Please Check Your Data')
    }

    const user = users.check_user_status(phone)

    const password = token.get_password(4)

    if (user !== undefined) {
        res.status(409).json('User Already Exist')
    } else {
        users.create_user(phone, name, password, now_time)
    }

    const result = {
        'name': name,
        'phone': phone,
        'password': password,
        'register_at': now_time
    }

    return res.json(result)
}

module.exports = {
    login,
    register,
    get_payload_data
}