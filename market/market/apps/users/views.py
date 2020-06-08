import random
import json

from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework import mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response

from users.serializer import VerifyCodeSerializer, UserSerializer
from users.models import VerifyCode
from .utils.messages import Message

# Create your views here.


User = get_user_model()
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
message = Message()


@api_view(['POST'], )
def get_code(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data = json.loads(data)
        phone = data.get('phone', '')
        random.seed()
        code = random.choices(numbers, k=4)
        code = ''.join([str(i) for i in code])
        status = message.sendMessage(code, phone)
        if status['code'] == 0:
            verify_code = VerifyCode.objects.create(code=code, phone=phone)
            verify_code_serializer = VerifyCodeSerializer(verify_code, partial=True)
            return Response(verify_code_serializer.data)


class UserDetail(generics.RetrieveAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def retrieve(self, request, *args, **kwargs):
        res = dict()
        res['username'] = request.user.username
        res['phone'] = request.user.phone[: 3] + '****' + request.user.phone[7:]
        res['picture'] = 'http://127.0.0.1:8000' + request.user.picture.url
        return Response(res)
