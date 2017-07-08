from dvhb_hybrid.tests import BaseTestApi


class TestApi(BaseTestApi):
    async def login(self):
        url = self.get_route('users.views.login').url()
        r = await self.client.post(url, data={'email': self.user['email'], 'password': self.user['password']})
        data = await r.json()
        if r.status == 200:
            self.headers[self.API_KEY] = data['api_key']
        return await self.prepare_result(r)

    async def logout(self):
        url = self.get_route('users.views.logout').url()
        r = await self.client.post(url, headers=self.headers)
        if self.API_KEY in self.headers:
            del self.headers[self.API_KEY]
        return await self.prepare_result(r)
