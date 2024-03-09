from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "index.html"


class AboutPageView(TemplateView): 
    template_name = "about.html"

class ContactPage(TemplateView): 
    template_name = "contact_us.html"