from django.urls import path
from . import views

# URLs here do NOT handle HTTP methods (GET, POST, PUT, HEAD)
urlpatterns = [
    path('', views.index, name='index'),
    path('compare.html', views.CompareConfigView.as_view(), name='compare_config'),
    # path('compare.html', views.compare_config, name='compare_config'),
    path('compare_success.html', views.compare_success, name='compare_success'),
    path('upload.html', views.UploadConfigView.as_view(), name='upload_config'),
    # path('upload.html', views.upload_config, name='upload_config'),
    path('upload_success.html', views.upload_success, name='upload_success'),
]