from django.db import models

# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.email

class Item(models.Model):
    proname = models.CharField(max_length=255)
    minbid = models.DecimalField(max_digits=20, decimal_places=2)
    description = models.CharField(max_length=2000, null=True,)
    picture = models.ImageField(upload_to='images/', null=True, blank=True)
    date = models.DateField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE,related_name='%(class)s_requests_created')

class bid(models.Model):
    amount= models.DecimalField(max_digits=20, decimal_places=2)
    post= models.ForeignKey(Item, on_delete=models.CASCADE)
    bidder= models.ForeignKey(User, on_delete=models.CASCADE)