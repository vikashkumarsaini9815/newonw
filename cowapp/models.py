from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=255, null = True, blank = True)
    contact = models.CharField(max_length=12, blank=True, unique=True)
    email = models.EmailField()
    address = models.TextField()
    comment = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    join_date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.contact

class Amount_info(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE, related_name="user")
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.amount