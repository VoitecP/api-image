from datetime import datetime, timedelta
from .serializers import *
from gallery.models import *
import pytz


# Cannot send request.data using APIView Classes 
# and need to use dummy path
dummy_path="Fixed URL: http://127.0.0.1:8000"


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
            try:                             
                return request.build_absolute_uri(f'/api/token/{model.hash}')
            except:
                return f'{dummy_path}{model.hash}'
            # return request.data


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
            return f'{dummy_path}{url}'


def thumb1_method(self, model):
    request=self.context.get('request')
    try:
        url=model.thumb_1.url
        return request.build_absolute_uri(f'{url}')
    except:
        return f'{dummy_path}{url}'


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
            return f'{dummy_path}{url}'


def date_method(self, model):
    date=model.upload_date.strftime("%m/%d/%Y, %H:%M:%S")
    t=int(model.tier_t)

    if t in [1,2]:
        return 'No date permissions'         
    else:                                  
        return (f'Upload date {date}') 


def time_method(self, model):
    t=int(model.tier_t)
    s=int(model.exp_time)
    # s:int=600              # seconds test  :int
    delta=str(datetime.timedelta(seconds=s))
    
    if t in [1,2]:
        return 'No Time expiration permissions'         
    else:                                  
        return (f'Token Time expiration {delta}') 