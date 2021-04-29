from django.db import models

# Create your models here.

class City (models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name 
    

    # class Meta :
    #     verbose_name_plural ='cities'
    objects = models.Manager()    # yah likhne se class object is not member ka  problem  khatam ho jayega ....
