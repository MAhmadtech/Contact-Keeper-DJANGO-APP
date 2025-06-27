# from django.shortcuts import render
# from .models import Contact
# from contacts.forms import SaveContact
# # Create your views here.

# def index(request):
#     if request.method == 'POST':
#         form = SaveContact(request.POST or None)
#         if form.is_valid():
#             form.save()

#     return render(request, 'index.html')

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from contacts.forms import SaveContact
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    contacts = Contact.objects.all().filter(contact_holder=request.user).order_by('-id')  # Get all contacts, newest first
    
    if request.method == 'POST':
        form = SaveContact(request.POST)
        if form.is_valid():
            # Check if contact with same phone number already exists
            phone = form.cleaned_data.get('phone')
            if Contact.objects.filter(phone=phone).exists():
                messages.error(request, "A contact with this phone number already exists!")
                return render(request, 'index.html', {'contacts': contacts})
            form.save(commit=False).contact_holder = request.user
            form.save()
            messages.success(request, "Contact has been added successfully!")
            return redirect('../contacts')  # Use redirect instead of render
        else:
            messages.error(request, "Please correct the errors below.")
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    
    return render(request, 'index.html', {'contacts': contacts})

@login_required
def delete(request, contact_id):
    contact = Contact.objects.get(pk=contact_id)
    contact.delete()
    messages.success(request, "Contact has been deleted successfully!")
    return redirect('../../contacts/')


@login_required
def edit(request, contact_id):
    contact = Contact.objects.get(pk=contact_id)
    if request.method == 'POST':
        form = SaveContact(request.POST, instance=contact)
        if form.is_valid():
            # Check if phone number is being changed to an existing one
            phone = form.cleaned_data.get('phone')
            if phone != contact.phone and Contact.objects.filter(phone=phone).exists():
                messages.error(request, "A contact with this phone number already exists!")
                return render(request, 'edit.html', {'contact': contact})
            
            form.save()
            messages.success(request, "Contact has been updated successfully!")
            return redirect('../../contacts/')
    else:
        return render(request, 'edit.html', {'contact': contact})


