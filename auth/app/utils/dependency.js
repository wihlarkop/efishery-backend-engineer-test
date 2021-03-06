const jwt = require('jsonwebtoken');
const auth = require('./token')

function JWTBearer(req, res, next) {
    const token = req.headers['Authorization'].split(" ")[1];
    next()
    try {
        return auth.get_payload(token)
    } catch (error) {
        return res.json('Token Invalid');
    }
}

module.exports = {
    JWTBearer
}