from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Products,Order
from .forms import OrderForm
from django.core.paginator import Paginator
from django.db.models import Q
from django.core.mail import send_mail,EmailMessage
#to send mail
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# Create your views here.

def send_mail(subject,attachement):
    server='smtp.gmail.com'
    port=587
    #Setup MIME
    message=MIMEMultipart()
    message['From']='email00@gmail.com'
    message['To']='email00@gmail.com'
    message['Subject']=subject
    message.attach(MIMEText(attachement,'plain'))
    
    #Create SMTP session and send the mail
    session=smtplib.SMTP(server,port)
    session = smtplib.SMTP(server,port)
    session.starttls()  #enable security
    session.login('email@gmail.com','password.com')
    msg_str=message.as_string()
    session.sendmail('sender','sender',msg_str)
    session.quit()

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
            queryset=Products.objects.filter(
                Q(name__icontains=query)
            )
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
    message=""
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
        
        subject="Order From : "+order.customer_name
        message+="Order Id : "+str(order.id)
        message=" Phone : "+order.customer_phone
        message+="\n Address : "+order.address
        message+="\n Products Name : "+Products.objects.get(id=id).name
        message+="\nPrice : "+str(obj.price)
        send_mail(subject, message)
        messages.success(request, 'Contact request submitted successfully.')
        return redirect('/')
    else:
        messages.error(request, 'Invalid form submission.')

    context={
        'title':Order,
        'object':obj,
        'form':form,
    }

    return render(request,'store/create-order.html',context)

def computers_view(request):

    template_name='store/home.html'
    queryset=Products.objects.filter(
        Q(category__name__contains='Laptop') | Q(category__name__contains='Desktop')
    )

    paginator=Paginator(queryset,8)
    page_number=request.GET.get('page')
    queryset=paginator.get_page(page_number)

    context={
        'title':'Computer',
        'objects':queryset,
    }

    return render(request,template_name,context=context)

def phones_view(request):

    template_name='store/home.html'
    queryset=Products.objects.filter(
        Q(category__name__icontains='Phone') | Q(category__name__icontains='Cellphone')|
        Q(category__name__icontains='Smartphone')
    )

    paginator=Paginator(queryset,8)
    page_number=request.GET.get('page')
    queryset=paginator.get_page(page_number)

    context={
        'title':'Phones',
        'objects':queryset,
    }

    return render(request,template_name,context=context)


def others_view(request):

    template_name='store/home.html'
    excludes=['Phone','Cellphone','Laptop','Desktop']

    queryset=Products.objects.exclude(category__name__in=excludes)

    paginator=Paginator(queryset,8)
    page_number=request.GET.get('page')
    queryset=paginator.get_page(page_number)

    context={
        'title':'Other',
        'objects':queryset,
    }

    return render(request,template_name,context=context)

def about_view(request):
    template_name='about.html'
    context={
        'title':'About Us',
    }
    return render(request,template_name,context=context)


def contact_view(request):
    template_name='contact.html'
    context={
        'title':'Contact',
    }
    return render(request,template_name,context=context)
