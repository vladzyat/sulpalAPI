"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


from core import settings
from . import yasg

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('apps.customers.urls')),
    path('api/verify_phone/', include('apps.verification_phone.urls')),
    path('api/verify_email/', include('apps.verification_email.urls')),
    path('api/shop/', include('apps.products.urls')),
    path('api/orders/', include('apps.orders.urls')),
    path('api/reviews/', include('apps.reviews.urls')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += yasg.urlpatterns