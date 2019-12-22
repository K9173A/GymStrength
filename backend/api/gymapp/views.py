"""
Module for gymapp views.
"""
from django.db.models import Q
from rest_framework import generics, status
from rest_framework.response import Response

from .models import (
    Workout,
    DatabaseExercise,
)
from .serializers import (
    WorkoutSerializer,
    DatabaseExerciseSerializer,
)
from .pagination import GymPageNumberPagination


class WorkoutListAPIView(generics.ListAPIView):
    """
    Provides list of paginated workouts.
    Provides method(s): GET.
    """
    serializer_class = WorkoutSerializer
    pagination_class = GymPageNumberPagination

    def get_queryset(self):
        """
        Gets user workouts ordered by date.
        :return: user workouts.
        """
        return Workout.objects.filter(
            Q(is_active=True) &
            Q(user_id=self.request.user.id)
        ).order_by('date')


class WorkoutCreateAPIView(generics.CreateAPIView):
    """
    Creates new workout.
    Provides method(s): POST.
    """
    serializer_class = WorkoutSerializer

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
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            headers=headers
        )


class DatabaseExerciseListAPIView(generics.ListAPIView):
    """
    Provides list of paginated database exercises.
    Provides method(s): GET.
    """
    serializer_class = DatabaseExerciseSerializer
    pagination_class = GymPageNumberPagination

    def get_queryset(self):
        """
        Gets exercises from the database collection ordered by id.
        :return: database exercises.
        """
        return DatabaseExercise.objects.filter(is_active=True).order_by('id')
