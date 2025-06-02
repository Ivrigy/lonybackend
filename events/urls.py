from django.urls import path
from .views import (
    EventListCreateAPIView,
    EventRetrieveUpdateDestroyAPIView,
    EventCommentListCreateAPIView,
    EventCommentRetrieveDestroyAPIView,
    EventLikeListCreateAPIView,
    EventLikeRetrieveDestroyAPIView,
)

urlpatterns = [
    path(
        '',
        EventListCreateAPIView.as_view(),
        name='event-list-create',
    ),
    path(
        '<int:pk>/',
        EventRetrieveUpdateDestroyAPIView.as_view(),
        name='event-detail',
    ),
    path(
        '<int:event_id>/comments/',
        EventCommentListCreateAPIView.as_view(),
        name='event-comment-list-create',
    ),
    path(
        'comments/<int:pk>/',
        EventCommentRetrieveDestroyAPIView.as_view(),
        name='event-comment-detail',
    ),
    path(
        '<int:event_id>/likes/',
        EventLikeListCreateAPIView.as_view(),
        name='event-like-list-create',
    ),
    path(
        'likes/<int:pk>/',
        EventLikeRetrieveDestroyAPIView.as_view(),
        name='event-like-detail',
    ),
]
