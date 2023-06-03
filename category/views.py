from django.shortcuts import render, get_object_or_404, redirect
from .models import Category
from .forms import CategoryForm

def category_list(request):
    category_list = Category.objects.all()
    return render(request, 'category/category_list.html', {'category_list': category_list})

def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    return render(request, 'category/category_detail.html', {'category': category})

def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category:category_list')
    else:
        form = CategoryForm()
    return render(request, 'category/category_create.html', {'form': form})

def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category:category_detail', pk=category.pk)
    else:
        form= CategoryForm(instance=category)
    return render(request, 'category/category_update.html', {'form': form})

def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
      category.delete()
      return redirect('category:category_list')
    return render(request, 'category/category_delete.html', {'category': category})