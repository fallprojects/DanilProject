from django.db import models

class Tag(models.Model):
    name=models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.name

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

class Games(models.Model):
    name_of_game = models.CharField(max_length=100,null=True)
    time_of_game = models.DateTimeField(max_length=100,null=True)
    command_structure = models.TextField(max_length=1000,null=True)

    def __str__(self):
        return self.name_of_game

class Teams(models.Model):
    position = models.IntegerField(null=True)
    name = models.CharField(max_length=50,null=True)
    matches = models.IntegerField(null=True)
    points = models.IntegerField(null=True)
    goals_scored = models.IntegerField(null=True)
    goals_conceded = models.IntegerField(null=True)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name

class Players(models.Model):
    first_name = models.CharField(max_length=50,null=True)
    last_name = models.CharField(max_length=50,null=True)
    team = models.ForeignKey(Teams,null=True,on_delete=models.SET_NULL)
    number = models.IntegerField(null=True)

    def __str__(self):
        return self.last_name

class Rates(models.Model):
      RESULTS = (
          ('win','win'),
          ('draw','draw'),
          ('lose','lose')
      )

      results = models.CharField(max_length=100,null=True,choices=RESULTS)
      money = models.IntegerField(null=True)
      game = models.ManyToManyField(Games)








