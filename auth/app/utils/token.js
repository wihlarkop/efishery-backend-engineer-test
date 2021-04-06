const jwt = require('jsonwebtoken');

function get_password(size) {
    let result = '';
    const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890';
    const charactersLength = characters.length;
    for (let i = 0; i < size; i++) {
        result += characters.charAt(Math.floor(Math.random() * charactersLength));
    }
    return result;
}

function decode_jwt(token, check_expiration = true) {
    return jwt.verify(token, process.env.SECRET_KEY, {algorithm: 'HS256'}, check_expiration);
}

function encode_jwt(payload) {
    return jwt.sign(payload, process.env.SECRET_KEY, {algorithm: 'HS256'})
}

function get_payload(token, check_expiration = true, raise_error = true) {

}

module.exports = {
    get_password,
    decode_jwt,
    encode_jwt,
    get_payload
}