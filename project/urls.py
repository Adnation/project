"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from question.views import search_questions
from question.views import render_index_html
from question.views import get_question_answer
from question.views import preapre_dashboard_data

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^question/get-answer/(?P<question_column>[a-zA-Z\w|\W]+)/$', get_question_answer, name='get_question_answer'),
    url(r'^question/search/(?P<search_term>[a-zA-Z\w|\W]+)/$', search_questions, name='search_question'),
    url(r'^get-dashboard-data/$', preapre_dashboard_data, name='prepare_dashboard_data'),
    url(r'^$', render_index_html, name='home_page'),
]
