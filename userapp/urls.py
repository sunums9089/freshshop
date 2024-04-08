from django.urls import path
from.import views

urlpatterns = [
    path('userindex',views.userindex,name='userindex'),
    path('sidebar',views.sidebar,name='sidebar'),
    path('details/<int:id>',views.details,name='details'),
    # path('wishlist',views.wishlist,name='wishlist'),
    path('home',views.home,name='home'),
    path('checkout',views.checkout,name='checkout'),
    path('aboutus',views.aboutus,name='aboutus'),
    path('cart',views.cart,name='cart'),
    path('contactus',views.contactus,name='contactus'),
    path('gallery',views.gallery,name='gallery'),
    path('register',views.register,name='register'),
    path('sighn',views.sighn,name='sighn'),
    path('publicdata',views.publicdata,name='publicdata'),
    path('userlogout',views.userlogout,name='userlogout'),
    path('cartdata/<int:id>',views.cartdata,name='cartdata'),
    path('cart_delete/<int:id>',views.cart_delete,name='cart_delete'),
    path('checkoutdata',views.checkoutdata,name='checkoutdata'),
    path('thanks',views.thanks,name='thanks'),
    path('tnk',views.tnk,name='tnk')

]