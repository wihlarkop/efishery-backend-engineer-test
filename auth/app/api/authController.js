const token = require('../utils/token')

exports.get_payload_data = (req, res) => {
    // get_password()
    res.json(token.get_password(4))

}

exports.login = (req, res, next) => {

}

exports.register = (req, res) => {

}