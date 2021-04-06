const jwt = require('jsonwebtoken');
const auth = require('./token')
const response = require('./response')

function JWTBearer(req, res, next) {
    const token = req.headers['Authorization'].split(" ")[1];
    next()
    try {
        return auth.get_payload(token)
    } catch (error) {
        return res.json(response.JsonResponse(null, 'Token Invalid', 401));
    }
}

module.exports = {
    JWTBearer
}