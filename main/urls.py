from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('',views.index, name='index'),
    path('Contact',views.contact,name='contact'),
    path('Plitki',views.plitki,name='plitki'),
    path('Gallery',views.gallery,name='gallery'),
    path('Laminat',views.laminat,name='laminat'),
    path('cart-create/',views.cart_create,name='cart_create'),
    path('cart-update/',views.cart_update,name='cart_update'),
    path('cart-delete/',views.cart_delete,name='cart_delete'),
]