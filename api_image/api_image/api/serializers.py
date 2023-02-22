from .function_serializers import *
from gallery.models import *
from rest_framework.response import Response
from rest_framework import serializers
from django.core.paginator import Paginator


class UserImageSerializer(serializers.ModelSerializer):
    token_url=serializers.SerializerMethodField(required=False, read_only=True)
    image_url=serializers.SerializerMethodField(required=False, read_only=True)
    thumb1_url=serializers.SerializerMethodField(required=False, read_only=True)
    thumb2_url=serializers.SerializerMethodField(required=False, read_only=True)
    upload_date=serializers.SerializerMethodField(required=False, read_only=True)
    exp_time=serializers.SerializerMethodField(required=False, read_only=True)
    
    class Meta:
        model=UserImage
        # fields=["id",'user',"thumb1_url","thumb2_url","image_url","token_url"]
        fields=["id",'user',"thumb1_url","thumb2_url","image_url","token_url","upload_date",'exp_time']

    def get_token_url(self, model):
        return token_method(self, model)

    def get_image_url(self, model):
        return url_method(self, model)

    def get_thumb1_url(self, model):
        return thumb1_method(self,model)
       
    def get_thumb2_url(self, model):
        return thumb2_method(self,model)
       
    def get_upload_date(self, model):
        return date_method(self,model)
       
    def get_exp_time(self, model):
        return time_method(self,model)


class UserSerializer(serializers.ModelSerializer):  
    user_images=serializers.SerializerMethodField(required=False, read_only=True)
    class Meta:
        model=User
        fields=['user_name','user_id','tier_type','user_images'] 
        # fields=['user_images'] 

    def get_user_images(self, model):                     # No pagination function
        serializer_context={'request': self.context.get('request')}     
        queryset=UserImage.objects.filter(user__id=model.id)      
        serializer=UserImageSerializer(queryset, many=True, context=serializer_context)
        return serializer.data


class PaginatedUserSerializer(UserSerializer):

    def get_user_images(self, model):
        try:
            # page_size = self.context['request'].query_params.get('size') or 5         # Custom page size 
            page_size = 5
            paginator = Paginator(UserImage.objects.filter(user__id=model.id), page_size)
            # paginator = Paginator(UserImage.objects.all(), page_size)
            page_number = self.context['request'].query_params.get('page') or 1
            books = paginator.page(page_number)
            serializer = UserImageSerializer(books, many=True)
            return serializer.data
        except:
            r=self.context.get('request')
            request=r.build_absolute_uri(f'?=page1')
            return  f'Page out of range, return {request}' 



class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['user_name','tier_t'] 

    def create(self, validated_data):
        return User(**validated_data)     


class UploadUserImageSerializer(serializers.ModelSerializer):       
    class Meta:
        model=UserImage
        fields=["user","img","exp_time"]  
      
    def create(self, validated_data):
        return UserImage(**validated_data)


class ImageSerializer(serializers.ModelSerializer):
    image=serializers.SerializerMethodField(required=False, read_only=True)

    class Meta:
        model=User
        # fields=['user_name','user_id','tier_type','user_images'] 
        fields=['user_images'] 

    def get_image(self, model):
        serializer_context={'request': self.context.get('request')}                    
        try:
            # queryset=UserImage.objects.filter(id=model.id)
            queryset=UserImage.objects.get(id=model.id)
            serializer=UserImageSerializer(queryset, many=True, context=serializer_context)
            return serializer.data
        except:
            response=Response()
            response['Queryset Validator'] = 'Proparbly corrupted data'
            return response
     

