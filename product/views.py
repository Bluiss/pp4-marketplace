from django.shortcuts import get_object_or_404
from django.contrib import messages
from .models import Product
from .forms import ProductForm
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages




# View for displaying a paginated list of products
class ProductList(generic.ListView):
    model = Product
    template_name = "product.html"
    paginate_by = 6
    ordering = ['id']


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = self.get_queryset() 
        return context

# View for displaying detailed information about a single product
class ProductListDetail(generic.DetailView):
    model = Product
    template_name = "product_detail.html"
    

# View for creating a new product (requires user authentication)
@login_required
def new(request):
    form = ProductForm(request.POST or None, request.FILES or None)  

    if request.method == "POST" and form.is_valid():
        new_product = form.save(commit=False)
        new_product.seller = request.user
        new_product.save()
        messages.success(request, "Product uploaded")
        return redirect('product:product_detail', pk=new_product.pk)

    return render(request, 'product/new.html', {'form': form})




@login_required
def edit(request, model_id):
    product = Product.objects.get(pk=model_id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid():
        form.save()
        messages.success(request, "Product edited")
        return redirect('product:product_detail', model_id)

    return render(request, 'product/edit.html', {'product': product , 'form': form})


@login_required
def delete(request, model_id):
    product = get_object_or_404(Product, pk=model_id)

    if request.method == 'POST':
        product.delete()
        messages.success(request, "Product deleted")
        return redirect('product:productlist')
    
    return render(request, 'product/delete.html', {'product': product})




