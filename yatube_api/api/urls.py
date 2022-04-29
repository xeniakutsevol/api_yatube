from rest_framework.routers import DefaultRouter
from django.urls import include, path
from .views import PostViewSet, GroupViewSet, CommentViewSet
from rest_framework.authtoken import views

router = DefaultRouter()
router.register(r'api/v1/posts/(?P<id>\d+)/comments', CommentViewSet,
                basename='comment')
router.register('api/v1/posts', PostViewSet, basename='post')
router.register('api/v1/groups', GroupViewSet, basename='group')


urlpatterns = [
    path('api/v1/api-token-auth/', views.obtain_auth_token),
    path('', include(router.urls)),
]
