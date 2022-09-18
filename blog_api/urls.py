from django.urls import path
from .views import PostLists, PostDetails

app_name = 'blog'

urlpatterns = [

    path('<int:pk>/',PostDetails.as_view(), name='detailcreate'),
    path('', PostLists.as_view(), name='listcreate'),
 
]
