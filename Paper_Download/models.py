from django.db import models
from Publication.models import Subject,Level

class Paper_Download(models.Model):
    title = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject)
    level = models.ForeignKey(Level)
    description = models.TextField()
    paper = models.FileField(upload_to = '.',
                                blank = True, null = True,)
    published_date = models.DateTimeField()

    class Meta:
	    verbose_name_plural = "Paper_Download"

    class Admin:
	    list_display   = ('subject','title')
    search_fields  = ('title',)

    def __unicode__(self):
	    return "%s [%s - %s]"%(self.title,self.subject.name,self.level.name)
