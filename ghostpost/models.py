from django.db import models


class GhostPost(models.Model):
    is_boast = models.BooleanField(default=True)
    content = models.CharField(max_length=200)
    up_votes = models.IntegerField(default=0)
    down_votes = models.IntegerField(default=0)
    posted_time = models.DateTimeField(auto_now_add=True)

    def vote_score(self):

        return self.up_votes - self.down_votes

    def __str__(self):

        return self.content
