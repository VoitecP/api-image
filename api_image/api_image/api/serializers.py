from .function_serializers import *
from gallery.models import *
from rest_framework.response import Response
from rest_framework import serializers
# from django.core.paginator import Paginator


class UserImageSerializer(serializers.ModelSerializer):
    token_url=serializers.SerializerMethodField(required=False, read_only=True)
    image_url=serializers.SerializerMethodField(required=False, read_only=True)
    thumb1_url=serializers.SerializerMethodField(required=False, read_only=True)
    thumb2_url=serializers.SerializerMethodField(required=False, read_only=True)

    class Meta:
        model=UserImage
        # fields=["id","thumb1_url","thumb2_url","image_url","token_url"]
        fields=["id",'user',"thumb1_url","thumb2_url","image_url","token_url"]
        # fields=["id","user","thumb1_url","thumb2_url","image_url","token_url"]   

    def get_token_url(self, model):
        return token_method(self, model)

    def get_image_url(self, model):
        return url_method(self, model)

    def get_thumb1_url(self, model):
        return thumb1_method(self,model)
       
    def get_thumb2_url(self, model):
        return thumb2_method(self,model)
       

class UserSerializer(serializers.ModelSerializer):
    user_images=serializers.SerializerMethodField(required=False, read_only=True)
    
    class Meta:
        model=User
        # fields=['user_name','user_id','tier_type','user_images'] 
        fields=['user_images'] 

    def get_user_images(self, model):
        # return user_images_method(self,model)
        
        # page_size=5           # Paginator disabled because not get proper data
        # page_size=self.context['request'].query_params.get('size') or 10

        serializer_context={'request': self.context.get('request')}
                # queryset should be single instance  but if not it is safer to use filter method instead of get
                                        # Set if/try to get single instance
        queryset=UserImage.objects.filter(user__id=model.id)       
        # queryset=UserImage.objects.get(user__id=model.id)

        # paginator=Paginator(queryset, page_size)
        # queryset=paginator.page(2)
        serializer=UserImageSerializer(queryset, many=True, context=serializer_context)
        return serializer.data


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

# Exp Time filed should be disabled to basic tiers
    # But need's to be validated thru authenticated user


# http://127.0.0.1:8000/api/User/1/images/84/

# class DetailSerializer(serializers.ModelSerializer):
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
            
        
class OwnerSerializer(serializers.ModelSerializer):
    user_images=serializers.SerializerMethodField(required=False, read_only=True)
    
    class Meta:
        model=User
        # fields=['user_name','user_id','tier_type','user_images'] 
        fields=['user_images'] 

    def get_user_images(self, model):

    #        t=int(model.tier_t)
    #     request=self.context.get('request')
    # if t == 1 :   
    #     return 'No permissions' 
    # if t != 1 :
     
        
        return request.build_absolute_uri(f'{url}')
        


class Owner
        
          # Set if/try to get single instance

# queryset should give single instance better .filter method instead of .get() to
# prevent to multi instace error..
#  if not it is safer to use filter method instead of get



##### Adnotations ####
class DynamicSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)

        # Instantiate the superclass normally
        super().__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)


class DynamicUserImageSerializer(DynamicSerializer):
    fields=serializers.SerializerMethodField('get_fields')

    class Meta:
        model=UserImage         
        fields=["user","img","exp_time"]  
       
    def create(self, validated_data):
        return UserImage(**validated_data) 

    def get_fields(self,model):
        serializer_context="img"


