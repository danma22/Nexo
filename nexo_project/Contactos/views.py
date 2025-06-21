from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from django.views.decorators.http import require_POST
from .models import Contact, Group, Domicile, PhoneNumber
from .forms import ContactForm, DomicileForm, PhoneNumberForm
from .filters import ContactFilter

#cbv
##fbv

# CONTACTO

def contactos(request):
    contactsFiltered = ContactFilter(request.GET, queryset=Contact.objects.all().order_by('name', 'last_name_p', 'last_name_m'))
    groups = Group.objects.all().order_by('name')

    context = {
        'active_page' : 'contactos',
        'contactsFiltered' : contactsFiltered,
        'groups' : groups
    }
    return render(request, 'contactos/contactos.html', context)

def show_contact(request, pk):
    contact = get_object_or_404(Contact, contact_id=pk)
    domicile_form = DomicileForm(prefix='domicile')
    phone_form = PhoneNumberForm(prefix='phone')

    if request.method == 'POST':
        form_id = request.POST['form_id']
        if form_id == 'domicile':
            domicile_form = DomicileForm(request.POST, prefix='domicile')
            if domicile_form.is_valid():
                try:
                    domicile = domicile_form.save()
                    contact.domicile = domicile
                    contact.save()
                    messages.add_message(request, messages.SUCCESS, 'El domicilio ha sido registrado correctamente.')
                    return redirect('ver-contacto', pk=pk)
                except:
                    messages.add_message(request, messages.ERROR, 'El domicilio no se pudo registrar.')
        elif form_id == 'phone':
            phone_form = PhoneNumberForm(request.POST, prefix='phone')
            if phone_form.is_valid():
                try:
                    phone = phone_form.save()
                    contact.phone_number = phone
                    contact.save()
                    messages.add_message(request, messages.SUCCESS, 'El teléfono ha sido registrado correctamente')
                    return redirect('ver-contacto', pk=pk)
                except:
                    messages.add_message(request, messages.ERROR, 'El teléfono no se pudo registrar')
            

    context = {
        'contact' : contact,
        'active_page' : 'contactos',
        'domicile_form' : domicile_form,
        'phone_form': phone_form
    }
    return render(request, 'contactos/contacto.html', context)

def create_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            try:
                form.save()
                # Teniendo dos modelos, y para crear uno tengo que crear el otro
                # entonces puedo crear dos formularios por cada modelo, y pasar el formulario de uno al otro
                # durante la función save()
                # form.save(phone_number = phone_number)
                messages.add_message(request, messages.SUCCESS, 'El contacto ha sido creado correctamente.')
            except:
                messages.add_message(request, messages.ERROR, 'El contacto no se pudo crear.')
            return redirect('contactos')
    else:
        form = ContactForm()

    context = {
        'active_page' : 'contactos',
        'title' : 'Creando contacto',
        'form' : form,
        'newContact' : True
    }
    return render(request, 'contactos/formContact.html', context)

def update_contact(request, pk):
    contact = get_object_or_404(Contact, contact_id = pk)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            try:
                form.save()
                messages.add_message(request, messages.SUCCESS, 'El contacto ha sido actualizado correctamente.')
            except:
                messages.add_message(request, messages.ERROR, 'El contacto no se pudo actualizar.')
            return redirect('contactos')
    else:
        form = ContactForm(instance=contact)

    context = {
        'active_page' : 'contactos',
        'title' : 'Editando contacto',
        'form' : form,
        'newContact' : False,
        'contact' : contact
    }
    return render(request, 'contactos/formContact.html', context)

@require_POST
def delete_contact(request, pk):
    try:
        contacto = Contact.objects.get(contact_id=pk)
        name = contacto.name + ' ' + contacto.last_name_p + ' ' + contacto.last_name_m
        contacto.delete()
        messages.add_message(request, messages.SUCCESS, 'El contacto con nombre ' + name + ' ha sido eliminado correctamente.')
    except:
        messages.add_message(request, messages.ERROR, 'No se pudo eliminar el contacto.')
    
    return redirect('contactos')

# GRUPO
@require_POST
def create_group(request):
    name = request.POST['name']
    if not name:
        return JsonResponse({'success': False, 'message': 'El nombre del grupo es requerido.'})
    
    if Group.objects.filter(name=name).exists():
        return JsonResponse({'success': False, 'message': 'El grupo ya existe.'})
    
    group = Group.objects.create(name=name)

    return JsonResponse({'success': True, 'message': 'Grupo ' + group.name + ' creado con éxito.'})

@require_POST
def delete_group(request):
    try:
        group_id = request.POST['group_id']
        group = Group.objects.get(group_id = group_id)
        group.delete()

        return JsonResponse({'success': True, 'message': 'Se elimino el grupo con éxito.', 'id': group_id})
    except:
        return JsonResponse({'success': False, 'message': 'No se pudo eliminar el grupo.'})

# DOMICILIO
@require_POST
def delete_domicile(request, pk, domicile_id):
    try:
        domicile = Domicile.objects.get(domicile_id = domicile_id)
        domicile.delete()
        messages.add_message(request, messages.SUCCESS, 'El domicilio ha sido eliminado correctamente.')
    except:
        messages.add_message(request, messages.ERROR, 'No se pudo eliminar el domicilio.')
    
    return redirect('ver-contacto', pk=pk)

# TELEFONO
@require_POST
def delete_phone(request, pk, phone_id):
    try:
        phone = PhoneNumber.objects.get(phone_id = phone_id)
        phone.delete()
        messages.add_message(request, messages.SUCCESS, 'El teléfono ha sido eliminado correctamente.')
    except:
        messages.add_message(request, messages.ERROR, 'No se pudo eliminar el teléfono.')
    
    return redirect('ver-contacto', pk=pk)