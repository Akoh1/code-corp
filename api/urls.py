from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'change', views.QuestionViewSet)


urlpatterns = [
    path('users/', views.ProfileView.as_view()),
    path('users/<int:pk>/', views.ProfileDetail.as_view()),
    path('tags/', views.TagsView.as_view()),
    path('tags/<int:pk>/', views.TagsDetail.as_view()),
    path('question/', views.QuestionView.as_view()),
    path('question/<int:pk>/', views.QuestionDetail.as_view()),
    path('answers/', views.AnswersView.as_view()),
    path('answers/<int:pk>/', views.AnswersDetail.as_view()),
    path('question/comment/', views.QuesCommentView.as_view()),
    path('question/comment/<int:pk>/', views.QuesCommentDetail.as_view()),
    path('answers/comment/', views.AnsCommentView.as_view()),
    path('answers/comment/<int:pk>/', views.AnsCommentDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns += router.urls