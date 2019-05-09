from django.urls import path
from . import views

urlpatterns = [
	path('', views.menu, name='menu'),
    path('blog', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('randomgen', views.randomgen, name='randomgen'),
    path('juno',views.juno, name='juno')
]


#path('actionUrl', views.randomgen, name='randomgen')