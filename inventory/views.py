from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from .models import Category

# Create your views here.

def categories (request):
    return render(request, "inventory/categories.html")

def add_categories(request):
    if request.method == "POST":
        name= request.POST.get("name")
        description=request.POST.get("description")
        
        Category.objects.create(name=name, description=description)
        messages.success(request,"Category Added Successfully")
        return redirect('category')
    return render(request, "inventory/add_categories.html")


def view_categories(request):
    categories= Category.objects.all().order_by("name")
    context={"categories": categories}
    return render(request, "inventory/view_categories.html", context)


def update_categories(request, id):
    category = get_object_or_404(Category, id=id)
    if request.method == "POST":
        category.name = request.POST.get("name")
        category.description = request.POST.get("description")
        category.save()
        messages.success(request, "Category updated successfully.")
        return redirect("view_category")
    context = {
        "category": category
    }
    return render(request, "inventory/update_categories.html", context)


def delete_category(request, id):
    category = get_object_or_404(Category, id=id)
    category.delete()
    messages.success(request, "Category deleted successfully.")
    return redirect("view_category")