from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from django.views.generic.base import RedirectView
from api.views import *
from rest_framework_nested.routers import NestedDefaultRouter


router=DefaultRouter()            # default router
router.register('adduser',AddUserViewSet, basename='add-user')
router.register('user',UserViewSet, basename='user')
router.register('uploaduserimage',UploadUserUimageViewSet, basename='upload-image')
router.register('userimage',UserImageViewSet, basename='user-image')
router.register('ownerimage',OwnerImageViewSet, basename='owner-image')



user_router=NestedDefaultRouter(router, 'user', lookup='user')   # The same name as  router.register('user'
user_router.register('images',SingleUserViewSet, basename='user-images')

# image_router=NestedDefaultRouter(router, 'userimage', lookup='userimage')    # The same name as  router.register('userimage'
# image_router.register('users',SingleImageViewSet, basename='images-user')

# Example Nested link
# http://127.0.0.1:8000/api/user/1/images/84/
# http://127.0.0.1:8000/api/user/1/images/84/

# http://127.0.0.1:8000/api/userimage/62/
# http://127.0.0.1:8000/api/userimage/62/

# http://127.0.0.1:8000/api/userimage/62/


urlpatterns = [
    # path(r'^$', RedirectView.as_view(url='api/'),name='base'),
    path('', RedirectView.as_view(url='api/'),name='base'),
    path('api/admin/', admin.site.urls),
    path('api/', include((router.urls,'api'))),
    path('api/', include((user_router.urls,'nested'))),
    # path('api/', include((image_router.urls,'nested'))),
    path('token/<hash>/', TokenView.as_view(), name='apiview')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

