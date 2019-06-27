from django.urls import path
from . import views

urlpatterns = [
    path('', views.myfiles, name='myfiles'),
    path('create_folder', views.create_folder, name='create_folder'),
    path('upload_file', views.upload_file, name='upload_file'),
    path('folders/<int:folder_id>', views.folders, name='folders'),
    path('search', views.search, name='search'),
    # File Operations
    path('move/<str:file_type>', views.move, name="move"),
    path('rename/<str:file_type>', views.rename, name="rename"),
    path('remove/<str:file_type>', views.remove, name="remove"),
    path('publish/<str:file_type>', views.publish, name="publish"),
    path('download/<int:file_id>', views.download, name="download"),
    path('share', views.share, name="share")
]
