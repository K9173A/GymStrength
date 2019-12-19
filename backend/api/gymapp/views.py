"""
Module for gymapp views.
"""
from rest_framework import generics, status
from rest_framework.response import Response

from .serializers import (
    Workout, DatabaseExercise,
)
from .pagination import GymPageNumberPagination


class WorkoutListAPIView(generics.ListAPIView):
    """
    Provides list of paginated workouts.
    Provides method(s): GET.
    """
    serializer_class = Workout
    pagination_class = GymPageNumberPagination


class WorkoutCreateAPIView(generics.CreateAPIView):
    """
    Creates new workout.
    Provides method(s): POST.
    """
    serializer_class = Workout

    def create(self, request, *args, **kwargs):
        """
        Creates Workout.
        :param request: Request instance.
        :param args: additional arguments.
        :param kwargs: additional key-value arguments.
        :return: Response object.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class DatabaseExerciseListAPIView(generics.ListAPIView):
    """
    Provides list of paginated database exercises.
    Provides method(s): GET.
    """
    serializer_class = DatabaseExercise
    pagination_class = GymPageNumberPagination
