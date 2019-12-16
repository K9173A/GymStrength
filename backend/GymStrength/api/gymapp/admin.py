from django.contrib import admin

from .models import (
    Muscle,
    WorkoutExercise,
    ExerciseInformation,
    Workout,
    Set,
)

admin.site.register(Muscle)
admin.site.register(WorkoutExercise)
admin.site.register(ExerciseInformation)
admin.site.register(Workout)
admin.site.register(Set)
