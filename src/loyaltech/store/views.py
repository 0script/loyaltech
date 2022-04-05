from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import Products,Order
from .forms import OrderForm
from django.core.paginator import Paginator
from django.db.models import Q
from django.core.mail import send_mail,EmailMessage

# Create your views here.

def home_view(request):
    template_name='store/home.html'

    queryset=Products.objects.all()
    paginator=Paginator(queryset,8)
    page_number=request.GET.get('page')
    queryset=paginator.get_page(page_number)

    context={
        'title':'Home',
        'objects':queryset,
    }

    return render(request,template_name,context=context)

def search_view(request):
    'minimalist search functionality'
    template_name='store/home.html'

    if request.method=='GET':
        query=request.GET.get('q')
        
        if query is not None:
            print(query)
            queryset=Products.objects.filter(
                Q(name__icontains=query)
            )    
            print(queryset)
            paginator = Paginator(queryset,8)
            page_number=request.GET.get('page')
            queryset=paginator.get_page(page_number)
            
            context={
                'title':'Home',
                'objects': queryset,
            }
    
            return render(request,'store/home.html',context=context)
    return HttpResponse("Bad Query '_' ")

def product_detail_view(request,id):
    template_name='store/product-detail.html'

    object=get_object_or_404(Products,id=id)
    context={
        'title':'Detail',
        'object':object,
    }

    return render(request,template_name,context)

def create_order_view(request,id):

    obj=get_object_or_404(Products,id=id)
    form=OrderForm(request.POST or None)
    order=None
    if form.is_valid():
        #saving the form
        order=Order.objects.create(
            product=Products.objects.get(id=id),
            customer_name=form.cleaned_data['customer_name'],
            customer_phone=form.cleaned_data['customer_phone'],
            price=obj.price,
            address=form.cleaned_data['customer_addr'],
        )

        order.save()
        #include function to send notification
        print('sending mail')
        subject="Order From : "+order.customer_name
        message=" Phone : "+order.customer_name
        message+="\n Address : "+order.address
        message+="\n Products Name : "+Products.objects.get(id=id).name
        email = EmailMessage(subject, message, to=['zokme00@gmail.com'])
        email.send()
        #send_mail(subject, message,'zokme00@gmail.com', ('zokme00@gmail.com',))
        print('mail sent')

    context={
        'title':order,
        'object':obj,
        'form':form,
    }

    return render(request,'store/create-order.html',context)
