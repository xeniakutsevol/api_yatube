from rest_framework.routers import DefaultRouter
from django.urls import include, path
from .views import PostViewSet, GroupViewSet, CommentViewSet
from rest_framework.authtoken import views

app_name = 'api'

router_v1 = DefaultRouter()
router_v1.register(r'v1/posts/(?P<id>\d+)/comments', CommentViewSet,
                   basename='comment')
router_v1.register('v1/posts', PostViewSet, basename='post')
router_v1.register('v1/groups', GroupViewSet, basename='group')


urlpatterns = [
    path('v1/api-token-auth/', views.obtain_auth_token),
    path('', include(router_v1.urls)),
]
