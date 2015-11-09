from django.shortcuts import render
from django.template import Context
from django.shortcuts import render_to_response
from addr_book.models import Book,Author
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def all_book(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("/login/")
    c = Context({"book": Book.objects.filter()})
    c1 = Context({"count":len(Book.objects.filter())})
    return render_to_response("all_book.html", c , c1)
######################################################
def add_author(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("/login/")
    user=request.user.username
    if request.POST:
        post = request.POST
        new_author = Author(
            user = request.user.username,
            Name = post["Name"],
            Age = post["Age"],
            Country = post["Country"])
        new_author.save()
    return render_to_response("add_author.html")
#######################################################  
def add_book(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("/login/")
    user=request.user.username
    if request.POST:
        post = request.POST
        try:
            author = Author.objects.get(Name = post["AuthorName"])
            try:
                BOOK = Book.objects.get(ISBN = post["ISBN"])
                right="The ISBN is exists!"
                return render_to_response("add_book.html",Context({"count":Book.objects.filter().count(),"right":right}))
            except:
                new_book = Book(
                    user = request.user.username,
                    ISBN = post["ISBN"],
                    Title = post["Title"],
                    Author = author,
                    Publisher = post["Publisher"],
                    PublishDate = post["PublishDate"],
                    Price = post["Price"])     
                new_book.save()
        except:
            right="create author first"
            return render_to_response("add_book.html",Context({"count":Book.objects.filter().count(),"right":right}))
    return render_to_response("add_book.html",Context({"count":Book.objects.filter().count()}))
  
def delete(request):
    id = request.GET["id"]
    Book_id = Book.objects.get(id = int(id))
    Book_id.delete()
    return render_to_response("delete.html",id)
    
def update(request):
    id = request.GET["id"]
    book = Book.objects.get(id=int(id))
    if request.POST:
        post = request.POST
        book.ISBN = post["ISBN"]
        book.Title = post["Title"]
        book.Publisher = post["Publisher"]
        book.PublishDate = post["PublishDate"]
        book.Price = post["Price"]
        book.save()
    return render_to_response("update.html",id,Context({"book":book}))

    
def book_detail(request):
    id = request.GET["id"]
    book = Book.objects.get(id=int(id))
    return render_to_response("book_detail.html",id,Context({"book":book}))

def search(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("/login/")
    try:
        author = Author.objects.get(Name = request.GET["Name"])
        c=Context({"book":author.book_set.all(),"count":len(Book.objects.filter())})
        return render_to_response('all_book.html', c)
    except:
        c=Context({"count":len(Book.objects.filter())})
        return render_to_response('all_book.html',c)
def creat_user(request):
    right=""
    if request.POST:       
        username = request.POST["username"]  
        password = request.POST["password"]
        password1 = request.POST["password1"]
        if password == password1:
            try:
                user = User.objects.create_user(username=username,password=password)  
                user.save()
                user = auth.authenticate(username=username, password=password)
                auth.login(request,user)
                return HttpResponseRedirect("/creat_user_ok/")
            except:
                right="This user has existed."
                return render_to_response("creat_user.html",{"right":right})
        else:
            right="Your passwords are different."
            return  render_to_response("creat_user.html",{"right":right})
    return render_to_response('creat_user.html')
def creat_user_ok(request):
    return render_to_response('creat_user_ok.html')
def set_password(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("/login/")
    right=""
    if request.POST:
        password = request.POST["password"]
        password1 = request.POST["password1"]
        if password == password1:
            user = User.objects.get(username=request.user.username)
            user.set_password(password)
            user.save()
            return HttpResponseRedirect("/all_book/")
        else :
            right="Your passwords are different."
            return  render_to_response("creat_user.html",{"right":right})
    return render_to_response("set_password.html")
def login_ok(request):
    if request.POST:
        username = request.POST.get("username", '')
        password = request.POST.get("password", '')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect("/all_book/")
            else:
                return render_to_response('Error.html')
        else:
            return render_to_response('Error.html')
    return render_to_response('login.html')
    
def logout_ok(request):
    logout(request)
    return render_to_response('logout.html')
def wan(request):
    return render_to_response('wan.html')
