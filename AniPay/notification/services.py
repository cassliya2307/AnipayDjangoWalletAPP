from django.core.mail import send_mail

from notification.models import Notification


def create_notification(user):
    notification = Notification.objects.create(
        user=user,
        message=f"""
        Hello {user.first_name}! Welcome to AniPay!
        Your account has been created!
        Your wallet number is {user.wallet.wallet_number}
        Your alternate wallet number is {user.wallet.account_number}
"""
    )
    send_mail(
        subject="Welcome to AniPay!",
        message=notification.message,
        from_email="",
        recipient_list=[user.email],
        fail_silently=True
    )

    notification.is_read = True
    notification.save()