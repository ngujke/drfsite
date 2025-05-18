from rest_framework import serializers
from .models import Players

class PlayersSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Players
        fields = "__all__"
