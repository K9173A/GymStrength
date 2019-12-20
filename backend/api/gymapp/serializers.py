"""
Module for gymapp serializers.
"""
from rest_framework import serializers

from .models import (
    DatabaseExercise,
    Workout,
    WorkoutExercise,
    Set,
)


class DatabaseExerciseSerializer(serializers.ModelSerializer):
    """
    DatabaseExercise model serializer.
    """
    id = serializers.ReadOnlyField()

    class Meta:
        model = DatabaseExercise
        fields = (
            'id',
            'name',
            'description',
            'image',
            'muscle',
        )


class WorkoutSerializer(serializers.ModelSerializer):
    """
    Workout model serializer.
    """
    id = serializers.ReadOnlyField()

    class Meta:
        model = Workout
        fields = (
            'id',
            'date',
            'name',
            'user',
        )


class WorkoutExerciseSerializer(serializers.ModelSerializer):
    """
    WorkoutExercise model serializer.
    """
    id = serializers.ReadOnlyField()

    class Meta:
        model = WorkoutExercise
        fields = (
            'id',
            'workout',
            'information',
        )


class SetSerializer(serializers.ModelSerializer):
    """
    Set model serializer.
    """
    id = serializers.ReadOnlyField()

    class Meta:
        model = Set
        fields = (
            'weight',
            'repetition',
            'exercise',
        )
