from django.urls import re_path
from qa.views import test, popular_questions, new_questions, question_page

urlpatterns = [
   re_path(r'^$', new_questions, name='question_list'),
   re_path(r'^popular/', popular_questions, name='popular'),
   re_path(r'^question/(?P<pk>\d+)/', question_page, name='question_detail'),
   re_path(r'^ask/', test, name='ask'),
   re_path(r'^login/', test, name='login'),
   re_path(r'^signup/', test, name='signup'),
   re_path(r'^new/', test, name='new'),
]
