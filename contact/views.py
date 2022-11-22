from django.shortcuts import render
from .forms import ContactForm
from .models import Contact


def contact (request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(454545454)
        form.save()
    email = request.GET.get('email')
    if email:
        Contact.objects.create(email=email)
    context = {
        'form': form
    }
    return render(request, 'contact.html', context)

