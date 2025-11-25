from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import HomeViews, LoginViews, SignupView
from .views import PostListView

urlpatterns = [
    path('', HomeViews.as_view(), name='home'),
    path('login/', LoginViews.as_view(), name='login'),
    path('signup/', SignupView.as_view(),name='signup'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('posts/', PostListView.as_view(), name='post_list'),

]