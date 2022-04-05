from django.shortcuts import render
from django.http import HttpResponse
from .models import Products
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.

def home_view(request):
    template_name='store/home.html'

    queryset= Products.objects.all()
    queryset.order_by('-id')

    paginator = Paginator(queryset,8)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)

    context={
        'title':'Home',
        'objects':page_obj,
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
    