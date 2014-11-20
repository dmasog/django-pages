from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, Template
from shipping.views import pull_usps

ctext = {}
ctext["Page_Title"]="Shipping Page"
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
ctext["ALERT"]=0



# Create your views here.
def home(request,parcel=""):
    LOCATION,STATUS,STATE,ALERT=pull_usps("LN430450976CN")
    ctext["Checkpoints_Completed"]=STATE 
    ctext["ShippingPoints_Location"]=LOCATION
    ctext["ShippingPoints_Status"]=STATUS
    if ALERT != "":
         ctext["ALERT"]=ALERT
    return render(request,"shipment-tracker.html",Context(ctext))
