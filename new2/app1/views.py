from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from app1.models import *
from app1.form import *
import json

# Create your views here.

def firstpage(request):
    cat = Category.objects.all()
    trend = Product.objects.filter(Trending = 'Yes')
    if(request.session.has_key('user_id')):
        userid = request.session['user_id']
        userid1 = "Log out"      
    else:
        userid1 = "Login"
        userid = " User   "
    return render(request, 'index.html', {'cat':cat, 'userid1':userid1, 'userid':userid, 'trend':trend})

def deletesession(request):
    if(request.session.has_key('user_id')):
        del request.session['user_id']
        return HttpResponseRedirect('/first/')
    else:
        return HttpResponseRedirect('/login/')


def scndpage(request,category_id): 
    obj = Product.objects.filter(category_id = category_id)
    return render(request, 'men.html', {'men':obj})

def thirdpage(request,id): 
    id = id
    men2 = Product.objects.filter(id = id)
    name = men2[0].name
    size = men2[0].size
    price = men2[0].price

   

    request.session['pname'] = name     
    request.session['psize'] = size
    request.session['pprice'] = price
    request.session['pid'] = id
    if(request.session.has_key('user_id')):
        uname0 = request.session['user_id']
    
        data = cart.objects.filter(name=name, full_name=uname0)
        if (data):
            cart1 = "Go To Cart"
        else:
            cart1 = "Add To Cart"
    else:
        cart1 = "Add To Cart"
    return render(request, 'men2.html', {'men2':men2, 'cart1':cart1})

def cart1(request):
    if(request.session.has_key('user_id')):
        uname0 = request.session['user_id']
        if(request.session.has_key('pname')):
            name0 = request.session['pname']
        if(request.session.has_key('psize')):
            size0 = request.session['psize']
        if(request.session.has_key('pprice')):
            price0 = request.session['pprice']
        if(request.session.has_key('pid')):
            pid = request.session['pid']
            data = cart.objects.filter(name=name0, full_name=uname0)
            if (data):
                obj1 = cart.objects.filter(full_name=uname0)
            else:
                obj = cart.objects.create(name=name0, size=size0, pid=pid, full_name=uname0, price=price0, price2=price0, quantity=1)
                obj.save()
        obj1 = cart.objects.filter(full_name=uname0)
        
        price11=0     #fortotalprice
        for obj in obj1:
            price11 += obj.price2      

        request.session['price11'] = price11
        if(request.session.has_key('pname')):
            del request.session['pname']
        if(request.session.has_key('psize')):
            del request.session['psize']
        if(request.session.has_key('pprice')):
            del request.session['pprice']
        if(request.session.has_key('pid')):
            del request.session['pid']
         
        return render(request, 'cart.html', {'obj1':obj1, 'uname0':uname0, 'tprice':price11})        
    else:
        return HttpResponseRedirect('/login/')
    
def cartrem(request):
    id = request.POST['objname']
    quant = cart.objects.filter(id = id)
    oldquantity = quant[0].quantity
    price1 = quant[0].price
    price2 = quant[0].price2
    btn = request.POST['btn']
    if(btn=="remove"):
        cart.objects.filter(pk=id).delete()
        return HttpResponseRedirect('/cart/')
    if(btn=="-"):
        if(oldquantity>0):
            cart.objects.filter(pk=id).update(quantity=(oldquantity-1),price2=(price2-price1))
            return HttpResponseRedirect('/cart/')
    if(btn=="+"):
        cart.objects.filter(pk=id).update(quantity=(oldquantity+1),price2=(price2+price1))
        return HttpResponseRedirect('/cart/')
    else:
        return HttpResponseRedirect('/cart/')       
    return HttpResponseRedirect('/cart/')


def orderdone(request):   
    if(request.method=="POST"):  
        add = request.POST['address']        
        mob = request.POST['mobile']        
        if(request.session.has_key('user_id')):
            name0 = request.session['user_id']
        if(request.session.has_key('price11')):
            price11 = request.session['price11']
        obj1 = cart.objects.filter(full_name=name0)
        for obj in obj1:
            name1 = obj.name
            size1 = obj.size
            uname1 = obj.full_name
            price1 = obj.price
            price2 = obj.price2
            quantity1= obj.quantity
            pid1 = obj.pid
            obj3 = order.objects.create(name=name1, pid=pid1, size=size1, full_name=uname1, price=price1,price2=price2, quantity=quantity1, address=add, mobile_no=mob)
            obj3.save()

        obj2 = cart.objects.filter(full_name=name0)
        obj2.delete()
        return HttpResponse("Your Order is done Buddy Chill")
    else:
        if(request.session.has_key('user_id')):
            name0 = request.session['user_id']
        if(request.session.has_key('price11')):
            price11 = request.session['price11']
        return render(request, 'order1.html', {'tprice':price11, 'uname':name0})

def ordershow(request):
    if(request.session.has_key('user_id')):
        name0 = request.session['user_id']
        obj4 = order.objects.filter(full_name=name0)
        return render(request, 'ordershow.html', {'data':obj4, 'uname0':name0})
    else:
        return HttpResponseRedirect('/login/')



def signup1(request):
    s = signupform(request.POST)
    if request.method == "POST":
        s = signupform(request.POST)
        s.save()
        return HttpResponse("saved")
    else:
        return render(request, 'signup.html', {'form':s})

def login1(request):
    l = loginform(request.POST)
    if request.method == "POST":
        q = request.POST['email_id']
        p = request.POST['password']
        all_objects = signup.objects.filter(email_id=q,password=p)
        if(all_objects):
            aa = all_objects[0].full_name
            request.session['user_id'] = aa
            
            return HttpResponseRedirect('/first/')
        else:
            return HttpResponse("uid or pwd is wrong") 
    else:
        return render(request, 'login.html', {'form':l})

def search1(request):
    a = request.POST.get('search')
    print(a)
    men = Product.objects.filter(name__contains=a)
    return render(request, 'men.html', {'men':men})


    #image = men2[0].image
    #image1 = json.dumps(str(image)) #this is for serialization
    #request.session['pimage'] = image1 
    #next = request.POST.get('next', '/')
    #return HttpResponseRedirect(next)
    #return HttpResponseRedirect(request.META.get('HTTP_REFERER'))