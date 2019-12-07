"""
Module for mainapp serializers.
"""
from rest_framework import serializers

from .models import (Muscle, Exercise, Set)


class MuscleSerializer(serializers.ModelSerializer):
    """
    Muscle model serializer.
    """
    id = serializers.ReadOnlyField()

    class Meta:
        model = Muscle
        fields = (id, name,)


class ExerciseSerializer(serializers.ModelSerializer):
    """
    Exercise model serializer.
    """
    id = serializers.ReadOnlyField()

    class Meta:
        model = Exercise
        fields = (id, name, description, image, muscle)


class SetSerializer(serializers.ModelSerializer):
    """
    Set model serializer.
    """
    id = serializers.ReadOnlyField()

    class Meta:
        model = Set
        fields = (weight, repetition)
