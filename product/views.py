from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views import generic
from django.contrib import messages


from .models import Product
from .forms import NewProductForm

class ProductList(generic.ListView):
    model = Product
    template_name = "product.html"
    paginate_by = 6

class ProductListDetail(generic.DetailView):
    model = Product
    template_name = "product_detail.html"

@login_required
def new(request):
    form = NewProductForm()

    if request.method == "POST":
        newForm = NewProductForm(request.POST, request.FILES)  
        if newForm.is_valid():
            new_product = newForm.save(commit=False)
            new_product.seller = request.user
            new_product.save()

            messages.success(request, "Product uploaded")
            return redirect('product:product_detail', pk=new_product.pk)

    return render(request, 'product/form.html', {'form': form})