from django.shortcuts import render
from.models import *
from django.shortcuts import redirect
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from userapp.models import *
# Create your views here.
def index(request):
    table=Products.objects.all().count()
    usertable=Info.objects.all().count()
    reg_table=Registeration.objects.all().count()
    check_table=Checkout.objects.all().count()
    return render(request,'index.html',{'table':table,'usertable':usertable,'reg_table':reg_table,'check_table':check_table})

def form(request):
    if request.method=='POST':
        product_name=request.POST['product_name']
        product_price=request.POST['product_price']
        product_image=request.FILES['product_image']
        data=Products(product_name=product_name,
                   product_price=product_price,
                   product_image=product_image)
        data.save()
    return render(request,'form.html')

def table(request):
    data=Products.objects.all()
    return render(request,'table.html',{'data':data})

def edit(request,id):
    data=Products.objects.filter(id=id)
    return render(request,'edit.html',{'data':data})

def update(request,id):
    if request.method=='POST':
        product_name=request.POST['product_name']
        product_price=request.POST['product_price']
        product_image=request.FILES['product_image']
        try:
            img_c=request.FILES['product_image']
            fs=FileSystemStorage()
            file=fs.save(img_c.name,img_c)
        except MultiValueDictKeyError:
            file=Products.objects.get(id=id).product_image

        data=Products.objects.filter(id=id).update(product_name=product_name,
                   product_price=product_price,
                   product_image=product_image)    
    return redirect('table')

def delete(request,id):
    Products.objects.filter(id=id).delete()
    return redirect('table')

def usertable(request):
    data=Info.objects.all()
    return render(request,'usertable.html',{'data':data})


def reg_table(request):
    data=Registeration.objects.all()
    return render(request,'reg_table.html',{'data':data})

def check_table(request):
    data=Checkout.objects.all()
    return render(request,'check_table.html',{'data':data})

def adminhome(request):
    table=Products.objects.all().count()
    usertable=Info.objects.all().count()
    reg_table=Registeration.objects.all().count()
    check_table=Checkout.objects.all().count()
    return render(request,'adminhome.html',{'table':table,'usertable':usertable,'reg_table':reg_table,'check_table':check_table})
