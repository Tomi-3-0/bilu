from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # set the path to our new app
    path('', include('shop.urls'))
]
