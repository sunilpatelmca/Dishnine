from django.db import models
from Publication.models import Author

class Home(models.Model):

    title = models.CharField(max_length=50,help_text='Maximum 50 characters.')
    #author = models.ForeignKey(Author)
    content = models.TextField()

    class Meta:
	    verbose_name_plural = "Home"


    class Admin:
	    pass

    def __unicode__(self):
	    return self.title
