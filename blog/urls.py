from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('animal/<str:id_animal>/', views.post_details, name='post_details'),
    path('animal/<str:id_animal>/?<str:message>', views.post_details, name='post_detail_mes'),
]
