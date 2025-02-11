from rest_framework import serializers
from my_project.models import Thread


class ThreadSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())  # Automatically set to current user
    participants = serializers.ListField(child=serializers.CharField())

    class Meta:
        model = Thread
        fields = '__all__'

    def create(self, validated_data):
        existing_thread = Thread.objects.filter( **validated_data).first()

        if existing_thread:
            return existing_thread

        return super().create(validated_data)