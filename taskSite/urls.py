from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('analytic.urls')), #we add the Blogs url as default_url
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #here we configure the media url
