from rest_framework import serializers

from events_app.models import Events


class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = '__all__'
