from django.shortcuts import render
from django.views import View
from main_app.models import ALog
from betfair_app.models import BFChamp,BFEvent,BFPlayer,BFOdds
from django.utils import timezone
from django.utils.timezone import localtime
import datetime
import plotly 
from plotly.offline.offline import _plot_html
from plotly.graph_objs import Scatter
from django.core import serializers
from django.http import JsonResponse
from django.http import HttpResponse

class Inspect(View):
    def get(self, request):
        params=dict()
        template='bf_all.html'
        if request.method == 'GET':
            if 'cid' in request.GET:
                cid=int(request.GET['cid'])
                events=BFEvent.objects.filter(cid__id=cid)
                params['champ']=events[0].cid.name if len(events)>0 else ''
                params['events']=events
                template='bf_champ.html'
            if 'evid' in request.GET and 'isip' in request.GET:
                evid=int(request.GET['evid'])
                isip=request.GET['isip']=='1'
                event=BFEvent.objects.get(id=evid)
                params['event']=event
                oddschanges=BFOdds.objects.filter(eid=event,ip=isip).order_by('dtc')
                params['isip0']='' if isip else ' disabled'
                params['isip1']=' disabled' if isip else ''
                try:
                    goip=BFOdds.objects.filter(eid=event,ip=False).latest('dtc').dtc
                except:
                    goip=''
                params['goip']=goip
                params['oddschanges']=oddschanges
                plotly.tools.set_credentials_file(username='hwait', api_key='mYs3EJORl98E0vxkWvGr')
                xr=[i.dtc for i in oddschanges]
                y1r=[i.b1odds for i in oddschanges]
                y2r=[i.b2odds for i in oddschanges]
                figure_or_data = [Scatter(x=xr, y=y1r,mode = 'lines',name = event.pid1.name),Scatter(x=xr, y=y2r,mode = 'lines',name = event.pid2.name)]
                config = {}
                config['showLink'] = False
                plot_html = plot_html, plotdivid, width, height = _plot_html(
                    figure_or_data,config, True, '100%', 500, False)
                resize_script = ''
                if width == '100%' or height == '100%':
                    resize_script = (
                        ''
                        '<script type="text/javascript">'
                        'window.removeEventListener("resize");'
                        'window.addEventListener("resize", function(){{'
                        'Plotly.Plots.resize(document.getElementById("{id}"));}});'
                        '</script>'
                    ).format(id=plotdivid)
                params['graph'] = ''.join([
                            plot_html,
                            resize_script])
                template='bf_event.html'
            else:
                params['cid']=''
                champs=BFChamp.objects.filter(bfevent__isnull=False).distinct()
                params['champs']=champs
        return render(request,template,params)

class ApiGet(View):
    def get(self, request):
        params=dict()
        try:
            lastget=ALog.objects.filter(name='bf_get').latest('dts').dts
        except:
            lastget=timezone.make_aware(datetime.datetime(2016, 12, 31))
        champs=BFChamp.objects.filter(lid=None)
        players=BFPlayer.objects.filter(lid=None)
        events=BFEvent.objects.filter(lid=None)
        odds=BFOdds.objects.filter(dtc__gt=lastget)
        response_data = {}
        response_data['result'] = 'Success'
        response_data['players'] = serializers.serialize('json', players)
        response_data['champs'] = serializers.serialize('json', champs)
        response_data['events'] = serializers.serialize('json', events)
        response_data['odds'] = serializers.serialize('json', odds)

        #try:
        #    response_data['result'] = 'Success'
        #    response_data['message'] = serializers.serialize('json', opmeet)
        #except:
        #    response_data['result'] = 'Error'
        #    response_data['message'] = 'Script has not ran correctly'
        return HttpResponse(JsonResponse(response_data), content_type="application/json")

