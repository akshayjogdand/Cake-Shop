from django.shortcuts import render,redirect
from AdminApp.models import Category, Product,UserInformation
from UserApp.models import MyCart

# Create your views here.

def homepage(request):
    cats = Category.objects.all()
    cake = Product.objects.all()
    return render (request,'homepage.html',{'cats': cats, 'cakes':cake})

def login(request):
    if(request.method == "GET"):
        cats = Category.objects.all()
        return render(request,'login.html',{'cats':cats})

    else:
        uname = request.POST["uname"]
        pwd = request.POST["pwd"]   
        print(uname)
        print(pwd)    

        try: #he yasathi lihale coz object.get hi mtd jeva userinfo table mdhe uname pwd match zala tr object show krte
            user = UserInformation.objects.get(username=uname,password=pwd) # record match nhi zala tr exception show krte hi mtd
        except:                                            # mhnun except mdhe apan user n pwd match nhi zalyavr punha
            return redirect(login)              #login page disyla pahije

        else:
            request.session["uname"]=uname #login zalyavr session as create krtat n te aplyala nav bar mdhe login
            return redirect(homepage)  # user che name diplay hoyla pahije



def showCakes(request,id):
    id = Category.objects.get(id=id)
    print(id.id)
    cakes = Product.objects.filter(cat = id) #filter mtd jevdhe id match zale tevdhe multiple object dete
    cats = Category.objects.all() #he yasathi ghetl coz apan homepage vr gelo tr category dropdown mdhe category disyla pahije
    return render (request,'homepage.html',{'cakes':cakes,'cats':cats})

def viewDetails(request,id):
    cake = Product.objects.get(id=id)
    cats = Category.objects.all()
    return render(request,'viewDetails.html',{'cake':cake,'cats':cats})

def signUp(request):
    if(request.method == "GET"):
        cats = Category.objects.all()
        return render(request, "signup.html",{'cats':cats})

    else:
        uname = request.POST["uname"]
        pwd = request.POST["pwd"]
        mail = request.POST["mail"]

        user = UserInformation()
        user.username = uname
        user.password = pwd
        user.email = mail 
        user.save()
        return redirect (homepage)

def signOut(request):
    request.session.clear()
    return redirect(homepage)

def addTocart(request):
    if(request.method =="POST"):
        if ("uname" in request.session):
            user = request.session["uname"]
            cakeid = request.POST["cakeid"]
            qty = request.POST["qty"]

            cake = Product.objects.get(id=cakeid)
            user = UserInformation.objects.get(username=user)
            try:
                cart = MyCart.objects.get(user=user, cake=cake)
            
            except:

                cart = MyCart()
                cart.user = user
                cart.cake = cake
                cart.qty = qty
                cart.save()
            else:
                pass
            return redirect(homepage)


        else:
            return redirect(login)

def showAllCartItems(request):
    uname = request.session["uname"]
    user = UserInformation.objects.get(username = uname)
    cats = Category.objects.all()
    if(request.method == "GET"):   
        cart = MyCart.objects.filter(user = user)
        total =0
        for items in cart:
            total += items.qty * items.cake.price
        request.session["total"] = total
        return render(request,'showAllCart.html',{'item':cart,'cats':cats})

    else:
        action = request.POST["action"]
        id = request.POST["cakeid"]
        cake = Product.objects.get(id=id)
        item = MyCart.objects.get(user=user,cake=cake)
        if(action == "remove"):
            item.delete()

        else:
            qty = request.POST["qty"]
            item.qty = qty
            item.save()

        return redirect(showAllCartItems)








