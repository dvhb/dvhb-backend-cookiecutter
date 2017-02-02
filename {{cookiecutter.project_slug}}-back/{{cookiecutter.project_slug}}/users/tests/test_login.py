import pytest
from aiohttp.web_exceptions import HTTPUnauthorized


@pytest.mark.django_db
async def test_login_logout(make_api, user, helper):
    api = await make_api(user)
    r, data = await api.login()
    await helper.check_status(r)

    r, data = await api.logout()
    await helper.check_status(r)

    r, data = await api.logout()
    await helper.check_status(r, HTTPUnauthorized)
