from rest_framework import serializers
from .models import Country, Language

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

        def create(self, validated_data):
            return Country(**validated_data)


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'

        def create(self, validated_data):
            return Language(**validated_data)
