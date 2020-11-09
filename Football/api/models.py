from django.db import models

class News(models.Model):
    CATEGORY = (
        ('EPL','EPL'),
        ('Bundesliga','Bundesliga'),
        ('La Liga','La Liga'),
        ('Seria A','Seria A'),
        ('RPL','RPL'),
    )
    name = models.CharField(max_length=100,null=True)
    description = models.CharField(max_length=1000,null=True)
    category = models.CharField(max_length=100,null=True,choices=CATEGORY)
    date_created = models.DateTimeField(auto_now_add=True,null=True)

