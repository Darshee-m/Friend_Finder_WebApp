from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from friendapp import views as v

from friend_finder.views import home

from friendapp.views import login_view, register_view, logout_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', v.login_view ),
    #path('admin/', admin.site.urls),
    #path('', home),
    #path('friendapp/login/', login_view),
    #path('friendapp/register/', register_view),
    #path('friendapp/logout/', logout_view)
]
