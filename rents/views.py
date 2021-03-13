from django.shortcuts import render
from django.shortcuts import render,get_list_or_404,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .forms import RegistrationForm,BookingForm,CommentsForm,UploadrentsForm,RatingForm,LoginForm
from .models import RatingModel,RegistrationModel,UploadrentsModel,BookingModel
from .forms import UploadForm
from .models import ImageModel
from .service import getAllProducts

# Create your views here.

def home(request):
    prdcts = UploadrentsModel.objects.all()
    return render(request,"home.html",{"prdct":prdcts})

def Registration(request):

    status = False
    if request.method == "POST":
        registrationforms = RegistrationForm(request.POST)

        registrationforms.is_valid()
        print("details:", registrationforms)



        registrationmodels = RegistrationModel()
        registrationmodels.fname = registrationforms.cleaned_data["fname"]
        print("name:",registrationmodels.fname)
        registrationmodels.lname = registrationforms.cleaned_data["lname"]
        '''registrationmodels.pathh = registrationforms.cleaned_data["pathh"]'''
        registrationmodels.company = registrationforms.cleaned_data["company"]
        registrationmodels.addres = registrationforms.cleaned_data["addres"]
        registrationmodels.age = registrationforms.cleaned_data["age"]
        registrationmodels.username = registrationforms.cleaned_data["username"]
        print(registrationmodels.username)
        registrationmodels.password = registrationforms.cleaned_data["password"]
        print(registrationmodels.password)
        registrationmodels.gender = registrationforms.cleaned_data["gender"]
        registrationmodels.mail = registrationforms.cleaned_data["mail"]
        registrationmodels.occupation = registrationforms.cleaned_data["occupation"]
        registrationmodels.phone = registrationforms.cleaned_data["phone"]
        registrationmodels.workingarea = registrationforms.cleaned_data["workingarea"]
        print("officelandmark:",registrationmodels.workingarea)
        user = RegistrationModel.objects.filter(username=registrationmodels.username).first()
        print("fields:",user)
        if user is not None:
            status = False
        else:
            try:
                registrationmodels.save()


                status = True
            except:
                status = False
                user = RegistrationModel.objects.all()
                print("user",user)
    if status:
        return render(request,"login.html",locals())
    else:
        response = render(request,"registration.html",{"message":"Registration is failed"})
    return response

def Login(request):
    uname = ""
    upass = ""
    if request.method == "GET":
        lgnfrm = LoginForm(request.GET)

        if lgnfrm.is_valid():
            uname = lgnfrm.cleaned_data["username"]
            upass = lgnfrm.cleaned_data["password"]
            if uname == "admin" and upass == "admin":
                request.session["username"] = "admin"
                request.session["role"] = "admin"
                return render(request,"uploadrents.html")
        user = RegistrationModel.objects.filter(username=uname,password=upass).first()

        if user is not None:
            request.session["username"] = uname
            request.session["role"] = "user"
            prdcts = UploadrentsModel.objects.all()
            return render(request, "home.html", {"prdct": prdcts})
        else:
            response = render(request,"login.html",{"message":"invalid deatails"})
        return response


def logout(request):
    try:
        del request.session["username"]
    except:
        pass
    return render(request,"login.html")


def Uploadrentals(request):
    if request.method == "POST":
        uploadrentform = UploadrentsForm(request.POST,request.FILES)
        uploadrentform.is_valid()
        uploadrentmodels = UploadrentsModel()
        uploadrentmodels.name = uploadrentform.cleaned_data["name"]
        uploadrentmodels.description = uploadrentform.cleaned_data["description"]
        uploadrentmodels.price = uploadrentform.cleaned_data["price"]
        uploadrentmodels.housetype = uploadrentform.cleaned_data["housetype"]
        uploadrentmodels.location = uploadrentform.cleaned_data["location"]
        try:
            uploadrentmodels.save()
            print("upload",uploadrentmodels.name)
            status = True
            user = UploadrentsModel.objects.all()
            if status:
                return render(request,"adminpage.html",{"users":uploadrentmodels})
        except:
            status = False
            upldmdl1 = UploadrentsModel.objects.all()
            print("uploadddd",upldmdl1)
        if status:
            return render(request,"adminpage.html")
        else:
            response = render(request,"uploadrents.html",{"message":"Invalid details"})
        return response

def userpage(request):
    upload = UploadrentsModel.objects.all()
    return render(request,"adminpage.html",{"profile": upload})


def Comments(request):

    if request.method == "POST":
        commentform = CommentsForm(request.POST)

        text = commentform.cleaned_data["text"]
        product_id = request.POST["product"]

        cmntmdl = CommentsModel.objects.filter(text=text,user=request.session[username],product=product_id)

        cmntmdl.save()
        return render(request,"userpage.html")



def Booking(request):
    if request.post == "POST":
        bookingform = BookingForm(request.POST)

        if bookingform.is_valid():

            name = bookingform.cleaned_data["name"]
            cvvno = bookingform.cleaned_data["cvvno"]
            cardno = bookingform.cleaned_data["phone"]
            email = bookingform.cleaned_data["email"]

            bkngmdl = BookingModel.objects.filter(name=name,cvvno=cvvno,cardno=cardno,email=email,user=request.session["username"])
            bkngmdl.save()
            return render(request,"userpage.html")


        response = render(request,"booking.html",{"message":"not booking"})

        return response

def Rating(request):
    if request.method == "POST":
        ratingform = RatingForm(request.POST)

        if ratingform.is_valid():

            rating = ratingform.cleaned_data["rating"]

            rtng = RatingModel.objects.filter(rating=rating,user=request.session['username'])

            return render(request,'userpage.html',{"rating":rtng})

def Profile(request):
    user = RegistrationModel.objects.get(username=navven, password=navven).first()

    if user is not None:
        request.session["username"] = uname
        request.session["role"] = "user"
        user = UploadrentsModel.objects.all()
        return render(request, "home.html", {"user": user})
    else:
        return render(request,'profile.html',{"profile": user})

def Upload(request):
    '''usmldml = UploadrentsModel.objects.all()
    user.pic = str(user.pic).split("/")[1]


    return render(request, 'adminpage.html',{"uploaddata": umldml})'''


# Create your views here.


def UploadImage(request):
    response=""
    uform=UploadForm(request.POST,request.FILES)
    if uform.is_valid():
        umodel=ImageModel()
        umodel.name = uform.cleaned_data['name']
        umodel.price = uform.cleaned_data['price']
        umodel.housetype = uform.cleaned_data['housetype']
        umodel.location = uform.cleaned_data['location']
        umodel.description=uform.cleaned_data['description']
        umodel.myfile=uform.cleaned_data['myfile']
        status=True
        try:
            umodel.save()
            print("details",umodel)
        except:
            status=False
        if status:
            return render(request, "adminpage.html", {"uploaddata": umodel})
        else:
            response = render(request, "uploadfile.html", {"message": "Invalid details"})
    else:
        response=render(request,"pagenotfound.html")
    return response
def viewfiles(request):

    files=[]

    for file in ImageModel.objects.all():

        file.myfile=str(file.myfile).split("/")[1]
        print("photo files:",files)
        print("photos file:",file)

        files.append(file)

    return render(request,"viewfiles.html",{"files":files})


def buyProduct(request):
    product=UploadrentsModel.objects.get(id=request.GET['product'])
    product.path = str(product.path).split("/")[1]
    return render(request, 'buyproduct.html', {'product':product})

def postComment(request):

    form = CommentForm(request.POST)
    print("whers is mistake",form)

    if form.is_valid():

        text = form.cleaned_data['text']
        product_id = request.POST['product']

        new_comment = CommentModel(text=text, user=request.session['username'], product=product_id)
        new_comment.save()

        return render(request, "products.html", {"products":getAllProducts()})
    else:

        return render(request, "login.html", {"products": getAllProducts()})













