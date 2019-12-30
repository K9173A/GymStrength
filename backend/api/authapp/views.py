"""
Module for authapp views. Redefinition of Djoser views suitable for usage with
Vue.js.
"""
from django.conf import settings
from django.contrib.auth.tokens import default_token_generator

from rest_framework import status
from rest_framework.decorators import api_view
from djoser import utils
from djoser.conf import settings as djoser_settings
from templated_mail import mail
from rest_framework_simplejwt import views


@api_view(['POST'])
def login(request, *args, **kwargs):
    """
    Calls Djoser's endpoint view which creates a pair of tokens (JWT) and
    saves them into cookies storage.
    :param request: Request object.
    :param args: additional positional arguments.
    :param kwargs: additional key-value arguments.
    :return: response object with tokens.
    """
    response = views.TokenObtainPairView.post(request, *args, **kwargs)
    if response.status_code == status.HTTP_200_OK:
        response.set_cookie(
            key='access',
            value=response['access'],
            expires=settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'],
            domain=None,
            secure=True,
            httponly=True,
        )
        response.set_cookie(
            key='refresh',
            value=response['refresh'],
            expires=settings.SIMPLE_JWT['REFRESH_TOKEN_LIFETIME'],
            secure=True,
            httponly=True,
        )
    return response


class ActivationEmailView(mail.BaseEmailMessage):
    """
    View of Djoser's email activation template.
    """
    template_name = 'email/activation.html'

    def get_context_data(self, **kwargs):
        """
        Overrides context data needed in the activation template.
        :param kwargs: additional key-value arguments.
        :return: renewed context.
        """
        context = super(ActivationEmailView, self).get_context_data()
        user = context.get('user')
        context['uid'] = utils.encode_uid(user.pk)
        context['token'] = default_token_generator.make_token(user)
        context['url'] = djoser_settings.ACTIVATION_URL.format(**context)
        context['protocol'] = settings.DJOSER_GYMSTRENGTH.get('protocol')
        context['domain'] = settings.DJOSER_GYMSTRENGTH.get('domain_address')
        context['site_name'] = settings.DJOSER_GYMSTRENGTH.get('domain_name')
        return context


class ConfirmationEmailView(mail.BaseEmailMessage):
    """
    View of Djoser's email confirmation template.
    """
    template_name = 'email/confirmation.html'

    def get_context_data(self, **kwargs):
        """
        Overrides context data needed in the confirmation template.
        :param kwargs: additional key-value arguments.
        :return: renewed context.
        """
        context = super(ConfirmationEmailView, self).get_context_data()
        context['site_name'] = settings.DJOSER_GYMSTRENGTH.get('domain_name')
        return context
