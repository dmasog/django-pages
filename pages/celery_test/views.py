from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

from celery.result import AsyncResult
from celery_test.tasks import do_something_long
from django.utils import simplejson as json

import logging

# Create your views here.

def start_celery_task(request):
    task = do_something_long.delay()
    
    return HttpResponseRedirect("%s%s" % ('/celery_progress?task_id=',task.id) )

def monitor_celery_task(request):
    if 'task_id' in request.GET:
        task_id = request.GET['task_id']
    else:
        return HttpResponse('No task_id passed')
  
    task = AsyncResult(task_id)
    data = task.result or task.state

    return HttpResponse(json.dumps(data), mimetype='application/json')
