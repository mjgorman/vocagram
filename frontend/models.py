from django.db import models

# Create your models here.
class Post(models.Model):
    user = models.CharField(max_length=16)
    title = models.CharField(max_length=140)
    body = models.TextField() # This will become audio file
    pub_date = models.DateTimeField('date published')
    likes = models.IntegerField()
    
    def __unicode__(self):
        return self.title
