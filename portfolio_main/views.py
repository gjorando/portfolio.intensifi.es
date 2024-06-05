from django.shortcuts import render
from django.utils.translation import gettext as _, get_language
from django.utils import translation
from datetime import datetime
import requests
from .forms import ContactForm
from .app_settings import *


def home(request, lang):
    sendmail_enabled = SENDMAIL
    guitar_years = datetime.now().year - 2003
    form = ContactForm(request.POST or None, auto_id=False)
    send_message = True
    error_info = ""

    if lang != "":
        translation.activate(lang)
    active_lang = get_language

    if request.method == 'POST':
        if not form.is_valid():
            send_message = False
            error_info = _("Formulaire invalide. Vérifiez la saisie et réessayez. ")
        
        if not sendmail_enabled:
            send_message = False
            error_info = _("Toutes mes excuses. L'envoi de mail est actuellement désactivé. N'hésitez pas à me "
                           "contacter sur les réseaux sociaux ! ")
        
        if send_message:
            request_url = 'https://api.mailgun.net/v3/{0}/messages'.format(MAILGUN_DOMAIN)
            http_request = requests.post(request_url, auth=('api', MAILGUN_KEY), data={
                'from': '{0} <{1}@{2}>'.format(MAILGUN_COMMON_NAME, MAILGUN_SENDER, MAILGUN_DOMAIN),
                'to': MAILGUN_RECIPIENT,
                'subject': form.cleaned_data['subject'],
                'text': _('Reçu de {sender}\n{message}').format(
                    sender=form.cleaned_data['email'],
                    message=form.cleaned_data['content']
                )
            })

            if http_request.status_code != requests.codes.ok:
                error_info = _("L'envoi a échoué pour une raison inconnue. Réessayez plus tard ou contactez moi sur "
                               "les réseaux sociaux.")
                success_info = False
            else:
                success_info = True

            if success_info:
                http_request = requests.post(request_url, auth=('api', MAILGUN_KEY), data={
                    'from': '{0} <{1}@{2}>'.format(MAILGUN_COMMON_NAME, MAILGUN_SENDER, MAILGUN_DOMAIN),
                    'to': form.cleaned_data['email'],
                    'subject': _('Confirmation d\'envoi - portfolio.intensifi.es'),
                    'text': _("Vous m'avez envoyé un email via portfolio.intensifi.es. Je vais l'examiner et y "
                              "répondre dans les plus brefs délais.\nSujet : {subject}\nMessage :\n{message}\n\nSi "
                              "vous n'êtes pas à l'origine de ce message, merci d'ignorer le présent e-mail (et toutes "
                              "mes excuses pour le dérangement, n'hésitez pas à me contacter si cela se reproduit).\n"
                              "Ne répondez pas directement à ce mail ! Je ne le recevrai pas. Contactez moi plutôt "
                              "avec le formulaire sur portfolio.intensifi.es.").format(
                        subject=form.cleaned_data['subject'],
                        message=form.cleaned_data['content']
                    )
                })
                form = ContactForm()

    return render(request, 'portfolio_main/index.html', locals())
