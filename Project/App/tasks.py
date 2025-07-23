from background_task import background
from django.utils import timezone
from django.core.mail import send_mail
from .models import ReminderStatus

@background(schedule=0)
def send_remainder_to_check_on_children():
    now = timezone.localtime()
    current_hour = now.hour

    if current_hour < 8 or current_hour > 15 or current_hour % 2 != 0:
        return

    today = now.date()
    status, _ = ReminderStatus.objects.get_or_create(date=today)

    if status.confirmed_count >= 2 or status.email_count >= 5:
        return

    send_mail(
        subject="Reminder: Call the nanny",
        message=(
            f"This is reminder #{status.email_count + 1}. "
            "Please confirm by logging into the app and clicking the check-in button."
        ),
        from_email=None,
        recipient_list=['gregorykimbira7@gmail.com'],
        fail_silently=False,
    )

    status.email_count += 1
    status.save()
