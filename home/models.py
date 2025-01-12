from django.db import models
from django.contrib.auth.models import User
# Create your models here.




class Category(models.Model):
    categoryName = models.CharField(max_length=233)

    def __str__(self):
        return self.categoryName

class Expense(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=False)
    name = models.CharField(max_length=140)
    amount = models.IntegerField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.name