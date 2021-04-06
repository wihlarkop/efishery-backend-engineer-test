function JsonResponse(data, message, code = 200, meta, status_code = 200, success = true) {
    return res.json({
        'data': data,
        'message': message,
        'code': code,
        'meta': meta,
        'success': success,
        'status_code': status_code
    })
}

module.exports = {
    JsonResponse
}