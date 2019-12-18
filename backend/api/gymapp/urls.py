"""
Module for gymapp URLs.
"""
from django.urls import path

import api.gymapp.views as gymapp_api


app_name = 'gymapp'

urlpatterns = [
    path('list_workouts/user/', gymapp_api.WorkoutListAPIView.as_view()),
    # path('list_db_exercises/', gymapp_api.DatabaseExerciseListAPIView.as_view()),
    # path('list_exercises/user/', gymapp_api.WorkoutExerciseListAPIView.as_view()),
]
