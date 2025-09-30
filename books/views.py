from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BookForm

# CREATE
def book_create(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm()
    return render(request, "library/book_form.html", {"form": form})

# READ (список книг)
def book_list(request):
    books = Book.objects.all()
    return render(request, "library/books_list.html", {"books": books})

# READ (деталі однієї книги)
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, "library/book_detail.html", {"book": book})

# UPDATE
def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm(instance=book)
    return render(request, "library/book_form.html", {"form": form})

# DELETE
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect("book_list")
    return render(request, "library/book_confirm_delete.html", {"book": book})


