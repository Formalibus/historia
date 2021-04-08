from django.conf.urls import url
from django.urls import path, include
from .views import (FabulaListApiView, FabulaDetailApiView)

urlpatterns = [
    path('', FabulaListApiView.as_view()),
    path('<int:fabula_id>/', FabulaDetailApiView.as_view())
]
