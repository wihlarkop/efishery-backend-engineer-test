const token = require('../utils/token')
const users = require('../utils/user')
const response = require('../utils/response')


exports.get_payload_data = (req, res) => {
    const author = req.headers.authorization

    const auth = author.replace('Bearer', '')

    const data = token.get_payload(auth)

    return res.json(Response.JsonResponse(data))

}

exports.login = (req, res) => {
    const phone = req.body.phone
    const password = req.body.password


    if (password === 0 || password == null || password.length === 0) {
        response.JsonResponse(null, 'Please Check Your Data', 400, null,)
    }

    if (phone === "" || phone == null || phone.length === 0) {
        response.JsonResponse(null, 'Please Check Your Data', 400, null,)
    }

    const user = users.check_user_status(phone)


    // if (user === null) {
    //     response.JsonResponse(null, 'User Does Not Exist', 200, null)
    // }
    //
    // if (user.password !== password) {
    //     response.JsonResponse(null, 'Invalid Password', 200, null)
    //
    // }

    // const access_token = token.generate_access_token(user.phone, user.name, user.password, user.register_at, user.role)
    //
    // const result = {
    //     'phone': user.phone,
    //     'name': user.name,
    //     'access_token': access_token
    // }
    //
    // return res.json(Response.JsonResponse(result))
}

exports.register = (req, res) => {
    const phone = req.body.phone
    const name = req.body.name
    const now_time = Date.now()

    if (name === "" || name == null || name.length === 0) {
        response.JsonResponse(null, 'Please Check Your Data', 400, null,)
    }

    if (phone === 0 || phone == null || phone.length === 0) {
        response.JsonResponse(null, 'Please Check Your Data', 400, null,)
    }

    const user = users.check_user_status(phone)

    const password = token.get_password(4)

    if (user !== null) {
        response.JsonResponse(null, 'User Already Exist', 200, null)
    } else {
        users.create_user(phone, name, password, now_time)
    }

    const result = {
        'name': name,
        'phone': phone,
        'password': password,
        'register_at': now_time
    }

    return res.json(response.JsonResponse(result, 'Success Create User', 200))
}