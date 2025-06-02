from rest_framework import serializers
from django.utils import timezone
from .models import Event, EventComment, EventLike


class EventSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    is_owner = serializers.SerializerMethodField()
    comments_count = serializers.IntegerField(
        source="comments.count", read_only=True
    )
    likes_count = serializers.IntegerField(
        source="likes.count", read_only=True
    )

    def get_is_owner(self, obj):
        request = self.context.get("request")
        return bool(request and request.user == obj.owner)

    def validate_event_date(self, value):
        if value < timezone.now():
            raise serializers.ValidationError(
                "The event date cannot be in the past."
            )
        return value

    class Meta:
        model = Event
        fields = [
            "id",
            "owner",
            "is_owner",
            "title",
            "description",
            "location",
            "event_date",
            "event_link",
            "comments_count",
            "likes_count",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "owner",
            "comments_count",
            "likes_count",
            "created_at",
            "updated_at",
        ]


class EventCommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    is_owner = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context.get("request")
        return bool(request and request.user == obj.owner)

    def get_created_at(self, obj):
        from django.contrib.humanize.templatetags.humanize import naturaltime

        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        from django.contrib.humanize.templatetags.humanize import naturaltime

        return naturaltime(obj.updated_at)

    class Meta:
        model = EventComment
        fields = [
            "id",
            "owner",
            "is_owner",
            "event",
            "content",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["owner", "created_at", "updated_at"]


class EventLikeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = EventLike
        fields = [
            "id",
            "event",
            "owner",
            "created_at",
        ]
        read_only_fields = ["owner", "created_at"]

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except Exception:
            raise serializers.ValidationError(
                {"detail": "You have already liked this event."}
            )
