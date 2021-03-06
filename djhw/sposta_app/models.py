from django.db import models

class MChamp(models.Model):
    mcid = models.IntegerField(null=True,db_index=True)
    sport = models.IntegerField(null=True)
    countryid = models.IntegerField(null=True)
    name = models.CharField(max_length=100,null=True)
    prize = models.CharField(max_length=20,null=True)
    link = models.CharField(max_length=100,null=True)
    gender = models.IntegerField(null=True) # filled with a binding
    surface = models.IntegerField(null=True)

class MPlayer(models.Model):
    mpid = models.IntegerField(null=True,db_index=True)
    name=models.CharField(max_length=100,db_index=True)
    db = models.DateTimeField(null=True)
    cid = models.IntegerField(null=True)
    gender = models.IntegerField(null=True) # filled with a binding

class MEvent(models.Model):
    meid = models.IntegerField(null=True,db_index=True)
    champ=models.ForeignKey(MChamp,null=True,db_index=True)
    res=models.CharField(max_length=50,null=True)
    p1=models.ForeignKey(MPlayer, related_name='mplayer1',null=True,db_index=True)
    p2=models.ForeignKey(MPlayer, related_name='mplayer2',null=True,db_index=True)
    dt = models.DateTimeField(null=True,db_index=True)
    free = models.IntegerField(null=True)
    def __unicode__(self):
        return '%s: [%s] %s - %s' % (self.id,self.meid,self.p1.name,self.p2.name)

class PlayerSetStats(models.Model):
    sc = models.IntegerField(db_index=True)
    meid = models.IntegerField(db_index=True)
    pid = models.IntegerField(db_index=True)
    tp = models.IntegerField(null=True)
    tw = models.IntegerField(null=True)
    s1w = models.IntegerField(null=True)
    s1ws2l = models.IntegerField(null=True)
    s1wml = models.IntegerField(null=True)
    s1ws2lmw = models.IntegerField(null=True)
    s1l = models.IntegerField(null=True)
    s1ls2w = models.IntegerField(null=True)
    s1lmw = models.IntegerField(null=True)
    s1ls2wml = models.IntegerField(null=True)
    def __unicode__(self):
        return '{t:%s,sc:0,tp:%s,tw:%s,s1w:%s,s1ws2l:%s,s1wml:%s,s1ws2lmw:%s,s1l:%s,s1ls2w:%s,s1lmw:%s,s1ls2wml:%s}' % (self.sc,self.tp,self.tw,self.s1w,self.s1ws2l,self.s1wml,self.s1ws2lmw,self.s1l,self.s1ls2w,self.s1lmw,self.s1ls2wml)
