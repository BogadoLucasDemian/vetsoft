from django.shortcuts import get_object_or_404, redirect, render, reverse

from .models import Client, Medicine, Pet, Product, Provider, Vet


def home(request):
    
    """
    Renderiza el template home.html que vendría a ser el menú principal (la pantalla de cards)
    """
    
    return render(request, "home.html")

def clients_repository(request):
    
    """
    Renderiza el template clients/repository.html. Este es el listado de clientes
    """
    
    clients = Client.objects.all()
    return render(request, "clients/repository.html", {"clients": clients})

def clients_form(request, id=None):
    
    """
    Renderiza el template clients/form.html, el cuál es el formulario de creación/edición de clientes.
    Valida si existe el id entre los parámetros del cuerpo de la request, si existe renderiza el form con datos a editar. De lo contrario renderiza para crear uno nuevo
    """
    if request.method == "POST":
        client_id = request.POST.get("id", "")
        errors = {}
        saved = True

        if client_id == "":
            saved, errors = Client.save_client(request.POST)
        else:
            client = get_object_or_404(Client, pk=client_id)
            saved, errors = client.update_client(request.POST) 

        if saved:
            return redirect(reverse("clients_repo"))

        return render(
            request, "clients/form.html", {"errors": errors, "client": request.POST},
        )

    client = None
    if id is not None:
        client = get_object_or_404(Client, pk=id)
    return render(request, "clients/form.html", {"client": client})

def clients_delete(request):
    
    """
    Permite recuperar un cliente y si existe lo elimina
    """
    
    client_id = request.POST.get("client_id")
    client = get_object_or_404(Client, pk=int(client_id))
    client.delete()

    return redirect(reverse("clients_repo"))

def providers_repository(request):
    
    """
    Renderiza el template providers/repository.html. Este es el listado de proveedores
    """
    
    providers = Provider.objects.all()
    return render(request, "providers/repository.html", {"providers": providers})

def providers_form(request, id=None):
    
    """
    Renderiza el template providers/form.html, el cuál es el formulario de creación/edición de proveedores.
    Valida si existe el id entre los parámetros del cuerpo de la request, si existe renderiza el form con datos a editar. De lo contrario renderiza para crear uno nuevo
    """
    
    if request.method == "POST":
        provider_id = request.POST.get("id", "")
        errors = {}
        saved = True

        if provider_id == "":
            saved, errors = Provider.save_provider(request.POST)
        else:
            provider = get_object_or_404(Provider, pk=provider_id)
            saved, errors = provider.update_provider(request.POST)

        if saved:
            return redirect(reverse("providers_repo"))

        return render(
            request, "providers/form.html", {"errors": errors, "provider": request.POST},
        )

    provider = None
    if id is not None:
        provider = get_object_or_404(Provider, pk=id)

    return render(request, "providers/form.html", {"provider": provider})

def providers_delete(request):
    
    """
    Permite recuperar un proveedor y si existe lo elimina
    """
    
    provider_id = request.POST.get("provider_id")
    provider = get_object_or_404(Provider, pk=int(provider_id))
    provider.delete()

    return redirect(reverse("providers_repo"))

def medicine_repository(request):
    
    """
    Renderiza el template medicine/repository.html. Este es el listado de medicamentos
    """
    
    medicines = Medicine.objects.all()
    return render(request, "medicine/repository.html", {"medicines": medicines})

def medicine_form(request, id=None):
    
    """
    Renderiza el template medicine/form.html, el cuál es el formulario de creación/edición de medicamentos.
    Valida si existe el id entre los parámetros del cuerpo de la request, si existe renderiza el form con datos a editar. De lo contrario renderiza para crear uno nuevo
    """
    

    if request.method == "POST":
        medicine_id = request.POST.get("id", "")
        errors = {}
        saved = True

        if medicine_id == "":
            saved, errors = Medicine.save_medicine(request.POST)
        else:
            medicine = get_object_or_404(Medicine, pk=medicine_id)
            saved, errors = medicine.update_medicine(request.POST)
            

        if saved:
            return redirect(reverse("medicine_repo"))

        return render(
            request, "medicine/form.html", {"errors": errors, "medicine": request.POST},
        )

    medicine = None
    if id is not None:
        medicine = get_object_or_404(Medicine, pk=id)

    return render(request, "medicine/form.html", {"medicine": medicine})

def medicine_delete(request):
    
    """
    Permite recuperar un medicamento y si existe lo elimina
    """
    
    medicine_id = request.POST.get("medicine_id")
    medicine = get_object_or_404(Medicine, pk=int(medicine_id))
    medicine.delete()

    return redirect(reverse("medicine_repo"))

def products_repository(request):
    
    """
    Renderiza el template products/repository.html. Este es el listado de productos
    """
    
    products = Product.objects.all()
    return render(request, "products/repository.html", {"products": products})

def products_form(request, id=None):
    
    """
    Renderiza el template products/form.html, el cuál es el formulario de creación/edición de productos.
    Valida si existe el id entre los parámetros del cuerpo de la request, si existe renderiza el form con datos a editar. De lo contrario renderiza para crear uno nuevo
    """
    
    if request.method == "POST":
        product_id = request.POST.get("id", "")
        errors = {}
        saved = True

        if product_id == "":
            saved, errors = Product.save_product(request.POST)
        else:
            product = get_object_or_404(Product, pk=product_id)
            saved, errors = product.update_product(request.POST)

        if saved:
            return redirect(reverse("products_repo"))

        return render(
            request, "products/form.html", {"errors": errors, "product": request.POST},
        )
    
    product = None
    if id is not None:
        product = get_object_or_404(Product, pk=id)

    return render(request, "products/form.html", {"product": product})

def products_delete(request):
    
    """
    Permite recuperar un producto y si existe lo elimina
    """
    
    product_id = request.POST.get("product_id")
    product = get_object_or_404(Product, pk=int(product_id))
    product.delete()

    return redirect(reverse("products_repo"))

def pets_repository(request):
    
    """
    Renderiza el template pets/repository.html. Este es el listado de mascotas
    """
    
    pets = Pet.objects.all()
    return render(request, "pets/repository.html", {"pets": pets})

def pets_form(request, id=None):
    
    """
    Renderiza el template pets/form.html, el cuál es el formulario de creación/edición de mascotas.
    Valida si existe el id entre los parámetros del cuerpo de la request, si existe renderiza el form con datos a editar. De lo contrario renderiza para crear uno nuevo
    """
    
    if request.method == "POST":
        pet_id = request.POST.get("id", "")
        errors = {}
        saved = True

        if pet_id == "":
            saved, errors = Pet.save_pet(request.POST)
        else:
            pet = get_object_or_404(Pet, pk=pet_id)
            saved, errors = pet.update_pet(request.POST)

        if saved:
            return redirect(reverse("pets_repo"))

        return render(
            request, "pets/form.html", {"errors": errors, "pet": request.POST},
        )
    
    pet = None
    if id is not None:
        pet = get_object_or_404(Pet, pk=id)

    return render(request, "pets/form.html", {"pet": pet})

def pets_delete(request):
    
    """
    Permite recuperar una mascota y si existe lo elimina
    """
    
    pet_id = request.POST.get("pet_id")
    pet = get_object_or_404(Pet, pk=int(pet_id))
    pet.delete()

    return redirect(reverse("pets_repo"))

def vets_repository(request):
    
    """
    Renderiza el template vets/repository.html. Este es el listado de veterinarios
    """
    
    vets = Vet.objects.all()
    return render(request, "vets/repository.html", {"vets": vets})

def vets_form(request, id=None):
    
    """
    Renderiza el template vets/form.html, el cuál es el formulario de creación/edición de veterinarios.
    Valida si existe el id entre los parámetros del cuerpo de la request, si existe renderiza el form con datos a editar. De lo contrario renderiza para crear uno nuevo
    """
    
    if request.method == "POST":
        vet_id = request.POST.get("id", "")
        errors = {}
        saved = True

        if vet_id == "":
            saved, errors = Vet.save_vet(request.POST)
        else:
            vet = get_object_or_404(Vet, pk=vet_id)
            saved, errors = vet.update_vet(request.POST)

        if saved:
            return redirect(reverse("vets_repo"))

        return render(
            request, "vets/form.html", {"errors": errors, "vet": request.POST},
        )

    vet = None
    if id is not None:
        vet = get_object_or_404(Vet, pk=id)

    return render(request, "vets/form.html", {"vet": vet})

def vets_delete(request):
    
    """
    Permite recuperar un veterinario y si existe lo elimina
    """
    
    vet_id = request.POST.get("vet_id")
    vet = get_object_or_404(Vet, pk=int(vet_id))
    vet.delete()

    return redirect(reverse("vets_repo"))