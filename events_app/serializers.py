from rest_framework import serializers
from .models import Event, EventPhoto, EventVideo, EventLinkVideo, Registration
from config.services import fix_phone


class EventPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventPhoto
        fields = "__all__"

class EventVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventVideo
        fields = "__all__"


class EventLinkVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventLinkVideo
        fields = "__all__"


class EventsSerializer(serializers.ModelSerializer):
    photo = EventPhotoSerializer(many=True)
    video = EventVideoSerializer(many=True)
    link_video = EventLinkVideoSerializer(many=True)

    class Meta:
        model = Event
        fields = "__all__"


class RegistrationSerializer(serializers.ModelSerializer):
    event = serializers.PrimaryKeyRelatedField(
        queryset=Event.objects.all(), required=True,
        )
    def validate_phone(self, value):
        return fix_phone(value)
    

    class Meta:
        model = Registration
        fields = "__all__"
