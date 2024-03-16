from django.shortcuts import get_object_or_404
from django.contrib import messages
from .models import Product
from .forms import NewProductForm, EditProductForm
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
        context['products'] = self.get_queryset()  # Pass the queryset of products to the template
        return context

# View for displaying detailed information about a single product
class ProductListDetail(generic.DetailView):
    model = Product
    template_name = "product_detail.html"
    

# View for creating a new product (requires user authentication)
@login_required
def new(request):
    # Instantiate a new product form
    form = NewProductForm()

    # Check if the form has been submitted
    if request.method == "POST":
        # Create a new form instance with the submitted data and files
        newForm = NewProductForm(request.POST, request.FILES)
        
        # Check if the form is valid
        if newForm.is_valid():
            # Create and save a new product with the current user as the seller
            new_product = newForm.save(commit=False)
            new_product.seller = request.user
            new_product.save()

            # Display a success message and redirect to the new product's detail page
            messages.success(request, "Product uploaded")
            return redirect('product:product_detail', pk=new_product.pk)

    # Render the form template with the instantiated form
    return render(request, 'product/form.html', {'form': form})



@login_required
def edit(request, model_id):  # Add model_id as a parameter
    model_instance = Product.objects.get(pk=model_id)

    if request.method == "POST":
        editForm = EditProductForm(request.POST, instance=model_instance)  # Correct typo in variable name

        if editForm.is_valid():
            editForm.save()  # Call editForm.save() to save the form data
            # Display a success message and redirect to the edited product's detail page
            messages.success(request, "Product updated")
            return redirect('product:product_detail', pk=model_instance.pk)  # Use model_instance instead of new_product

    else:
        editForm = EditProductForm(instance=model_instance)  # Use instance=model_instance

    return render(request, 'product/edit_form.html', {'form': editForm})  # Use editForm instead of form

@login_required
def delete(request , model_id):
    product = get_object_or_404(Product, pk=model_id)

    if request.method == "POST":
        product.delete()
        messages.success(request, "Product deleted")
        return redirect('product:productlist')
    return render(request, 'product.html', {'product': product})