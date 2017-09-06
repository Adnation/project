from django.conf.urls import url
from .views import get_question_answer

urlpatterns = [
	url(r'^get-answer/(?P<question_column>[a-zA-Z\w|\W]+)/$', get_question_answer, name='get_question_answer')
]
