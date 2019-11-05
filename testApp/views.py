from django.shortcuts import render
import math

# Create your views here.
def home(request):
    return render(request,'testApp/index.html')

def class9(request):
    return render(request,'testApp/class9.html')

def fact9(request):
    value1=0
    value2=0
    d=0

    if request.method=="POST":
        a=int(request.POST['coffofx1'])
        b=int(request.POST['coffofx2'])
        c=int(request.POST['coffofx3'])
        d=b*b-4*a*c
        if d>=0:
            x1=(-b+math.sqrt(d))/(2*a)
            x2=(-b-math.sqrt(d))/(2*a)
            value1=x1
            value2=x2
    return render(request,'testApp/factpol9.html',{'x1':value1,'x2':value2, 'd':d})

def quadrant9(request):
    value=0
    if request.method=="POST":
        a=int(request.POST['coffofx1'])
        b=int(request.POST['coffofx2'])
        if (a>0 and b>0):
            value="point is on first quadrant"
        elif (a<0 and b>0):
            value='point is on second quadrant'
        elif (a<0 and b<0):
            value='point is on third quadrant '
        elif (a>0 and b<0):
            value='point is on fourth quadrant'
        elif (a==0 and b!=0):
            value='point is on y-axis'
        elif (a!=0 and b==0):
            value='point is on x-axis'
        else:
            value='point is origin'
    return render(request,'testApp/quadrant9.html',{'x':value})


def areaOfTraingle9(request):
    value=0
    if request.method=="POST":
        a=int(request.POST['coffofx1'])
        b=int(request.POST['coffofx2'])
        c=int(request.POST['coffofx3'])

        if (a<0 or b<0 or c<0):
            value=-1
        else:
            s=(a+b+c)/2
            value=math.sqrt(s*(s-a)*(s-b)*(s-c))
    return render(request,'testApp/areaOfTraingle.html',{'x':value})

def areaOfTraingleBaseHeight9(request):
    value=0
    if request.method=="POST":
        a=int(request.POST['coffofx1'])
        b=int(request.POST['coffofx2'])
        if (a<0 or b<0):
            value=-1
        else:
            value=.5*a*b
    return render(request,'testApp/areaOfTraingle2.html',{'x':value})


def areaOfQuadrilateral(request):
    value=0
    if request.method=="POST":
        a=int(request.POST['coffofx1'])
        b=int(request.POST['coffofx2'])
        c=int(request.POST['coffofx3'])
        if (a<0 or b<0 or c<0):
            value=-1
        else:
            value=.5*a*(b+c)
    return render(request,'testApp/areaOfQuadrilateral.html',{'x':value})

def areaOfParallelogram(request):
    value=0
    if request.method=="POST":
        a=int(request.POST['coffofx1'])
        b=int(request.POST['coffofx2'])
        if (a<0 or b<0):
            value=-1
        else:
            value=a*b
    return render(request,'testApp/areaOfParallelogram.html',{'x':value})


def areaOfRohumbus(request):
    value=0
    if request.method=="POST":
        a=int(request.POST['coffofx1'])
        b=int(request.POST['coffofx2'])
        if (a<0 or b<0):
            value=-1
        else:
            value=.5*a*b
    return render(request,'testApp/areaOfRohumbus.html',{'x':value})

def volumeOfCuboid(request):
    value=0
    if request.method=="POST":
        a=int(request.POST['coffofx1'])
        b=int(request.POST['coffofx2'])
        c=int(request.POST['coffofx2'])
        if (a<0 or b<0 or c<0):
            value=-1
        else:
            value=a*b*c
    return render(request,'testApp/volumeOfCuboid.html',{'x':value})

def volumeOfCube(request):
    value=0
    if request.method=="POST":
        a=int(request.POST['coffofx1'])
        if (a<0):
            value=-1
        else:
            value=a*a*a
    return render(request,'testApp/volumeOfCube.html',{'x':value})

def volumeOfCylender(request):
    value=0
    if request.method=="POST":
        a=int(request.POST['coffofx1'])
        b=int(request.POST['coffofx2'])
        if (a< 0 or b<0):
            value=-1
        else:
            p=math.pi
            value=p*a*a*b
    return render(request,'testApp/volumeOfCylender.html',{'x':value})

def volumeOfCone(request):
    value=0
    if request.method=="POST":
        a=int(request.POST['coffofx1'])
        b=int(request.POST['coffofx2'])
        if (a< 0 or b<0):
            value=-1
        else:
            p=math.pi
            value=(p*a*a*b)/3
    return render(request,'testApp/volumeOfCone.html',{'x':value})

def volumeOfSphere(request):
    value=0
    if request.method=="POST":
        a=int(request.POST['coffofx1'])
        if (a< 0):
            value=-1
        else:
            p=math.pi
            value=4*(p*a*a*a)/3
    return render(request,'testApp/volumeOfSphere.html',{'x':value})
