from django_filters.rest_framework import FilterSet
from gallery.models import *

class UserFilter(FilterSet):
    class Meta:
        model=User
        fields={
            'id':['exact'],
            'user_name':['exact'],
            'tier_t':['exact'],
        }
    

class UserImageFilter(FilterSet):
    class Meta:
        model=UserImage
        fields={
            'id':['exact'],
            'user':['exact'],
            'upload_date':['gt','lt'],
        }
