from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='events',
    )
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=255)
    event_date = models.DateTimeField()
    event_link = models.URLField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return (
            f"{self.id} | {self.title} @ {self.location} "
            f"on {self.event_date:%Y-%m-%d %H:%M}"
        )


class EventComment(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='event_comments'
    )
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return (
            f"Comment {self.id} on Event {self.event.id} "
            f"by {self.owner.username}"
        )


class EventLike(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='event_likes'
    )
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name='likes'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('owner', 'event')
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner.username} liked Event {self.event.id}"
