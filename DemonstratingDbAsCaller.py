import logging
from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.apps import apps

class UserAccount(models.Model):
    
    username = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

@receiver(post_save, sender=UserAccount)

def send_welcome_email(sender, instance, **kwargs):
    try:
        with transaction.atomic():
            EmailLog = apps.get_model('myapp', 'EmailLog')
            email_log = EmailLog(user=instance, email_type='welcome')
            email_log.save()
            raise ValueError('Simulated database error while sending email') 
    except ValueError as e:
        logging.error(f"Error sending welcome email: {e}")



#This means that if someone creates a new user account, the account gets saved to the database successfully. Even if something goes wrong in the signal handler (like an error while trying to send a welcome email), that error won't rollback the account creation. The account is saved, but the email sending fails separately, without affecting the account creation.

#So, the account is created, but the email doesn’t get sent because of the error. 
