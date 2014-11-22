from django.http import HttpResponse
from encodings import *
from unicodedata import *
import datetime
import nltk
from nltk.corpus import wordnet as wn
import enchant

import subprocess

def pronunciation(p):
   ret = []
   if p == "":
      p = "dog"
   r = subprocess.call(["curl","-o","out","www.thefreedictionary.com/"+p])

   with open("out") as f:
      ln=f.read()

   while ln.find("Click for pronun") > 0:
      ind= ln.find("Click for pronun")
      ln = ln[ind+1:]
      hit = ln[ln.find(">")+1:ln.find(">")+200:].strip()
      if hit[0]=="(":
         hit= hit[1:hit.find(",")]
      else:
         hit= hit[:hit.find("<")]
      if hit[0]!="-":
         ret.append(hit)
   return ret

def home(request,parm=""):
    pronun = pronunciation(parm)
    now = datetime.datetime.now()
    resp = "%s     %s:<br><ol>" % (parm,pronun)
    for i in wn.synsets(parm):
        resp += "<li>%s</li>" % i.definition()
    html = "<html><body>%s</ol></body></html>" % resp
    print "html:",html
    
    return HttpResponse(html.encode("utf-16"))
