from django.urls import re_path, include

urlpatterns = [
   re_path(r'^$', include('qa.urls')),
   re_path(r'^login/$', include('qa.urls'), name='login'),
   re_path(r'^signup/', include('qa.urls'), name='signup'),
   re_path(r'^question/(?P<id>[0-9]+)/$', include('qa.urls'), name='question'),
   re_path(r'^ask/', include('qa.urls'), name='ask'),
   re_path(r'^popular/', include('qa.urls'), name='popular'),
   re_path(r'^new/', include('qa.urls'), name='new'),
]
