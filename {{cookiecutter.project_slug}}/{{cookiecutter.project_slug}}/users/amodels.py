import random
import string

from django.contrib.auth.hashers import make_password
from dvhb_hybrid import utils
from dvhb_hybrid.amodels import Model, method_connect_once

from .models import User as DjangoUser


class User(Model):
    table = Model.get_table_from_django(DjangoUser)
    list_fields = (
        Model.primary_key,
        'email',
        'first_name',
        'last_name',
        'is_active',
        'last_login',
        'date_joined',
    )

    @classmethod
    def set_defaults(cls, data: dict):
        data.setdefault('date_joined', utils.now())
        data.setdefault('is_active', True)
        data.setdefault('is_superuser', False)
        data.setdefault('is_staff', False)
        data.setdefault('first_name', '')
        data.setdefault('last_name', '')

        if 'password' not in data:
            password = ''.join(random.sample(string.ascii_letters + string.digits, 10))
            data['password'] = make_password(password)

    @classmethod
    @method_connect_once
    def get_user_by_email(cls, email, connection=None):
        return cls.get_one(cls.table.c.email == email, connection=connection)
