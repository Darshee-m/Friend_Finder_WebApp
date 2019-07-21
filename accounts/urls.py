from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
     path('admin/', admin.site.urls),
     path('createpost/', views.createpost, name='createpost'),
     path('showusers/', views.showusers, name='showusers'),

]
