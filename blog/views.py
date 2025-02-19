from django.shortcuts import render
from blog.models import Header, Blog, About, Contact, ContactMessage

# Create your views here.
def home_page(request):
    context = {}
    context["header"] = Header.objects.last()
    context["blogs"] = Blog.objects.filter(status="publish").order_by("-publish_date")
    return render(request, "home/index.html", context)

def blog_detail(request, id):
    context = {}
    context['blog'] = Blog.objects.get(id=id)
    return render(request, "detail.html", context)

def about_view(request):
    context = {}
    context["about"] = About.objects.last()
    return render(request, "about.html", context)

def contact_view(request):
    context = {}
    context["contact"] = Contact.objects.last()
    if request.method == 'POST':
        ContactMessage.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
            message=request.POST.get('message'),
        )
        context["message"] = "Teklifiniz/Shikayetiniz ugurla qeyde alindi"
    return render(request, "contact.html", context)