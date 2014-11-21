from django.http import HttpResponse
import datetime
import nltk
from nltk.corpus import wordnet as wn
import enchant

def home(request,parm=""):
    now = datetime.datetime.now()
    resp = "%s:<br><ol>" % parm 
    for i in wn.synsets(parm):
        resp += "<li>%s</li>" % i.definition()
    html = "<html><body>%s</ol></body></html>" % resp
    return HttpResponse(html)
