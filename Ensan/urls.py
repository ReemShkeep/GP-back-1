from django.urls import path
from . import views

urlpatterns = [
    path('classes',views.classes,name='classes'),
    path('students',views.students,name='students'),
    path('instructors',views.instructors,name='instructors'),
    path('category',views.category,name='category'),
    path('albumphotos',views.albumPhotos,name='albumPhotos'),
    path('albums',views.albums,name='albums'),
    path('news',views.news,name='news'),
    path('collections',views.collections,name='collections'),



    path('albumphotonew/<int:colid>/<int:Aid>',views.albumPhotosnew,name='albumPhotonew'),

    # path('api-add', views.api_add_student,name='api-add'),
    # path('api-edit/<st_id>', views.api_edit_student,name='api-edit'),
    # path('api-del/<st_id>', views.api_del_student,name='api-del'),
]



