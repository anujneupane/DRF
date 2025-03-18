from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import User
from .serializer import UserSerializer
from rest_framework.pagination import PageNumberPagination

class MyPage(PageNumberPagination):
    page_size = 7
    max_page_size = 5
    page_query_param = 'p'



class userList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = MyPage