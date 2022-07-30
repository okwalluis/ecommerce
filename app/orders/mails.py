from django.urls import reverse
from django.conf import settings
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

class Mail:
    @staticmethod
    def get_absolute_url(url):
        if settings.DEBUG: # si nos encontramos en modo desarrollo
            return 'http://localhost:8000{}'.format(
                reverse(url)
            )

    @staticmethod
    def send_complete_order(order, user):
        subject = 'Tu pedido ha sido enviado'
        template = get_template('orders/mails/complete.html')
        content = template.render({
            'user': user,
            'next_url': Mail.get_absolute_url('orders:completeds')
        })
        #mensaje
        message = EmailMultiAlternatives(subject,
                                        'Mensaje importante',
                                        settings.EMAIL_HOST_USER,
                                        [user.email])
        #contenido
        message.attach_alternative(content, 'text/html')
        message.send()