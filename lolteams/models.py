from django.db import models

# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=20, unique=True, error_messages={'unique' : "이미 존재하는 이름입니다."})
    total = models.PositiveIntegerField(default=0)
    win = models.PositiveIntegerField(default=0)
    lose = models.PositiveIntegerField(default=0)
    winrate = models.DecimalField(default=0, max_digits=3, decimal_places=2)
    create_date = models.DateTimeField()

class League(models.Model):
    blue = models.CharField(max_length=5)
    red = models.CharField(max_length=5)
    create_date = models.DateTimeField()

class Entry(models.Model):
    member = models.ForeignKey(Member, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=20)
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    result = models.CharField(max_length=5)
    camp = models.CharField(max_length=10)
    create_date = models.DateTimeField()