from django.urls import path,include

from rest_framework.routers import DefaultRouter

from . import views

app_name = 'posts'

router = DefaultRouter()

router.register('posts',viewset=views.PostView, basename="posts")
router.register('answers',viewset=views.AnswerView, basename="answers")
router.register('comments',viewset=views.CommentView, basename="comments")
router.register('tags',viewset=views.TagView, basename="tags")

urlpatterns = [
    path("",include(router.urls)),
]