from rest_framework import routers
from rest_framework_nested.routers import NestedSimpleRouter

from . import views


app_name = "blog"

router = routers.DefaultRouter()
router.register(prefix='posts', viewset=views.PostView, basename='post')

post_router = NestedSimpleRouter(parent_router=router, parent_prefix='posts', lookup='post')
post_router.register(prefix='comments', viewset=views.CommentPostView, basename='comment')

likes_post_router = NestedSimpleRouter(parent_router=router, parent_prefix='posts', lookup='post')
likes_post_router.register(prefix='likes', viewset=views.LikesPostView, basename='likes')

comment_router = NestedSimpleRouter(parent_router=post_router, parent_prefix='comments', lookup='comment')
comment_router.register(prefix='likes', viewset=views.LikesCommentView, basename='likes')

urlpatterns = router.urls
urlpatterns += post_router.urls
urlpatterns += likes_post_router.urls
urlpatterns += comment_router.urls



__all__ = ('app_name', 'urlpatterns')
