from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import User
from .serializer import UserSerializer
from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination,CursorPagination

class MyPage(PageNumberPagination):
    page_size = 7
    max_page_size = 5
    page_query_param = 'p'
    page_size_query_param = 'give'
    max_page_size = 10

class MyPage1(LimitOffsetPagination):
    default_limit = 4
    limit_query_param = 'limit'
    offset_query_param = 'cut'
    max_limit = 10

class MyPage2(CursorPagination):
    page_size = 7
    ordering = 'name'
    cursor_query_param = 'cu'
    max_limit = 10
    


class userList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = MyPage1