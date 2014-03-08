from django.contrib.comments.forms import CommentForm
from django.contrib.comments.models import Comment
from recaptcha_works.fields import RecaptchaField

class CustomCommentForm(CommentForm):
    recaptcha = RecaptchaField(label='Are you human?', required=True)
    def get_comment_model(self):
        return Comment

