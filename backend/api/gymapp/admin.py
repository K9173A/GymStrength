from django.contrib import admin

from .models import (
    Muscle,
    WorkoutExercise,
    DatabaseExercise,
    Workout,
    Set,
)

admin.site.register(Muscle)
admin.site.register(WorkoutExercise)
admin.site.register(DatabaseExercise)
admin.site.register(Workout)
admin.site.register(Set)
