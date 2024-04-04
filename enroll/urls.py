from django.urls import path
from enroll.views import home, save_data, delete_data, edit_data
from django.urls import path


urlpatterns = [
    path('add/', home, name='home'),
    path('save/', save_data, name='save'),
    path('delete/', delete_data, name='delete'),
    path('edit/', edit_data, name='edit'),
]