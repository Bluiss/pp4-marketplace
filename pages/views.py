from django.views.generic import TemplateView, DetailView
from django.views import generic
from product.models import Product


class HomePageView(TemplateView):
    template_name = "index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()  
        return context


class AboutPageView(TemplateView): 
    template_name = "about.html"
    


class ContactPage(TemplateView): 
    template_name = "contact_us.html"