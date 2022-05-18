from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'home.html',{'name':'Arya'})

def add(request):
    val1 = int(request.GET['a'])
    val2 = int(request.GET['b'])
    val3 = int(request.GET['c'])
    val4 = int(request.GET['d'])
    val5 = float(request.GET['e'])
    val6 = float(request.GET['f'])
    bv = val1 * val3
    bc = val2 * val4
    bw = bv * bc
    ew = (bw/100) * val5
    lh= int(ew/val6)
    lm= ((ew % val6)/val6)*60
    return render(request,'result.html',{'one':bv,'two':bc,'three':bw,'four':ew,'five':lh,'six':lm})