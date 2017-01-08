from django.shortcuts import render
from django.views import View
from app.models import Log
from betfair_app.models import BFEvent
from livescores.models import LSEvent
from django.utils import timezone
import datetime

class Stats(View):
    def get(self, request):
        params=dict()
        logs=Log.objects.filter(dts__gt=timezone.now()-datetime.timedelta(hours=2)).order_by('-dts')
        params['logs']=logs
        #bfipc=BFEvent.objects.filter(bfodds__ip=True,bfodds__dtc__gt=timezone.now()-datetime.timedelta(minutes=30)).count()
        bfipc=BFEvent.objects.filter(dtc__gt=timezone.now()-datetime.timedelta(minutes=30)).count()
        params['bfipc']=bfipc
        lsipc=LSEvent.objects.filter(dtc__gt=timezone.now()-datetime.timedelta(minutes=30)).count()
        params['lsipc']=lsipc
        params['last_time_data_taken']=timezone.now()

        #dtadd=OPMeet.objects.latest('dtadd').dtadd
        #params['dtdiff']=(datetime.datetime.now(dtadd.tzinfo)-dtadd).seconds
        return render(request,'stats.html',params)