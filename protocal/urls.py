from django.urls import path

from protocal.views import NewsAPI

urlpatterns = [
    path('news/', NewsAPI.as_view(), name='news'),
]
