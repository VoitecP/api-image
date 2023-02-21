from django.core.files.storage import FileSystemStorage
from django.utils.crypto import get_random_string
import uuid, os.path
class UniqeFileStorage(FileSystemStorage):

    
   
    def get_available_name(self, name, max_length=None):

        dir_name, file_name = os.path.split(name)
        file_root, file_ext = os.path.splitext(file_name)

        # f_name,ext=os.path.splitext(file_root)
        hash=str(uuid.uuid4())
        name=f'{hash[0:5]}{file_ext}'
        # file_root=str(hash[0:5])
        # name=f'{hash[0:5]}.jpg'
        # name='abc-test.jpg'

        return name
        

    def _save(self,name, content):
        # full_path = self.path(name)


        return super()._save(name,content)













    # def get_alternative_name(self, file_root, file_ext):
    #     """
    #     Return an alternative filename, by adding an underscore and a random 7
    #     character alphanumeric string (before the file extension, if one
    #     exists) to the filename.
    #     """

    #     rnd=get_random_string(7)
    #     file_root=f'{file_root}_{rnd}{file_ext}'
    #     # return '%s%s' % (file_root, file_ext)
    #     return file_root

    # def get_alternative_name(self, file_root, file_ext):
    #     """
    #     g
    #     Return an alternative filename, by adding an underscore and a random 7
    #     character alphanumeric string (before the file extension, if one
    #     exists) to the filename.
    #     """

    #     file_root=self.get_available_name(self)
    #     return '%s' % (file_root)
        
    #     # file_root:str


    # # def get_available_name(self, name, file_root, max_length=None):

    # #         dir_name, file_name = os.path.split(name)
    # #         file_root, file_ext = os.path.splitext(file_name)

    # #         # f_name,ext=os.path.splitext(file_root)
    # #         hash=str(uuid.uuid4())
    # #         name=f'{hash[0:5]}{file_ext}'
    # #         file_root=str(hash[0:5])
    # #         # name=f'{hash[0:5]}.jpg'
    # #         # name='abc-test.jpg'

    # #         return file_root
            
            
    #         # file_root:str
        
    