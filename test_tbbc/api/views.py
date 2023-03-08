from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages
from django.db.models import Q

# Create your views here.


def home(request):
    """View for the main template

    Gets all contacts, and can filter them according to the search
    parameter which can be name or phoneNumber.
    """
    querySet = request.GET.get("search")
    _contacts = Contact.objects.all()

    if querySet:
        _contacts = Contact.objects.filter(
            Q(name__icontains=querySet) | Q(phoneNumber__icontains=querySet)
        ).distinct()
    else:
        messages.success(request, "¡Contacts Listed!")
    return render(request, "manageContact.html", {"contacts": _contacts})


def registerContact(request):
    """View to register a Contact

    Capture the name, phoneNumber, and email, to register/create a contact.
    """
    _name = request.POST["txtName"]
    _phoneNumber = request.POST["txtPhoneNumber"]
    _email = request.POST["txtEmail"]

    Contact.objects.create(name=_name, phoneNumber=_phoneNumber, email=_email)
    messages.success(request, "¡Contact Registered!")
    return redirect("/")


def editingContact(request, id):
    """View redirecting to the template to edit a specific contact"""
    _contact = Contact.objects.get(id=id)
    return render(request, "editContact.html", {"contact": _contact})


def editContact(request):
    """
    View to edit a contact

    Capture and update contact parameters (name, phoneNumber, and email).
    """
    _name = request.POST["txtName"]
    _phoneNumber = request.POST["txtPhoneNumber"]
    _email = request.POST["txtEmail"]
    _id = request.POST["txtId"]

    _contact = Contact.objects.get(id=_id)
    _contact.name = _name
    _contact.phoneNumber = _phoneNumber
    _contact.email = _email
    _contact.save()
    messages.success(request, "¡Contact Updated!")
    return redirect("/")


def deleteContact(request, id):
    """View to delete a contact"""
    _contact = Contact.objects.get(id=id)
    _contact.delete()
    messages.success(request, "¡Contact Deleted!")
    return redirect("/")
