from django.urls import path, include
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('add/', views.blog_add, name='addblog'),
    path('', views.posts, name="home"),
    path('blogs/<int:user_id>', views.user_blog, name='blogs'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>', views.post_detail_view, name="post_detail"),
    path('accounts/', include('django.contrib.auth.urls'))
]
