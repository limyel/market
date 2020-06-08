import random

from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

from users.models import VerifyCode


User = get_user_model()
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v'
           , 'w', 'x', 'y', 'z']


class UserBackend(ModelBackend):
    """
    自定义用户验证
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        # data = request.body.decode('utf-8')
        # data = json.loads(data)
        phone = username
        code = password
        try:
            verify_code = VerifyCode.objects.filter(code=code, phone=phone).first()
            if verify_code:
                random.seed()
                user = User.objects.filter(phone=phone).first()
                if not user:
                    user = User.objects.create(username=''.join(random.choices(letters, k=8)), phone=phone)
                verify_code.delete()
                return user
        except Exception as e:
            return None
