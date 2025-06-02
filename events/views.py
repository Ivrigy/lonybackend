from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Event, EventComment, EventLike
from .serializers import (
    EventSerializer,
    EventCommentSerializer,
    EventLikeSerializer,
)
from django.shortcuts import get_object_or_404


class EventListCreateAPIView(generics.ListCreateAPIView):
    queryset = Event.objects.all().order_by('-created_at')
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class EventRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_update(self, serializer):
        serializer.save(owner=self.request.user)


class EventCommentListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = EventCommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        event_id = self.kwargs.get('event_id')
        return EventComment.objects.filter(
            event__id=event_id
        ).order_by('created_at')

    def perform_create(self, serializer):
        event = get_object_or_404(Event, id=self.kwargs.get('event_id'))
        serializer.save(owner=self.request.user, event=event)


class EventCommentRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = EventComment.objects.all()
    serializer_class = EventCommentSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class EventLikeListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = EventLikeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        event_id = self.kwargs.get('event_id')
        return EventLike.objects.filter(
            event__id=event_id
        ).order_by('-created_at')

    def perform_create(self, serializer):
        event = get_object_or_404(Event, id=self.kwargs.get('event_id'))
        serializer.save(owner=self.request.user, event=event)


class EventLikeRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = EventLike.objects.all()
    serializer_class = EventLikeSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
