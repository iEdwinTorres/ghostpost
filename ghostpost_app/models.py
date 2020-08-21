from django.db import models
from django.utils import timezone


class BoastRoast(models.Model):
    boast_or_roast = ((True, "Boast"), (False, "Roast"))
    choices = models.BooleanField(choices=boast_or_roast, default=True)
    user_post = models.CharField(max_length=280, default="")
    timeposted = models.DateTimeField(default=timezone.now)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)

    @property
    def totalvotes(self):
        return self.upvotes - self.downvotes
