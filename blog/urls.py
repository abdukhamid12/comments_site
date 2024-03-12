from django.urls import path, include

from blog import views

urlpatterns = [
    path('', views.index, name='index'),
    path('portfolio/', views.home, name='portfolio'),
    path('<tag>/', views.index, name='category_tag'),
    path('post/<int:pk>', views.add_comment_to_post, name='add_comment_to_post'),
    path('home/', views.home, name='home'),
    path('accounts/', include("django.contrib.auth.urls")),
    path('register/', views.register, name='register')
]