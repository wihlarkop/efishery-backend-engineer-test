async def login():
    user = get_user_by_username(request, login.username)

    if user is None:
        return JsonResponse(message='User does not exist', code=404)

    # check status
    if user.UDStatus == 'registered':
        return JsonResponse(message='User is not activated')
    elif user.UDStatus == 'suspended':
        return JsonResponse(message='User is suspended')
    elif user.UDStatus == 'deleted':
        return JsonResponse(message='User is deleted')

    # check password
    encrypted_password = get_encrypted_password(login.username, login.password)

    if user.UDPassword.encode(encoding='utf-8') != encrypted_password:
        return JsonResponse(message='Invalid password')

    ip_add = request.client.host

    access_token = generate_access_token(request, user_id=user.UDKey,
                                         username=user.UDUsername,
                                         ip_address=ip_add,
                                         platform=login.platform)

    login_user(
        request,
        user_id=user.UDKey,
        username=user.UDUsername,
        device_id=login.device_id,
        platform=login.platform,
        token=access_token
    )

    result = {
        'user_id': user.UDKey,
        'access_token': access_token,
        'username': user.UDUsername
    }

    return JsonResponse(data=result)
