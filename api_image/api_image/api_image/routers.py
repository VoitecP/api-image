from rest_framework.routers import DefaultRouter
from api.views import *
from api.viewsets import *
from rest_framework_nested.routers import NestedDefaultRouter


router=DefaultRouter()            # default router
router.register('adduser',AddUserViewSet, basename='add-user')
router.register('user',UserViewSet, basename='UserViewSet')
router.register('user-paginated',PaginatedUserViewSet, basename='PaginatedUserViewSet')
router.register('uploaduserimage',UploadUserUimageViewSet, basename='upload-image')
router.register('userimage',UserImageViewSet, basename='user-image')
router.register('user-nested',UserViewSet, basename='Userviewset')
router.register('userimage-nested',UserImageViewSet, basename='userimage-nested')


# router.register('ownerimage',OwnerImageViewSet, basename='owner-image')

# The same name as  router.register('user'    lookup to pk/id related model
user_router=NestedDefaultRouter(router, 'user-nested', lookup='user_name')   
user_router.register('images',SingleUserViewSet, basename='images')

 # The same name as  router.register('userimage'   lookup to pk/id related model
image_router=NestedDefaultRouter(router, 'userimage-nested', lookup='user')   
image_router.register('users',SingleImageViewSet, basename='users')


# Example Nested link
# http://127.0.0.1:8000/api/user/1/images/84/
# http://127.0.0.1:8000/api/user/1/images/84/

# http://127.0.0.1:8000/api/userimage/62/
# http://127.0.0.1:8000/api/userimage/62/

# http://127.0.0.1:8000/api/userimage/62/
