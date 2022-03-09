from django.urls import path
from . import views
from rest_framework import routers
from .views import *
from django.conf.urls import include

router = routers.DefaultRouter()
router.register('students',students)
router.register('persons',persons)
router.register('instructors', instructors)
urlpatterns = [
    path('',include(router.urls)),
]



