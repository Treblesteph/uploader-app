from django.conf.urls import url
from file_upload.uploader.views import list

urlpatterns = [
    url(r'^list/$', list, name='list')
]
