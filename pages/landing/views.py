from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, Template

# Create your views here.
ctext = {}
ctext["Carrier"]="USPS"
ctext["Address"]="7321 Sweet Bay LN<br>Raleigh NC 27615"
ctext["Order_Number"]="05-00032"
ctext["TrackingNo"]="LN430450976CN"
ctext["Company_Address"]="7321 Sweet Bay LN<br>Raleigh NC 27615"
ctext["Company_Email"]="dave@masog.com"
ctext["Company_Phone"]="919 289 9253"
ctext["Checkpoints_Completed"]=3
ctext["Checkpoints"]=["First","Second","Third","Fourth","Fifth"]
ctext["Chkpts"]=[1,2,3,4,5]
ctext["ShippingPoints_Location"]=["January 23, 2014, 11:03 am, Alexandria VA US","January 24, 2014, 10:12 am, Alexandria VA US","January 25, 2014, 03:20 pm, Alexandria VA US","January 26, 2014, 05:15 pm, Alexandria VA US","January 27, 2014, 09:10 am, Alexandria VA US","January 28, 2014, 11:03 am, Alexandria VA US","January 29, 2014, 10:12 am, Alexandria VA US","January 30, 2014, 05:15 pm, Alexandria VA US"]
ctext["ShippingPoints_Status"]=["Shipped","Out for delivery","Package arrived at a carrier facility","Package arrived at a carrier facility","Package arrived at a carrier facility","Package arrived at a carrier facility","Package arrived at a carrier facility","Package arrived at a carrier facility"]

def home(request):
    return render(request,"landing.html",Context(ctext))
