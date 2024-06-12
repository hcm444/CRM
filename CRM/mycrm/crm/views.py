# crm/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Customer, Note
from .forms import CustomerForm, NoteForm

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'crm/customer_list.html', {'customers': customers})

def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm()
    return render(request, 'crm/add_customer.html', {'form': form})

def customer_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    notes = customer.notes.all()
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.customer = customer
            note.save()
            return redirect('customer_detail', pk=customer.pk)
    else:
        form = NoteForm()
    return render(request, 'crm/customer_detail.html', {'customer': customer, 'notes': notes, 'form': form})
