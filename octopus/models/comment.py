from django.db import models
from django.urls import reverse


class Comment(models.Model):
    class Meta:
        verbose_name_plural = 'comment'

    text = models.TextField(blank=False)
    name = models.CharField(unique=True, max_length=200)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'{} - {}'.format(self.name, self.text[:40])

    def get_absolute_url(self):
        return reverse('comment-detail', kwargs={'pk': self.pk})