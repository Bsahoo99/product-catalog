from django.shortcuts import render, redirect
from django.views import View
from .models import Thing
from .forms import ProductForm
from django.http import HttpResponse


class Home(View):

    def get(self, request):
        things = Thing.objects.all()
        return render(request, 'home.html', {'things': things})


class Item(View):

    def get(self, request, name):
        thing = Thing.objects.get(name=name)
        return render(request, 'item.html', {'thing': thing})


class NewProduct(View):

    def get(self, request):
        form = ProductForm()
        return render(request, 'new_product.html', {'form': form})

    def post(self, request):
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
        return render(request, 'new_product.html', {'form': form})


class Success(View):

    def get(self, request):
        return render(request, 'success.html')
