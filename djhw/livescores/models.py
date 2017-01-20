from django.db import models

class LSChamp(models.Model):
    mcid = models.IntegerField(null=True)
    sport = models.IntegerField()
    name = models.CharField(max_length=100)

class LSPlayer(models.Model):
    mpid = models.IntegerField(null=True)
    gender = models.IntegerField(null=True)
    name = models.CharField(max_length=50,db_index=True)
    link = models.CharField(max_length=100,null=True)

class LSEvent(models.Model):
    meid = models.IntegerField(null=True)
    lsid=models.IntegerField(unique=True)
    cid=models.ForeignKey(LSChamp,null=True,db_index=True)
    pid1=models.ForeignKey(LSPlayer, related_name='player1',null=True,db_index=True)
    pid2=models.ForeignKey(LSPlayer, related_name='player2',null=True,db_index=True)
    dtc = models.DateTimeField(null=True,db_index=True)

class LSGame(models.Model):
    eid=models.ForeignKey(LSEvent,null=True,db_index=True)
    setn=models.IntegerField()
    sc1=models.IntegerField()
    sc2=models.IntegerField()
    serve=models.IntegerField(null=True)
    prewin=models.IntegerField(null=True)
    dtc = models.DateTimeField(null=True,db_index=True)

class LSPoint(models.Model):
    gid=models.ForeignKey(LSGame,null=True,db_index=True)
    sc1=models.IntegerField()
    sc2=models.IntegerField()
    dtc = models.DateTimeField(null=True)
