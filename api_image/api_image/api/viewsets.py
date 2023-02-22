from gallery.models import *
from .serializers import *
from django.shortcuts import redirect
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from .filters import *


class UserViewSet(ModelViewSet):            # shows image gallery of each user 
    pagination_class=PageNumberPagination   # im not sure why it is not working in html templates
    queryset=User.objects.all()

    serializer_class=UserSerializer
    filter_backends=[SearchFilter,OrderingFilter,DjangoFilterBackend]
    filterset_fields=['user_name', 'id', 'tier_t'] 
    # search_fields=['user_name']     # searching  not working ! returns error
    filterset_class=UserFilter
    http_method_names=['get']

class PaginatedUserViewSet(UserViewSet):
    serializer_class=PaginatedUserSerializer
 

class UserImageViewSet(ModelViewSet):       # Get images by id image   
    pagination_class=PageNumberPagination
    queryset=UserImage.objects.all()      
    serializer_class=UserImageSerializer
    filter_backends=[SearchFilter,OrderingFilter,DjangoFilterBackend]
    filterset_fields=['user', 'id', 'upload_date'] 
    # search_fields=['user']       # searching  not working ! returns error
    filterset_class=UserImageFilter
    http_method_names=['get']

    def perform_create(self, serializer):
        serializer.save()


class AddUserViewSet(ModelViewSet):         # Allow to Create User
    queryset=User.objects.none()
    serializer_class=CreateUserSerializer
    http_method_names=['post']
   

class UploadUserUimageViewSet(ModelViewSet):
    queryset=UserImage.objects.none()
    serializer_class=UploadUserImageSerializer


class TokenView(APIView):
    def get(self, *args,**kwargs):                   #  first() prevents multi queryset error
        # queryset=UserImage.objects.get(**kwargs)      
        queryset=UserImage.objects.filter(**kwargs).first()
        response=Response()
        response['Token Link Validator']='Proparbly wrong link'
        try:
            return redirect(queryset.img.url)  
        except:
            return response


class SingleUserViewSet(ModelViewSet):
    pagination_class=PageNumberPagination
    # queryset=User.objects.filter(id=1)
    serializer_class=UserSerializer


    def get_queryset(self):
        # queryset=User.objects.filter(user__id=self.kwargs["user_pk"])
        queryset=UserImage.objects.filter(user__id=self.kwargs["user_pk"])
        return queryset
    
    def get_serializer_context(self):
        context={"user_id":self.kwargs["user_pk"]}
        # context={"user_id":self.kwargs["user_pk"]}
        return context

## wrong
class SingleImageViewSet(ModelViewSet):
    pagination_class=PageNumberPagination
    queryset=User.objects.filter(id=1)
    serializer_class=ImageSerializer

    def get_queryset(self):
        # queryset=UserImage.objects.filter(user__id=self.kwargs["user_pk"])
        queryset=UserImage.objects.filter(id=self.kwargs["pk"])
        return queryset
    
    def get_serializer_context(self):
        context={"user_id":self.kwargs["user_pk"]}
        # context={"user_id":self.kwargs["user_pk"]}
        return context

    



## select user from id or from list ? to view queryset
## make redirection to self user images or 

# or start from select by id/name  from invisible list then see list and then post
### add pagination to list view of images in user

## expiring link set config seconds in serializer in image send now!!!\

# cleaning the import and pip and decoupler and check erors clean code and comments