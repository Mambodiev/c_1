
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core import paginator
from django.http.response import HttpResponse
from django.core.paginator import Paginator, EmptyPage,  PageNotAnInteger
from django.core.mail import send_mail
from django.shortcuts import reverse, render
from django.views import generic
from .forms import ContactForm
from .models import Carousel, About, Faq, Shipping_returns, Terms_of_use
from cart.models import Order, Product
from django.http import HttpResponse, request





class ProfileView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context.update({
            "orders": Order.objects.filter(user=self.request.user, ordered=True)
        })
        return context


def home(request):

    product = Product.objects.all()
    carousel = Carousel.objects.all()

    paginator = Paginator(product, per_page=4)
    page_number = request.GET.get('page',1)
    page_obj = paginator.get_page(page_number)

    context={
        'page':'page',
        'product':page_obj.object_list,
        'carousel':carousel,
        'paginator':paginator,
        'page_number':int(page_number),
    }

    return render(request, 'home.html',context)


def about(request):
    about = About.objects.all()
    context={
        'about':about,
    }

    return render(request, 'about.html',context)


def faq(request):
    faq = Faq.objects.all()
    context={
        'faq':faq,
    }
    return render(request, 'faq.html', context)


def terms_of_use(request): 
    terms_of_use = Terms_of_use.objects.all()
    context={
        'terms_of_use':terms_of_use,
    } 
    return render(request, 'terms_of_use.html', context)


def shipping_returns(request): 
    shipping_returns = Shipping_returns.objects.all()
    context={
        'shipping_returns':shipping_returns,
    } 
    return render(request, 'shipping_returns.html', context)


class ContactView(generic.FormView):
    form_class = ContactForm
    template_name = 'contact.html'

    def get_success_url(self):
        return reverse("contact")

    def form_valid(self, form):
        messages.info(
            self.request, "Thanks for getting in touch. We have received your message.")
        name = form.cleaned_data.get('name')
        email = form.cleaned_data.get('email')
        message = form.cleaned_data.get('message')

        full_message = f"""
            Received message below from {name}, {email}
            ________________________


            {message}
            """
        send_mail(
            subject="Received contact form submission",
            message=full_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.NOTIFY_EMAIL]
        )
        return super(ContactView, self).form_valid(form)
