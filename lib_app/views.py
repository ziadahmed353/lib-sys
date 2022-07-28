from django.shortcuts import render , redirect, get_object_or_404
from .models import *
from .forms import *
# Create your views here.
def index(request):
    if request.method == 'POST':
        add_book = Book_form(request.POST, request.FILES)
        if add_book.is_valid() :
            add_book.save()
            return redirect('/')
        
        add_cat = Category_form(request.POST)
        if add_cat.is_valid():
            add_cat.save()
            return redirect('/')
        
        
    context = {
        'books':Book.objects.all(),
        'category':Category.objects.all(), 
        'form' : Book_form(),
        'form_cat': Category_form(),
        'books_num':Book.objects.filter(active = True).count(),
        'books_availble':Book.objects.filter(status = 'availble').count(),
        'books_rental':Book.objects.filter(status = 'rental').count(),
        'books_sold':Book.objects.filter(status = 'sold').count(),
    }
    return render(request, 'pages/index.html', context)

def books(request):
    search=Book.objects.all()
    title = None
    if 'search_name' in request.GET:
        title = request.GET['search_name']
        if title:
            search = search.filter(title__icontains = title)
    
    
    if request.method == 'POST':
        add_cat = Category_form(request.POST)
        if add_cat.is_valid():
            add_cat.save()
    context = {
        'books':search,
        'category':Category.objects.all(), 
        'form_cat': Category_form()
    }
    return render(request, 'pages/books.html', context)

def update(request, id):
    book_update = Book.objects.get(id = id)
    if request.method == 'POST':
        book_save = Book_form(request.POST, request.FILES, instance= book_update)
        if book_save.is_valid():
            book_save.save()
            return redirect('/')
    else:
        book_save = Book_form(instance=book_update)
    
    context = {
        'update_form' : book_save
    }
    return render(request, 'pages/update.html',context)

def delete(request, id):
    book_delete = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        book_delete.delete()
        return redirect('/')
    return render(request, 'pages/delete.html')