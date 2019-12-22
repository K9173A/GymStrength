"""
Module for gymapp models definitions.
"""
from django.db import models

from api.authapp.models import User


class DatabaseExercise(models.Model):
    """
    DatabaseExercise model stores information about all exercises used in
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
    is_active = models.BooleanField(
        verbose_name='activity',
        default=True
    )

    def __str__(self):
        """
        Human-readable representation of database exercise.
        :return: string with database exercise name.
        """
        return f'{self.name}'


class Workout(models.Model):
    """
    Workout is a complex of exercises with set amount of sets and reps for
    each exercise.
    """
    date = models.DateField()
    name = models.CharField(
        max_length=128,
        default='Workout',
        blank=True
    )
    user = models.ForeignKey(
        User,
        related_name='user_set',
        on_delete=models.CASCADE
    )
    is_active = models.BooleanField(
        verbose_name='activity',
        default=True
    )

    def __str__(self):
        """
        Human-readable representation of workout.
        :return: string with user's workout and date.
        """
        return f'{self.user.name}\'s {self.name} ({self.date})'


class WorkoutExercise(models.Model):
    """
    Model which stores sets which are planned for the workout.
    """
    workout = models.ForeignKey(
        Workout,
        related_name='exercise_set',
        on_delete=models.CASCADE,
    )
    db_exercise = models.ForeignKey(
        DatabaseExercise,
        related_name='db_exercise_set',
        on_delete=models.CASCADE,
    )
    is_active = models.BooleanField(
        verbose_name='activity',
        default=True
    )

    def __str__(self):
        """
        Human-readable representation of workout exercise.
        :return: string with exercise name and workout's id.
        """
        return f'{self.db_exercise.name} (Workout id: {self.workout.id})'


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
        WorkoutExercise,
        related_name='exercise_set',
        on_delete=models.CASCADE
    )
    is_active = models.BooleanField(
        verbose_name='activity',
        default=True
    )

    def __str__(self):
        """
        Human-readable representation of workout exercise.
        :return: string with weight and amount of reps name and workout exercise's id.
        """
        return f'{self.weight}x{self.repetition} (Exercise id: {self.exercise.id})'
