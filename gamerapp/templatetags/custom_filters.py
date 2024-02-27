# yourapp/templatetags/custom_filters.py
from django import template
from django.utils import timezone
from datetime import timedelta

register = template.Library()

@register.filter(name='time_ago_format')
def time_ago_format(date_created):
    now = timezone.now()
    delta = now - date_created

    if delta < timedelta(days=1):
        hours = delta.seconds // 3600
        if hours > 0:
            return f"{hours} {'hour' if hours == 1 else 'hours'} ago"
        else:
            minutes = delta.seconds // 60
            return f"{minutes} {'minute' if minutes == 1 else 'minutes'} ago"
    else:
        return date_created.strftime('%B %d, %Y')
