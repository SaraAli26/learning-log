from django.db import models

# Create your models here.
class Topic(models.Model):
    """The topics that will classify the articles"""
    text = models.CharField(max_length=150)
    date_published = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        """Return sring representation for the model"""
        return self.text


class Entry(models.Model):
    """ represents entries for each Topic"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    data_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural  = 'entries'

    def __str__(self):
        """ returen a discreption of the model"""
        the_text = self.text
        if len(the_text) > 50:
            return self.text[:50] + "..."
        else:
            return self.text
