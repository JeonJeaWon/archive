from django.db import models
# Create your models here.

class Archive(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date_published')
    body = models.TextField()

    def __str__(self):
        return self.title

    def t_summary(self):
        return self.title[:15]

    def b_summary(self):
        return self.body[:20]
