from django.db import models

# Create your models here.
class Topic(models.Model):
    """The topics that will classify the articles"""
    discription = models.CharField(max_length=150)
    date_published = models.DateTimeField(auto_now_add=True)

class Entry(models.Model):
    """ represents entries for each Topic"""
    topic = models.ForeignKey(Topic, on_delete=models.DO_NOTHING)
    text = models.TextField()
    data_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural  = 'entries'

    def __str__(self):
        """ returen a discreption of the model"""
        return self.text[:50] + "..."


def __str__(self):
    """Return sring representation for the model"""
    return self.discription
