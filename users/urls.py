from django.urls import path

from . import views

app_name = 'users'
urlpatterns = [
    path('<int:pk>/', views.UserView.as_view(), name='user'),
    path('role_register/', views.role_register, name='role_register'),
    path('settings/', views.settings, name='settings'),
    path('myworks/', views.my_works_view, name='my_works'),
    path('myreviews/', views.my_reviews, name='my_reviews')
    # path('person_register/', views.person_register, name='person_register')
]