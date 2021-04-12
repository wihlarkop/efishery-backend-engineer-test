const jwt = require('jsonwebtoken');

const AUTH_TOKEN_EXPIRATION = 3 * 60 * 60

const SECRET_KEY = 'backendengineer'

function generate_access_token(phone, name, password, register_at, role) {
    const expiration = Date.now() + AUTH_TOKEN_EXPIRATION
    const payload = {
        'phone': phone,
        'name': name,
        'password': password,
        'register_at': register_at,
        'role': role,
        'exp': expiration.getTime()
    }
    return encode_jwt(payload)
}

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
    return jwt.verify(token, SECRET_KEY, {algorithm: 'HS256'}, check_expiration);
}


function encode_jwt(payload) {
    return jwt.sign(payload, SECRET_KEY, {algorithm: 'HS256'})
}

function get_payload(token, check_expiration = true, raise_error = true) {
    try {
        return jwt.verify(token, SECRET_KEY, {algorithm: 'HS256'})
    } catch (err) {
        if (raise_error) {
            throw err
        }
        return null
    }
}


module.exports = {
    generate_access_token,
    get_password,
    decode_jwt,
    encode_jwt,
    get_payload
}