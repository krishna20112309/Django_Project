
from django.contrib import admin
from django.urls import path,re_path
from myapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='login'),
    # for registration
    path('reg/',user_reg,name='reg'),
    #for check username and password
    path('auth/',user_auth,name='check_auth'),
    #path('index/',index_page,name='index'),
    path('logout/',user_logout,name='logout'),
    re_path('detail/(\d+)',detail_post,name='detail'),
    re_path('delete_post/(\d+)/',delete,name='delete')
    
]
