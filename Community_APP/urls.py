
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from django.views.generic.base import TemplateView 
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('django.contrib.auth.urls')),
    path('',views.home,name='home'),
    path('signup/', views.signup, name='signup'),
    path('post/new',views.post_new,name='new_post'),
    path('/auth/logout',views.logout_view,name='logout_view'),
    path('search/' ,views.search_view ,name='search_view'),
]
