"""
Module for authapp views. Redefinition of Djoser views suitable for usage with
Vue.js.
"""
from django.conf import settings
from django.contrib.auth.tokens import default_token_generator

from djoser import utils
from djoser.conf import settings as djoser_settings
from templated_mail import mail


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
