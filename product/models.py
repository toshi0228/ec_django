from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField('カテゴリー名', max_length=32)
    
    def __str__(self):
        return self.name
    
    
class Plan(models.Model):
    category = models.ForeignKey(Category, null=True, blank=True,
                                 on_delete=models.SET_NULL)
    plan_title = models.CharField('プラン名', max_length=128)
    price = models.PositiveIntegerField('価格')
    
    
    def __str__(self):
        return self.name