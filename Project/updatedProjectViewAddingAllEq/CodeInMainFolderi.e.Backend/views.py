from django.shortcuts import render
from django.http import HttpResponse
import math



def home(request):
    return render(request,'home.html')

def add(request):
    val1 = int(request.POST['a'])
    val2 = int(request.POST['b'])
    val3 = int(request.POST['c'])
    val4 = int(request.POST['d'])
    val5 = float(request.POST['e'])
    val6 = float(request.POST['f'])
    bv = val1 * val3
    bc = val2 * val4
    bw = bv * bc
    ew = (bw/100) * val5
    lh= int(ew/val6)
    lm= ((ew % val6)/val6)*60

    #Program For Rolling Resistance:
    urr = float(request.POST['g'])
    m = float(request.POST['h'])
    x = int(request.POST['i'])
    g = 9.8

    x1 = math.radians(x)
    x2 = math.cos(x1)

    Frr= urr * m * g * x2


    #Program for Calculating Aerodynamic Drag:

    p=1.204
    Cd = float(request.POST['j'])
    Vx = float(request.POST['k'])
    V= (Vx *1000)/3600
    Vxair= float(request.POST['l'])
    Vair = (Vxair * 1000) / 3600
    A= float(request.POST['m'])
    Fad= (1/2) * p * Cd *A * (V + Vair)  * (V + Vair)

    # Program for Calculating Gradient Force:
    x2 = math.sin(x1)
    Fg = m * g * x2

    #Program for Calculating Tractive Efforts:
    Fte= Frr + Fad + Fg

    #Program for Calculating Vehicle Range on Plane Road:
    Ex=float(request.POST['n'])
    E= Ex * 3600
    power= Fte * V
    dist= (E/power) * V
    dk = dist/1000


    #Program for Calculating Vehicle Motor Specifications:
    r = float(request.POST['o'])
    G= float(request.POST['p'])
    Ng=float(request.POST['q'])
    Tw = Fte * r

    Ww = V/r
    Tm = Tw/( G * Ng)
    Wm = Ww * G




    return render(request,'result.html',{'one':bv,'two':bc,'three':bw,'four':ew,'five':lh,'six':lm,'seven':Frr,'eight':Fad,'nine':Fg,'ten':Fte,'eleven':x,'twelve':E,'thirteen':dist,'fourteen':dk,'fifteen':Tm,'sixteen':Wm,'seventeen':power})