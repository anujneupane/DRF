from rest_framework import viewsets
from .serializer import UserSerializer
from .models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly

class UserModelViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    permission_classes = [IsAuthenticatedOrReadOnly]



'''from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from .serializer import UserSerializer
from .models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly,DjangoObjectPermissions,BasePermission

class UserViewSet(viewsets.ViewSet):
    def list(self, request):  
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None): 
        user = get_object_or_404(User, pk=pk)  #  Handle 404 errors safely
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        user = get_object_or_404(User, pk=pk)  # Fix model reference
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Complete Data Updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, pk=None):
        user = get_object_or_404(User, pk=pk)  # Fix model reference
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Data Updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        print("***********Destroy**************")
        print("Basename :",self.basename)
        print("Action :",self.action)
        print("Details :",self.detail)
        print("Suffix :",self.suffix)
        print("Name :",self.name)
        print("Description :",self.description)

        user = get_object_or_404(User, pk=pk)  # Fix model reference
        user.delete()
        return Response({'msg': 'Data Deleted'})

class MyPerm(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True   

class UserModelViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # authentication_classes = [BasicAuthentication]
    authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticated]
    # permission_classes = [IsAdminUser]  #only for is staff = true
    # permission_classes = [IsAuthenticatedOrReadOnly] 
    # permission_classes = [DjangoModelPermissions] 
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]   # unauthenticated user can read only provided
    #permission_classes = [DjangoObjectPermissions] 
    permission_classes = [MyPerm] # custom permission '''

