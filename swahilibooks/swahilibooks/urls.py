
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',include('sales.urls')),
    path('admin/',admin.site.urls),
    path('sales/',include('sales.urls')),
    path('customers/',include('customers.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
