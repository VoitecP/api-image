from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from django.views.generic.base import RedirectView
from api.views import *
from api.viewsets import *
from .routers import router, user_router, image_router


urlpatterns = [
    path('api/', APIUrls.as_view(),name='base'),

    path('', RedirectView.as_view(url='api/'),name='api-v2'),
    path('api/admin/', admin.site.urls),

    path('api/userimage/<str:pk>/',DetailImageView.as_view(),name='userimages-id'),
    path('api/userimage/', UploadUserImageView.as_view(),name='userimage'),
    path('api/generic/userimage/<str:pk>/', UserImageGenericView.as_view(),name='userimage'),
    path('api/gallery/<str:pk>/', GalleryView.as_view(),name='userimage'),
    path('api/token/<hash>/', TokenView.as_view(), name='apiview'),

    path('api/v2/', include((router.urls,'api'))),
    path('api/v2/', include((user_router.urls,'user-nested-router'))),
    path('api/v2/', include((image_router.urls,'image-nested-router'))),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



