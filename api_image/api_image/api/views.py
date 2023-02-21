from gallery.models import *
from .serializers import *
from django.shortcuts import redirect
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination


class UserViewSet(ModelViewSet):
    pagination_class=PageNumberPagination
    queryset=User.objects.all()
    serializer_class=UserSerializer
    # filterset_class=UserFilter
    filter_backends=[SearchFilter,OrderingFilter]
    search_fields=['id','user_name']        # allow to search exact value id or User Name
    # search_fields=['id','user']
    # http_method_names=['get','post','head','delete']
    http_method_names=['get']
   

class UserImageViewSet(ModelViewSet):       # Allow to Get User 
    pagination_class=PageNumberPagination
    queryset=UserImage.objects.all()        #.filter(user__id=1)  # For testing
    serializer_class=UserImageSerializer
    http_method_names=['get']

    def perform_create(self, serializer):
        serializer.save()


class OwnerImageViewSet(ModelViewSet):       # Allow to Get User 
    pagination_class=PageNumberPagination
    queryset=UserImage.objects.all()        #.filter(user__id=1)  # For testing
    # queryset=UserImage.objects.filter(user=self.kwargs["user_pk"])
    serializer_class=UserImageSerializer
    http_method_names=['get']

    
# def get_serializer_context(self):
#         context={"user":self.kwargs["pk"]}
#         # context={"user_id":self.kwargs["user_pk"]}
#         return context

    def get_queryset(self): 
          
            # queryset=UserImage.objects.all().filter(user=1)
            # queryset=UserImage.objects.filter(user__user=self.kwargs['pk'])
            # x=self.kwargs['user_id']
            # /66/ adres get id of image filters 
            x=1
            queryset=UserImage.objects.filter(user=x)       # show only user 1 images without parameters

            # queryset=UserImage.objects.filter(ticker__ticker=self.kwargs['stocks_ticker'])

            return queryset



class OwnView(APIView):
    def get(self, *args,**kwargs):                   #  first() prevents multi queryset error
        # queryset=UserImage.objects.get(**kwargs)      
        queryset=UserImage.objects.filter(**kwargs).first()
        response=Response()
        response['Token Link Validator']='Proparbly wrong link'
        try:
            return redirect(queryset.img.url)  
        except:
            return response





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


##########


# class UploadUserUimageViewSet(ModelViewSet):
#     queryset=UserImage.objects.none()
#     serializer_class=UploadUserImageSerializer

#     def get_serializer_class(self):
#         tier=int(self.tier_t)
#         # # tier=self.request.tier_t
#         if tier in [1,2]:
#             return UploadUserImageSerializer
#         else:
#             return Upload2UserImageSerializer

#         # serializer.data['exp_time'] == None
#         # serializer.save()
#         # return super().perform_create(serializer)
    


## not working
    # def get_serializer_context(self, *args, **kwargs):
    #     context=super().get_serializer_context()
    #     context.update({"request":self.request})
    #     return context




# class UploadUserUimageViewSet(ModelViewSet):
#     queryset=UserImage.objects.none()
#     # user_type=SerializerMe
#     # serializer_class=DynamicUploadUserImageSerializer
#     serializer_class=DynamicFieldSerializer

    



## select user from id or from list ? to view queryset
## make redirection to self user images or 

# or start from select by id/name  from invisible list then see list and then post
### add pagination to list view of images in user

## expiring link set config seconds in serializer in image send now!!!\

# cleaning the import and pip and decoupler and check erors clean code and comments