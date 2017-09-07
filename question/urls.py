from django.conf.urls import url
from .views import search_questions
from .views import get_question_answer

urlpatterns = [
    url(r'^get-answer/(?P<question_column>[a-zA-Z\w|\W]+)/$', get_question_answer, name='get_question_answer'),
    url(r'^search/(?P<search_term>[a-zA-Z\w|\W]+)/$', search_questions, name='search_question')
]