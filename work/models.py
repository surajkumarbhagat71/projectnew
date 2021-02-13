from django.db import models

# Create your models here.

class Url(models.Model):
    url_id = models.AutoField(primary_key=True)
    urls = models.URLField()


class EventDetail(models.Model):
    ed_id = models.AutoField(primary_key=True)
    url = models.ForeignKey(Url,on_delete=models.CASCADE)
    title  = models.CharField(max_length=200 ,default="")
    datetime = models.CharField(max_length=200,default="")
    location = models.CharField(max_length=200,default="")

    def __str__(self):
        return self.title