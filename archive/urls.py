from django.urls import path
from . import views

urlpatterns = [
    path('', views.archivemain, name = 'archivemain'),
    path('<int:archive_id>', views.archivedetail, name = 'archivedetail'),
]