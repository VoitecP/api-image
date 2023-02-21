import datetime
from django.core.validators import (FileExtensionValidator, 
                                    MinValueValidator, MaxValueValidator )
from django.db import models
from .thumbnails import make_thumb


class Tier(models.Model):
    tier_type=models.IntegerField(default=4,editable=True, validators=[MinValueValidator(4), MaxValueValidator(999)])
    tier_name=models.CharField(max_length=50)
    thumb1_H=models.IntegerField(default=2, validators=[MinValueValidator(2), MaxValueValidator(9999)])
    thumb1_W=models.IntegerField(default=2, validators=[MinValueValidator(2), MaxValueValidator(9999)])
    thumb2_H=models.IntegerField(blank=True, default=2, editable=False)
    thumb2_W=models.IntegerField(blank=True, default=2, editable=False)

    def __str__(self):
        return f'{self.tier_name}'


class User(models.Model):
    user_name=models.CharField(max_length=50)
    tier_t=models.ForeignKey(Tier,models.PROTECT)
    img=models.ImageField(blank=True, editable=False,validators=[FileExtensionValidator(allowed_extensions=['jpg','png'])], )

    def __str__(self):
        return f'{self.user_name}'

    @property
    def user_id(self):
            return f'{self.id}'       

    @property           # useless
    def tier_type(self):
        return self.tier_t.tier_type      

class UserImage(models.Model):
    user=models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    img=models.ImageField(validators=[FileExtensionValidator(allowed_extensions=['jpg','png'])])
    thumb_1=models.ImageField(editable=False, blank=True)  
    thumb_2=models.ImageField(editable=False, blank=True)
    exp_time=models.IntegerField(default=400, blank=True, 
                validators=[MinValueValidator(300), MaxValueValidator(30000)])     # second range int
    hash=models.CharField(default='', editable=False, max_length=50, unique=False)
    upload_date=models.DateTimeField(default=datetime.datetime.now(), editable=False)
    
    def __str__(self):
        return f'{self.user}'

    @property           # needed property
    def tier_t(self):
        return self.user.tier_t.tier_type     
    
    
    def save(self, *args, **kwargs):
        make_thumb(self)
        return super().save(self, *args, **kwargs)

        