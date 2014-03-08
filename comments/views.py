from django.contrib.comments.views.comments import post_comment
from recaptcha_works.decorators import fix_recaptcha_remote_ip

def custom_post_comment(request, next=None, using=None):
    return fix_recaptcha_remote_ip(post_comment)(request, next, using)

