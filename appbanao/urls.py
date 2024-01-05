from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('add/', views.blog_add, name='addblog'),
    path('', views.posts, name="home"),
    path('details', views.details, name="details"),
    path('appointment', views.appointment, name="appointment"),
    path('doctors', views.doctor_list, name="doctors"),
    path('blogs/<int:user_id>', views.user_blog, name='blogs'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>', views.post_detail_view, name="post_detail"),
    path('accounts/', include('django.contrib.auth.urls'))
]
