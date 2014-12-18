from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Question(models.Model):
    def __unicode__(self):
        return self.question_text
    
    question_text = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('Date published')
    
    def was_published_recently(self):
        return timezone.now() >= self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_descripton = 'Published recently?'    
    
class Choice(models.Model):
    def __unicode__(self):
        return self.choice_text
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default=0)
