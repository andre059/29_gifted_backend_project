from rest_framework import serializers
from .models import Event, EventPhoto, EventVideo, EventLinkVideo, Registration

class EventPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventPhoto
        fields = ['id', 'link']

class EventVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventVideo
        fields = ['id', 'link']

class EventLinkVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventLinkVideo
        fields = ['id', 'link_video', 'date']


class EventsSerializer(serializers.ModelSerializer):
    photo = EventPhotoSerializer(many=True, read_only=True)
    video = EventVideoSerializer(many=True, read_only=True)
    link_video = EventLinkVideoSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = [
            'id', 
            'name_of_event', 
            'description_of_event',
            'address_of_event', 
            'date_time_of_event', 
            'end_of_event',
            'photo', 
            'video', 
            'link_video',
        ]


class RegistrationSerializer(serializers.ModelSerializer):
    event = serializers.PrimaryKeyRelatedField(queryset=Event.objects.all(), required=True)

    class Meta:
        model = Registration
        fields = [
            'id',
            'event', 
            'first_name', 
            'last_name', 
            'email', 
            'phone', 
            'comment', 
            'timestamp', 
            'terms_agreed',
            ]
