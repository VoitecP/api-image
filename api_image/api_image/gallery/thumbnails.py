import os
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
from django.utils.crypto import get_random_string

def make_thumb(self):
    h1=int(self.user.tier_t.thumb1_H)
    w1=int(self.user.tier_t.thumb1_W)
    h2=int(self.user.tier_t.thumb2_H)
    w2=int(self.user.tier_t.thumb2_W)
    t=int(self.user.tier_t.tier_type) # var type protector for Tier value
    file=self.img
    file_h=self.img.height
    file_w=self.img.width
    th1=self.thumb_1
    th2=self.thumb_2
    ratio=file_w/file_h
    w1_r=int(round(h1 * ratio))
    w2_r=int(round(h2 * ratio))

    if t in [1,2,3]:
        w1=w1_r
        w2=w2_r
    else:
        pass

    try:
        image = Image.open(file)
        image.thumbnail((h1,w1), Image.ANTIALIAS)
        th_name, th_ext = os.path.splitext(file.name)
        th_ext = th_ext.lower()

        if th_ext == '.jpg':       # .jpeg extension are not valid !
            FTYPE = 'JPEG'
        elif th_ext == '.png':
            FTYPE = 'PNG'

        th_filename = f'{th_name}_thumb{h1}x{w1}{th_ext}'
        temp_th = BytesIO()              # SavE thumbnail to in-memory file as StringIO
        image.save(temp_th, FTYPE)
        temp_th.seek(0)

        th1.save(th_filename, ContentFile(temp_th.read()), save=False) # set save must be False !
        temp_th.close()
    except IOError:
        pass
    
    if t == 2 or t== 3 :
        try:
            image = Image.open(file)
            image.thumbnail((h2,w2), Image.ANTIALIAS)
            th_name, th_ext = os.path.splitext(file.name)
            th_ext = th_ext.lower()

            if th_ext == '.jpg':       # .jpeg extension are not valid !
                FTYPE = 'JPEG'
            elif th_ext == '.png':
                FTYPE = 'PNG'

            th_filename = f'{th_name}_thumb{h2}x{w2}{th_ext}'
            temp_th = BytesIO()              # SavE thumbnail to in-memory file as StringIO
            image.save(temp_th, FTYPE)
            temp_th.seek(0)

            th2.save(th_filename, ContentFile(temp_th.read()), save=False) # set save must be False !
            temp_th.close()
        except IOError:
            pass      

    if t==1 or t==2 :
        self.hash=''
        self.exp_time=0        # force set value to 0'
    else:
        self.hash=get_random_string(10)     # token generator
