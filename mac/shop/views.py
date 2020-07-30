from django.shortcuts import render
from django.http import HttpResponse
from .models import product, Contact,Orders,OrderUpdate
from math import  ceil
import json

# Create your views here.
def index(request):
    allProds=[]
    catprods=product.objects.values('chatagory','id')
    cats={item['chatagory'] for item in catprods}
    for cat in cats:
        prod=product.objects.filter(chatagory=cat)
        n=len(prod)
        nSlides= n//4 + ceil((n/4)-(n//4))
        allProds.append([prod,range(1,nSlides),nSlides])
    params = {'allProds':allProds}
    return render(request,'shop/index.html',params)

def searchMatch(query,item):
    if query in item.product_name.lower() or query in item.desc.lower() or query in item.chatagory.lower() or query in item.subchatagory.lower():
        return True
    else:
        return False
def search(request):
    query=request.GET.get('search','')
    print(query)
    allProds=[]
    catprods=product.objects.values('chatagory','id')
    cats={item['chatagory'] for item in catprods}
    for cat in cats:
        prodtemp=product.objects.filter(chatagory=cat)
        prod=[item for item in prodtemp if searchMatch(query,item)]

        n=len(prod)
        nSlides= n//4 + ceil((n/4)-(n//4))
        if len(prod) != 0:
            allProds.append([prod,range(1,nSlides),nSlides])
    params = {'allProds':allProds,'msg':''}
    if len(allProds) ==0 or len(query)<4:
        params={'msg':'Please make sure to search for a valid item name or catagory'}
    return render(request,'shop/search.html',params)


def about(request):
    return render(request,'shop/about.html')
def contact(request):
    if request.method=="POST":
        
        print(request)
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        desc=request.POST.get('desc','')
        print(name,email,phone,desc)
        contact=Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()
        
        thanku=True
        return render(request,'shop/contact.html',{'thanku':thanku})
        
    return render(request,'shop/contact.html')
def tracker(request):
    if request.method=="POST":
        order_id=request.POST.get('order_id','')
        email=request.POST.get('email','')
        try:
            order=Orders.objects.filter(order_id=order_id,email=email)
            if len(order)>0:
                update=OrderUpdate.objects.filter(order_id=order_id)
                updates=[]
                for items in update:
                    updates.append({'text':items.update_desc,'time':items.timestamp})
                    response= json.dumps({'status':'success','updates':updates,'itemsjson':order[0].item_json},default=str)
                return HttpResponse(response)

            else:
                return HttpResponse('{"status":"noitem"}')
        except Exception as e:
            return HttpResponse('{{"status":"error"}}')

    return render(request,'shop/tracker.html')


def productview(request,id):
    #fetch product using id
    products=product.objects.filter(id=id)
    print(products)
    return render(request,'shop/productview.html',{'myproducts':products[0]})
def checkout(request):
    if request.method=="POST":
        item_json=request.POST.get('itemsJson','')
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        amount=request.POST.get('amount','')
        address=request.POST.get('address','')+""+request.POST.get('address2','')
        phone=request.POST.get('phone','')
        country=request.POST.get('country','')
        state=request.POST.get('state','')
        zip_code=request.POST.get('zip_code','')
        
        print(name,email,phone,address,state,country,zip_code)
        Order=Orders(item_json=item_json,name=name,email=email,amount=amount,phone=phone,address=address,country=country,state=state,zip_code=zip_code)
        Order.save()
        update=OrderUpdate(order_id=Order.order_id,update_desc="Your order has been placed")
        update.save()
        thank=True
        id=Order.order_id
        return render(request,'shop/checkout.html',{'thank':thank,'id':id})
    return render(request,'shop/checkout.html')
def success(request):
    return render(request,'shop/success.html')