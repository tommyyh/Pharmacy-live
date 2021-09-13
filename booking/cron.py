from django.core.management import call_command

def cron_send():
  call_command('send_mail')