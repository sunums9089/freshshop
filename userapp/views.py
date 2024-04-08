from django.shortcuts import render
from adminapp.models import *
from.models import *
from django.shortcuts import redirect
# Create your views here.
def userindex(request):
    data=Products.objects.all()
    data1=Products.objects.all()
    u=request.session.get('u_id')
    data3=Mycart.objects.filter(userid=u,status=0).count()
    data4=Mycart.objects.filter(userid=u,status=0)
    print(data3)
    return render(request,'userindex.html',{'data':data, 'data1':data1,'data3':data3,'data4':data4})

def sidebar(request):
    data=Products.objects.all()
    return render(request,'sidebar.html',{'data':data})

def details(request,id):
    data=Products.objects.filter(id=id)
    return render(request,'details.html',{'data':data})

# def wishlist(request):
#     return render(request,'wishlist.html')

def home(request):
    return render(request,'home.html')

def checkout(request):
    u=request.session.get('u_id')
    data=Mycart.objects.filter(userid=u,status=0)
    return render(request,'checkout.html',{'data':data})

def aboutus(request):
    return render(request,'aboutus.html')

def cart(request):
    u=request.session.get('u_id')
    data=Mycart.objects.filter(userid=u,status=0)
    return render(request,'cart.html',{'data':data})

def contactus(request):
    if request.method=='POST':
        your_name=request.POST['your_name']
        your_email=request.POST['your_email']
        subject=request.POST['subject']
        your_message=request.POST['your_message']
        data=Info(your_name=your_name,
                  your_email=your_email,
                  subject=subject,
                  your_message=your_message)
        data.save()
    return render(request,'contactus.html')

def gallery(request):
    u=request.session.get('u_id')
    data=Checkout.objects.filter(userid=u)
    return render(request,'gallery.html',{'data':data})

def register(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        contact=request.POST['contact']
        data=Registeration(name=name,
                           email=email,
                           password=password,
                           contact=contact)
        data.save()
    return render(request,'register.html')

def sighn(request):
    return render(request,'sighn.html')



def publicdata(request):
    if request.method == "POST":
        name=request.POST.get('name')
        password=request.POST.get('password')
        if Registeration.objects.filter(name=name,password=password).exists():
           data = Registeration.objects.filter(name=name,password=password).values('id','email','contact').first()
           request.session['u_id'] = data['id']
           request.session['contact_u'] = data['contact'] 
           request.session['email_u'] = data['email'] 
           request.session['name_u'] = name
           request.session['password_u'] = password
           return redirect('userindex') 
        else:
            return render(request,'sighn.html',{'msg':'invalid user credentials'})
    else:
        return redirect('sighn')

def userlogout(request):
    del request.session['name_u']
    del request.session['u_id']
    del request.session['contact_u']
    del request.session['email_u']
    del request.session['password_u']
    return redirect('sighn')

def cartdata(request,id):
    if request.method=="POST":
        userid=request.session.get('u_id')
        quantity=request.POST['Quantity']
        total=request.POST['total']
        data=Mycart(userid=Registeration.objects.get(id=userid),
                    productid=Products.objects.get(id=id),
                    quantity=quantity,
                    total=total)
        data.save()
    return redirect('cart')

def cart_delete(request,id):
    Mycart.objects.filter(id=id).delete()
    return redirect('cart')


def checkoutdata(request):
    if request.method=="POST":
        userid=request.session.get('u_id')
        address=request.POST['address']
        country=request.POST['country']
        state=request.POST['state']
        zip1=request.POST['zip1']
        order=Mycart.objects.filter(userid=userid,status=0)

        for i in order:
            data=Checkout(userid=Registeration.objects.get(id=userid),
                          cartid=Mycart.objects.get(id=i.id),
                          address=address,
                          country=country,
                          state=state,
                          zip1=zip1)
            data.save()
            Mycart.objects.filter(id=i.id).update(status=1)
    return redirect('thanks')


def thanks(request):
    u=request.session.get('u_id')
    data=Checkout.objects.filter(userid=u)
    return render(request,'thanks.html',{'data':data})

def tnk(request):
    return redirect('userindex')