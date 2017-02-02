from django.contrib.auth.hashers import check_password

from dvhb_hybrid import exceptions
from dvhb_hybrid.amodels import method_redis_once
from dvhb_hybrid.redis import redis_key
from dvhb_hybrid.permissions import permissions, gen_api_key


async def login(request, email, password):
    user = await request.app.models.user.get_user_by_email(email)
    if user and check_password(password, user.password):
        await gen_api_key(user.id, request=request, auth='email')
        request.user = user
        return {'api_key': request.session}
    return exceptions.HTTPBadRequest(errors=dict(
        __all__=['Пользователь или пароль указан не верно']
    ))


@method_redis_once('sessions')
@permissions
async def logout(request, sessions):
    key = redis_key(request.app.name, request.session, namespace='session')
    await sessions.delete(key)
    return exceptions.HTTPOk()
