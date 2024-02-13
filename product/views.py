from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views import generic

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
    # Instantiate the form
    form = NewProductForm()

    return render(request, 'product/form.html', {'form': form})
