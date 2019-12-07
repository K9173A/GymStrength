"""
Module for mainapp models definitions.
"""
from django.db import models

from api.authapp.models import User


class Muscle(models.Model):
    """
    Muscle model stores predefined set of muscle names which can be trained
    in the training routine.
    """
    name = models.CharField(
        max_length=128
    )


class ExerciseInformation(models.Model):
    """
    ExerciseInformation model stores information about all exercises used in
    the training process.
    """
    name = models.CharField(
        max_length=128
    )
    description = models.TextField(
        max_length=256,
        blank=True
    )
    image = models.ImageField(
        blank=True
    )
    muscle = models.ForeignKey(
        Muscle,
        related_name='muscle_set',
        on_delete=models.SET_NULL,
        null=True
    )


class WorkoutExercise(models.Model):
    workout = models.ForeignKey(
        Workout,

    )

class Set(models.Model):
    """
    Set defines number of repetitions with required weight.
    """
    weight = models.FloatField(
        default=1.0
    )
    repetition = models.IntegerField(
        default=1
    )
    exercise = models.ForeignKey(
        Exercise,
        related_name='exercise_set',
        on_delete=models.CASCADE
    )


class Workout(models.Model):
    """
    Workout is a complex of exercises with set amount of sets and reps for
    each exercise.
    """
    date = models.DateField()
    name = models.CharField(
        max_length=128,
        blank=True
    )
    sets = models.ManyToManyField(
        Set
    )
    user = models.ForeignKey(
        User,
        related_name='user_set',
        on_delete=models.CASCADE
    )
