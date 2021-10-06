from django.db.models import fields
from rest_framework import serializers
from app.models import Character, Pirate, Insult

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ('name', 'description', 'role', )

    def to_representation(self, instance):
        data = super(CharacterSerializer, self).to_representation(instance=instance)
        data['role'] = "Personaje principal" if data['role'] == 'MC' else "Personaje secundario"

        return data

class PirateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pirate
        fields = ('name', 'description', 'is_captain', 'role', )

    def to_representation(self, instance):
        data = super(PirateSerializer, self).to_representation(instance=instance)
        data['name'] = f"Capitán {data['name']}" if data['is_captain'] else f"Pirata {data['name']}"
        data['role'] = "Personaje principal" if data['role'] == 'MC' else "Personaje secundario"

        return data

class InsultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insult
        fields = ('insult', 'comeback', )

    def to_representation(self, instance):
        data = super(InsultSerializer, self).to_representation(instance=instance)
        data['insult'] = data['insult'].capitalize()

        return data