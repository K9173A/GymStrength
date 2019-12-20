"""
Module for authapp models definitions.
"""
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.conf import settings

from djoser.signals import user_activated


class User(AbstractUser):
    """
    Django user model implementation.
    """
    pass


class UserProfile(models.Model):
    """
    UserProfile stores additional user information.
    """
    GENDER_CHOICES = (
        (0, 'Not Set'),
        (1, 'Male'),
        (2, 'Female')
    )
    user = models.OneToOneField(
        User,
        related_name='profile',
        on_delete=models.CASCADE
    )
    avatar = models.ImageField(
        verbose_name='avatar',
        upload_to=settings.USER_AVATARS_DIR_NAME,
        blank=True
    )
    gender = models.IntegerField(
        verbose_name='gender',
        choices=GENDER_CHOICES,
        default=0
    )
    height = models.IntegerField(
        verbose_name='height',
        blank=True
    )
    weight = models.IntegerField(
        verbose_name='weight',
        blank=True
    )

    def __str__(self):
        """
        Human-readable representation of user profile.
        :return: string user name and email.
        """
        return f'Profile of {self.user.name} ({self.user.email})'


@receiver(user_activated)
def save_user_profile(sender, user, request, **kwargs):
    """
    Creates a profile associated with activated User instance.
    Triggered when user_activated signal is being emitted by the ActivationView.
    :param sender: ActivationView subclass used to activate the user.
    :param user: User instance representing the activated account.
    :param request: HttpRequest in which the account was activated.
    :param kwargs: additional key-value arguments.
    :return:
    """
    (user_profile, created) = UserProfile.objects.get_or_create(user=user)
    if created:
        user_profile.save()
