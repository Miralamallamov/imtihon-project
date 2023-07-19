from django.db import models
# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    # author = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.title


    # class Meta:
    #     bd_table = "news"



