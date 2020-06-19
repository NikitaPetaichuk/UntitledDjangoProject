from django.urls import re_path, include
from django.contrib import admin


admin.autodiscover()
urlpatterns = [
   re_path(r'^', include('qa.urls')),
   re_path(r'^admin/', admin.site.urls)
]
