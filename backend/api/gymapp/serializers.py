"""
Module for gymapp serializers.
"""
from rest_framework import serializers

from .models import (
    Muscle,
    DatabaseExercise,
    Workout,
    WorkoutExercise,
    Set,
)


class MuscleSerializer(serializers.ModelSerializer):
    """
    Muscle model serializer.
    """
    id = serializers.ReadOnlyField()

    class Meta:
        model = Muscle
        fields = (
            'id',
            'name',
        )


class ExerciseInformationSerializer(serializers.ModelSerializer):
    """
    ExerciseInformation model serializer.
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
