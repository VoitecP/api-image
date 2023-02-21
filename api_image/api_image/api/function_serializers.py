from datetime import datetime, timedelta
from .serializers import *
from gallery.models import *
import pytz


def token_method(self, model):
    t=int(model.tier_t)
    request=self.context.get('request')
    now=datetime.datetime.now().replace(tzinfo=pytz.UTC)
    date=model.upload_date.replace(tzinfo=pytz.UTC)
    duration=int(model.exp_time)        # seconds :int format protector
    # duration=3000000                   # test value opion
    
    if t in [1,2]:
        return 'No token permissions'         
    else: 
        if date < now - timedelta(seconds=duration):
            return 'Token link expired'
        else:                                  
            return request.build_absolute_uri(f'/token/{model.hash}')     


def url_method(self, model):
    t=int(model.tier_t)
    request=self.context.get('request')
    if t == 1 :   
        return 'No permissions' 
    if t != 1 :
        try:
            url=model.img.url
            return request.build_absolute_uri(f'{url}')
        except:
            return 'File not found'


def thumb1_method(self, model):
    request=self.context.get('request')
    try:
        url=model.thumb_1.url
        return request.build_absolute_uri(f'{url}')
    except:
        return 'File not found'


def thumb2_method(self, model):
    t=int(model.tier_t)
    request=self.context.get('request')
    if t not in [2,3]:   
        return 'No permissions' 
    else:    
        try:
            url=model.thumb_2.url
            return request.build_absolute_uri(f'{url}')
        except:
            return 'File not found'



# # def get_user_images(self, model):
# def single_image_method(self,model):
#     serializer_context={'request': self.context.get('request')}                    
#     try:
#         # queryset=UserImage.objects.filter(id=model.id)
#         queryset=UserImage.objects.get(id=model.id)
#         serializer=UserImageSerializer(queryset, many=True, context=serializer_context)
#         return serializer.data
#     except:
#         response=Response()
#         response['Queryset Validator'] = 'Proparbly corrupted data'
#         return response

# def user_images_method(self, model):
        
#         # page_size=5           # Paginator disabled because not get proper data
#         # page_size=self.context['request'].query_params.get('size') or 10

#         serializer_context={'request': self.context.get('request')}
#                 # queryset should be single instance  but if not it is safer to use filter method instead of get
#                                         # Set if/try to get single instance
#         queryset=UserImage.objects.filter(user__id=model.id)       
#         # queryset=UserImage.objects.get(user__id=model.id)

#         # paginator=Paginator(queryset, page_size)
#         # queryset=paginator.page(2)
#         serializer=UserImageSerializer(queryset, many=True, context=serializer_context)
#         return serializer.data