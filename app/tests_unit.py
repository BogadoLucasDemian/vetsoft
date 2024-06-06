import datetime

from django.test import TestCase

from app.models import (
    City,
    Client,
    Medicine,
    Pet,
    Product,
    Provider,
    Speciality,
    Vet,
    validate_client,
    validate_medicine,
    validate_pet,
    validate_product,
    validate_provider,
    validate_vet,
)


class ClientModelTest(TestCase):
    """
    Pruebas para la gestión de clientes en el sistema.
    """

    def test_can_create_and_get_client(self):
        """Prueba que se pueda crear y obtener un cliente correctamente."""

        city = "La Plata"
        self.assertTrue(self.is_valid_city(city))

        Client.save_client(
            {
                "name": "Juan Sebastian Veron",
                "phone": "54221555232",
                "city": city,
                "email": "brujita75@vetsoft.com",
            },
        )
        clients = Client.objects.all()
        self.assertEqual(len(clients), 1)

        self.assertEqual(clients[0].name, "Juan Sebastian Veron")
        self.assertEqual(clients[0].phone, "54221555232")
        self.assertEqual(clients[0].city, "La Plata")
        self.assertEqual(clients[0].email, "brujita75@vetsoft.com")

    def test_create_client_with_invalid_email(self):
        """Intenta crear un cliente con un email invalido"""
        data = {
                "name": "Juan Sebastian Veron",
                "phone": "54221555232",
                "city": "La Plata",
                "email": "brujita75",
            }
        errors = validate_client(data)
        self.assertIn("email", errors)
        self.assertEqual(errors["email"], "Por favor ingrese un email valido")

    def test_create_client_with_invalid_email_vetsoft_com(self):
        """Intenta crear un cliente con un email que no contenga 'vetsoft.com'"""
        data = {
                "name": "Juan Sebastian Veron",
                "phone": "221555232",
                "city": "La Plata",
                "email": "brujita75@gmail.com",
            }
        errors = validate_client(data)
        self.assertIn("email", errors)
        self.assertEqual(errors["email"], "Por favor ingrese un email que incluya '@vetsoft.com'")

    def test_can_update_client(self):
        """Prueba que se pueda actualizar la información de un cliente correctamente."""
        Client.save_client(
            {
                "name": "Juan Sebastian Veron",
                "phone": "54221555232",
                "city": "La Plata",
                "email": "brujita75@vetsoft.com",
            },
        )
        client = Client.objects.get(pk=1)

        self.assertEqual(client.phone, "54221555232")

        client.update_client({
            "name": "Juan Sebastian Veron",
            "phone": "54221555233",
            "city": "La Plata",
            "email": "brujita75@vetsoft.com",
            })

        client_updated = Client.objects.get(pk=1)

        self.assertEqual(client_updated.phone, "54221555233")

    def test_update_client_with_error(self):
        """
    Prueba que el cliente no se actualice si se proporciona un número de teléfono vacío.

    Se crea un cliente con un número de teléfono válido. Luego se intenta
    actualizar el cliente con un número de teléfono vacío. Se verifica que
    el número de teléfono del cliente no cambie después de intentar la actualización.
        """
        Client.save_client(
            {
                "name": "Juan Sebastian Veron",
                "phone": "54221555232",
                "city": "La Plata",
                "email": "brujita75@vetsoft.com",
            },
        )
        client = Client.objects.get(pk=1)

        self.assertEqual(client.phone, "54221555232")

        client.update_client({"phone": ""})

        client_updated = Client.objects.get(pk=1)

        self.assertEqual(client_updated.phone, "54221555232")

    def test_validate_client_incorrect_name(self):
        """
        Prueba que verifica que si un nombre es ingresado con algún caracter que no sean letras minúsculas, mayúsculas o espacios devuelva el error
        """

        data = {
            "name": "Juan Sebastian Veron 11",
            "phone": "54221555232",
            "city": "La Plata",
            "email": "brujita75@vetsoft.com",
        }

        result = validate_client(data)

        self.assertIn("El nombre debe contener solo letras y espacios", result.values())

    def test_update_client_with_invalid_email(self):
        """
    Prueba que el cliente no se actualice si se proporciona un email invalido

    Se crea un cliente con un email válido. Luego se intenta
    actualizar el cliente con un email invalido. Se verifica que
    el email cliente no cambie después de intentar la actualización.
        """
        Client.save_client(
            {
                "name": "Juan Sebastian Veron",
                "phone": "54221555232",
                "city": "La Plata",
                "email": "brujita75@vetsoft.com",
            },
        )
        client = Client.objects.get(pk=1)

        self.assertEqual(client.email, "brujita75@vetsoft.com")

        client.update_client({"email": "brujita75@gmail.com"})

        client_updated = Client.objects.get(pk=1)
        
        self.assertEqual(client_updated.email, "brujita75@vetsoft.com")
        
    def test_update_client_with_empty_name(self):
        """Prueba que verifica si se produce un error al intentar actualizar un cliente con un campo de nombre vacío.""" 
        Client.save_client(
            {
                "name": "Juan Sebastian Veron",
                "phone": "54221555232",
                "city": "La Plata",
                "email": "brujita75@vetsoft.com",
            },
        )
        client = Client.objects.get(pk=1)
        
        self.assertEqual(client.name, "Juan Sebastian Veron")
        
        client.update_client({"name": ""})
        client_updated = Client.objects.get(pk=1)
        
        self.assertEqual(client_updated.name, "Juan Sebastian Veron")

    def test_update_client_with_incorrect_name(self):
        """Prueba que verifica si se produce un error al intentar actualizar un cliente con un campo de nombre incorrecto.""" 
        Client.save_client(
            {
                "name": "Juan Sebastian Veron",
                "phone": "54221555232",
                "city": "La Plata",
                "email": "brujita75@vetsoft.com",
            },
        )
        client = Client.objects.get(pk=1)
        
        self.assertEqual(client.name, "Juan Sebastian Veron")
        
        client.update_client({"name": "Juan Sebastian Veron 11"})
        client_updated = Client.objects.get(pk=1)
        
        self.assertEqual(client_updated.name, "Juan Sebastian Veron")
    
    def test_create_client_with_invalid_phone(self):
        """Intenta crear un cliente con un telefono invalido"""
        data = {
                "name": "Juan Sebastian Veron",
                "phone": "11221555232",
                "city": "La Plata",
                "email": "brujita75",
            }
        errors = validate_client(data)
        self.assertIn("phone", errors)
        self.assertEqual(errors["phone"], "El teléfono debe empezar con el prefijo 54")
    
    def test_update_client_with_incorrect_phone(self):
        """Prueba que verifica si se produce un error al intentar actualizar un cliente con un campo de telefono incorrecto.""" 
        Client.save_client(
            {
                "name": "Juan Sebastian Veron",
                "phone": "54221555232",
                "city": "La Plata",
                "email": "brujita75@vetsoft.com",
            },
        )
        client = Client.objects.get(pk=1)
        
        self.assertEqual(client.phone, "54221555232")
        
        client.update_client({"phone": "11221555232"})
        client_updated = Client.objects.get(pk=1)
        
        self.assertEqual(client_updated.phone, "54221555232")

    def test_validate_phone_with_non_numeric_value(self):
        """Prueba que verifica que la validación del teléfono genere un error si se proporciona un valor no numérico."""

        # Datos de cliente con teléfono no numérico
        form_data = {
            "name": "Juan Sebastian Veron",
            "phone": "ee21",  # Número de teléfono no numérico
            "city": "La Plata",
            "email": "brujita75@hotmail.com",
        }

        # Crear un cliente inicial con los datos proporcionados
        client = Client.objects.create(**form_data)

        # Verificar que el teléfono inicial es correcto
        self.assertEqual(client.phone, "ee21")

        # Intentar actualizar el cliente con un número de teléfono no numérico
        success, errors = client.update_client({"phone": "ee32w3"})

        # Verificar que la actualización falló
        self.assertFalse(success)

        # Verificar que se mantuvo el teléfono original
        updated_client = Client.objects.get(pk=client.pk)
        self.assertEqual(updated_client.phone, "ee21")

        # Verificar que el error relacionado con el teléfono no numérico se haya devuelto
        self.assertIn("phone", errors)
        self.assertEqual(errors["phone"], "El teléfono debe ser un número")

    def is_valid_city(self, city):
        """
        Verifica si una ciudad dada es válida
        """
        return city in [choice.value for choice in City]
    
    def test_empty_city_error(self):
        """
    Prueba que verifica si se produce un error al intentar crear un veterinario con una especialidad vacía.

    Se crea un diccionario de datos que representa un veterinario con una especialidad vacía.
    Luego, se valida el diccionario de datos y se verifica que se encuentre el mensaje de error
    correspondiente en los errores generados.
        """
        data = {
            "name": "Juan Sebastian Veron",
            "phone": "54221555233",
            "city": "",
            "email": "brujita75@vetsoft.com",
        }

        errors = validate_client(data)

        self.assertIn("Por favor seleccione una ciudad", errors.values())

class TestValidateProduct(TestCase):
    """
    Pruebas para la validación de productos.
    """

    def test_valid_price(self):
        """Prueba que verifica si el precio es válido."""
        data = {
            "name": "ampicilina",
            "type": "antibiotico",
            "price": "100",
        }
        errors = validate_product(data)
        self.assertNotIn("price", errors)
    
    def test_price_equal_zero(self):
        """Prueba que verifica si el precio es igual a cero."""
        data = {
            "name": "ampicilina",
            "type": "antibiotico",
            "price": "0",
        }
        errors = validate_product(data)
        self.assertIn("price", errors)
        self.assertEqual(errors["price"], "Por favor ingrese un precio mayor a cero")

    def test_price_missing(self):
        """Prueba que verifica si falta el precio."""
        data = {
            "name": "ampicilina",
            "type": "antibiotico",
            "price": "",
        }
        errors = validate_product(data)
        self.assertIn("price", errors)
        self.assertEqual(errors["price"], "Por favor ingrese un precio")
    
    def test_negative_price(self):
        """Prueba que verifica si se proporciona un precio negativo."""
        data = {
            "name": "ampicilina",
            "type": "antibiotico",
            "price": "-10",
        }
        errors = validate_product(data)
        self.assertIn("price", errors)
        self.assertEqual(errors["price"], "Por favor ingrese un precio mayor a cero")

    def test_can_update_valid_price(self):
        """Prueba que verifica si se puede actualizar un producto con un precio válido."""
        Product.save_product(
            {
                "name": "ampicilina",
                "type": "antibiotico",
                "price": "10",
            },
        )
        product = Product.objects.get(pk=1)
        
        self.assertEqual(product.name, "ampicilina")
        
        product.update_product({
            "name": "ampicilina",
            "type": "antibiotico",
            "birthday": "10",
        })
        
        product_updated = Product.objects.get(pk=1)
        self.assertEqual(product_updated.name, "ampicilina")

    def test_update_product_with_error(self):
        """Prueba que verifica si ocurre un error al intentar actualizar un producto con datos incorrectos.""" 
        Product.save_product(
            {
                "name": "ampicilina",
                "type": "antibiotico",
                "price": "10",
            },
        )
        product = Product.objects.get(pk=1)
        
        self.assertEqual(product.name, "ampicilina")
        
        product.update_product({"name": ""})
        
        product_updated = Product.objects.get(pk=1)
        self.assertEqual(product_updated.name, "ampicilina")

    def test_update_product_with_error_price(self):
        """Prueba que verifica si se produce un error al intentar actualizar un producto con un precio negativo.""" 
        data = {
                "name": "ampicilina",
                "type": "antibiotico",
                "price": "-10",
            }
        
        result = validate_product(data)
        self.assertIn("Por favor ingrese un precio mayor a cero", result.values())

    def test_validate_product_all_ok(self):
        """Prueba que verifica si la validación de datos del producto es exitosa cuando se proporcionan todos los datos necesarios."""
        data = {
                "name": "ampicilina",
                "type": "antibiotico",
                "price": "10",
            }
        
        result = validate_product(data)
        
        self.assertDictEqual(result,{})

    def test_validate_product_empty_data(self):
        """Prueba que verifica si se producen errores cuando no se proporcionan datos para el producto."""
        data = {
                "name": "",
                "type": "",
                "price": "",
            }
        
        result = validate_product(data)
        
        self.assertIn("Por favor ingrese un nombre",result.values())
        self.assertIn("Por favor ingrese un tipo",result.values())
        self.assertIn("Por favor ingrese un precio",result.values())

    def test_validate_product_incorrect_name(self): 
        """Prueba que verifica que si un nombre es ingresado con algún caracter que no sean letras minúsculas,
        mayúsculas o espacios devuelva el error"""
        
        data = {
            "name": "ampicilina 21",
            "type": "antibiotico",
            "price": "10",
        }

        result = validate_product(data)

        self.assertIn("El nombre debe contener solo letras y espacios", result.values())

    def test_update_product_with_incorrect_name(self):
        """Prueba que verifica si se produce un error al intentar actualizar un producto con un campo de nombre incorrecto.""" 
        Product.save_product(
            {
                "name": "ampicilina",
                "type": "antibiotico",
                "price": "10",
            },
        )
        product = Product.objects.get(pk=1)
        
        self.assertEqual(product.name, "ampicilina")
        
        product.update_product({"name": "ampicilina 21"})
        product_updated = Product.objects.get(pk=1)
        
        self.assertEqual(product_updated.name, "ampicilina")


class PetModelTest(TestCase):
    """
    Pruebas para la gestión de mascotas en el sistema.
    """

    def test_can_create_and_get_pet(self):
        """Prueba que verifica si se puede crear y obtener una mascota correctamente."""
        Pet.save_pet(
            {
                "name": "gatito",
                "breed": "orange",
                "birthday": "2024-05-18",
            },
        )
        pets = Pet.objects.all()
        self.assertEqual(len(pets), 1)
    
    def test_can_update_pet(self):
        """Prueba que verifica si se puede actualizar una mascota correctamente."""
        Pet.save_pet(
            {
                "name": "gatito",
                "breed": "orange",
                "birthday": "2024-05-18",
            },
        )
        pet = Pet.objects.get(pk=1)
        
        self.assertEqual(pet.name, "gatito")
        
        pet.update_pet({
            "name": "gato",
            "breed": "orange",
            "birthday": "2024-05-18",
        })
        pet_updated = Pet.objects.get(pk=1)
        
        self.assertEqual(pet_updated.name, "gato")
    def test_update_pet_with_error(self):
        """Prueba que verifica si se produce un error al intentar actualizar una mascota con un campo de nombre vacío.""" 
        Pet.save_pet(
            {
                "name": "gatito",
                "breed": "orange",
                "birthday": "2024-05-18",
            },
        )
        pet = Pet.objects.get(pk=1)
        
        self.assertEqual(pet.name, "gatito")
        
        pet.update_pet({"name": ""})
        pet_updated = Pet.objects.get(pk=1)
        
        self.assertEqual(pet_updated.name, "gatito")
    
    def test_validate_pet_all_ok(self):
        """Prueba que valida si todos los campos de una mascota están llenos correctamente."""
        data = {
                "name": "gatito",
                "breed": "orange",
                "birthday": "2024-05-18",
            }
        
        result = validate_pet(data)
        
        self.assertDictEqual(result,{})
    
    def test_validate_pet_empty_data(self):
        """Prueba que verifica si se detectan errores cuando todos los campos de una mascota están vacíos."""
        data = {
                "name": "",
                "breed": "",
                "birthday": "",
            }
        
        result = validate_pet(data)
        
        self.assertIn("Por favor ingrese una fecha de nacimiento valida y anterior a la de hoy",result.values())
        self.assertIn("Por favor ingrese un nombre",result.values())
        self.assertIn("Por favor ingrese una raza",result.values())
    
    def test_validate_pet_invalid_birthday_today(self):
        """Prueba que verifica si se detecta un error cuando la fecha de nacimiento de la mascota es la misma que la fecha actual."""
        date_now = datetime.date.today().strftime("%Y-%m-%d")
        data = {
            "name": "gatito",
                "breed": "orange",
                "birthday": date_now,
        }
        
        result = validate_pet(data)
        
        self.assertIn("Por favor ingrese una fecha de nacimiento valida y anterior a la de hoy",result.values())
    
    def test_validate_pet_invalid_birthday_date_later_than_today(self):
        """Prueba que verifica si se detecta un error cuando la fecha de nacimiento de la mascota es posterior a la fecha actual."""
        date_now = datetime.date.today()
        date_later = date_now + datetime.timedelta(days=1)
        date = date_later.strftime("%Y-%m-%d")
        
        data = {
            "name": "gatito",
            "breed": "orange",
            "birthday": date,
        }
        
        result = validate_pet(data)
        
        self.assertIn("Por favor ingrese una fecha de nacimiento valida y anterior a la de hoy",result.values())

    def test_validate_pet_incorrect_name(self):
        """Prueba que verifica que si un nombre es ingresado con algún caracter que no sean letras minúsculas,
        mayúsculas o espacios devuelva el error"""
        
        data = {
            "name": "gatito 10",
            "breed": "orange",
            "birthday": "2024-05-18",
        }

        result = validate_pet(data)

        self.assertIn("El nombre debe contener solo letras y espacios", result.values())

    def test_update_pet_with_incorrect_name(self):
        """Prueba que verifica si se produce un error al intentar actualizar una mascota con un campo de nombre incorrecto.""" 
        Pet.save_pet(
            {
                "name": "gatito",
                "breed": "orange",
                "birthday": "2024-05-18",
            },
        )
        pet = Pet.objects.get(pk=1)
        
        self.assertEqual(pet.name, "gatito")
        
        pet.update_pet({"name": "gatito 10"})
        pet_updated = Pet.objects.get(pk=1)
        
        self.assertEqual(pet_updated.name, "gatito")


class VetModelTest(TestCase):
    """
    Pruebas para la gestión de veterinarios en el sistema.
    """

    def test_can_create_and_get_vet(self):
        """
        Prueba que verifica si se puede crear y obtener un veterinario correctamente.

        Se asegura de que el veterinario se crea correctamente y que todos los campos tienen los valores esperados.
        """
        speciality = "Urgencias"
        self.assertTrue(self.is_valid_speciality(speciality))
        
        Vet.save_vet(
            {
                "name": "Juan Sebastian Veron",
                "email": "brujita75@hotmail.com",
                "phone": "54221555232",
                "speciality": speciality,
            },
        )
        
        vets = Vet.objects.all()
        self.assertEqual(len(vets), 1)
        
        self.assertEqual(vets[0].name, "Juan Sebastian Veron")
        self.assertEqual(vets[0].email, "brujita75@hotmail.com")
        self.assertEqual(vets[0].phone, "54221555232")
        self.assertEqual(vets[0].speciality, "Urgencias")
    
    def test_can_update_vet(self):
        """
    Prueba que verifica si se puede actualizar un veterinario correctamente.

    Se asegura de que el veterinario se crea inicialmente con un número de teléfono,
    luego se actualiza el número de teléfono y se verifica que la actualización sea exitosa.
        """
        Vet.save_vet(
            {
                "name": "Juan Sebastian Veron",
                "email": "brujita75@hotmail.com",
                "phone": "54221555232",
                "speciality": "Urgencias",
            },
        )
        
        vet = Vet.objects.get(pk=1)
        self.assertEqual(vet.phone, "54221555232")
        
        vet.update_vet({
            "name": "Juan Sebastian Veron",
            "email": "brujita75@hotmail.com",
            "phone": "54221555233",
            "speciality": "Urgencias",
            })
        
        vet_updated = Vet.objects.get(pk=1)
        
        self.assertEqual(vet_updated.phone, "54221555233")
    
    def test_update_vet_with_error(self):
        """
    Prueba que verifica que un veterinario no se actualice si se proporcionan datos inválidos.

    Se asegura de que el veterinario se crea inicialmente con un número de teléfono válido.
    Luego, se intenta actualizar el veterinario con un número de teléfono vacío y se verifica
    que el número de teléfono no se haya actualizado.
        """
        Vet.save_vet(
            {
                "name": "Juan Sebastian Veron",
                "email": "brujita75@hotmail.com",
                "phone": "54221555232",
                "speciality": "Urgencias",
            },
        )
        
        vet = Vet.objects.get(pk=1)
        self.assertEqual(vet.phone, "54221555232")
        
        vet.update_vet({"phone": ""})
        vet_updated = Vet.objects.get(pk=1)
        
        self.assertEqual(vet_updated.phone, "54221555232")

    def is_valid_speciality(self, speciality):
        """
        Verifica si una especialidad dada es válida
        """
        return speciality in [choice.value for choice in Speciality]
    
    def test_empty_speciality_error(self):
        """
    Prueba que verifica si se produce un error al intentar crear un veterinario con una especialidad vacía.

    Se crea un diccionario de datos que representa un veterinario con una especialidad vacía.
    Luego, se valida el diccionario de datos y se verifica que se encuentre el mensaje de error
    correspondiente en los errores generados.
        """
        data = {
            "name": "Juan Sebastian Veron",
            "email": "brujita75@hotmail.com",
            "phone": "221555232",
            "speciality": "",
        }

        errors = validate_vet(data)

        self.assertIn("Por favor seleccione una especialidad", errors.values())

    def test_validate_vet_incorrect_name(self):
        """Prueba que verifica que si un nombre es ingresado con algún caracter que no sean letras minúsculas,
        mayúsculas o espacios devuelva el error"""
        
        data = {
            "name": "Juan Sebastian Veron 11",
            "email": "brujita75@hotmail.com",
            "phone": "221555232",
            "speciality": "Urgencias",
        }

        result = validate_vet(data)

        self.assertIn("El nombre debe contener solo letras y espacios", result.values())

    def test_validate_vet_with_empty_name(self):
        """Prueba que verifica que no se pueda crear un veterinario con el campo nombre vacío"""
        data = {
            "name": "",
            "email": "brujita75@hotmail.com",
            "phone": "221555232",
            "speciality": "Urgencias",
        }

        errors = validate_vet(data)

        self.assertIn("Por favor ingrese un nombre", errors.values())

    def test_update_vet_with_empty_name(self):
        """Prueba que verifica si se produce un error al intentar actualizar un veterinario con un campo de nombre vacío.""" 
        Vet.save_vet(
            {
                "name": "Juan Sebastian Veron",
                "email": "brujita75@hotmail.com",
                "phone": "54221555232",
                "speciality": "Urgencias",
            },
        )
        vet = Vet.objects.get(pk=1)
        
        self.assertEqual(vet.name, "Juan Sebastian Veron")
        
        vet.update_vet({"name": ""})
        vet_updated = Vet.objects.get(pk=1)
        
        self.assertEqual(vet_updated.name, "Juan Sebastian Veron")
    
    def test_update_vet_with_incorrect_name(self):
        """Prueba que verifica si se produce un error al intentar actualizar un veterinario con un campo de nombre incorrecto.""" 
        Vet.save_vet(
            {
                "name": "Juan Sebastian Veron",
                "email": "brujita75@hotmail.com",
                "phone": "54221555232",
                "speciality": "Urgencias",
            },
        )
        vet = Vet.objects.get(pk=1)
        
        self.assertEqual(vet.name, "Juan Sebastian Veron")
        
        vet.update_vet({"name": "Juan Sebastian Veron 11"})
        vet_updated = Vet.objects.get(pk=1)
        
        self.assertEqual(vet_updated.name, "Juan Sebastian Veron")
    
    def test_create_vet_with_invalid_phone(self):
        """Intenta crear un veterinario con un telefono invalido"""
        data = {
                "name": "Juan Sebastian Veron",
                "email": "brujita75",
                "phone": "11221555232",
                "speciality": "Urgencias",
            }
        errors = validate_vet(data)
        self.assertIn("phone", errors)
        self.assertEqual(errors["phone"], "El teléfono debe empezar con el prefijo 54")
    
    def test_update_vet_with_incorrect_phone(self):
        """Prueba que verifica si se produce un error al intentar actualizar un veterinario con un campo de telefono incorrecto.""" 
        Vet.save_vet(
            {
                "name": "Juan Sebastian Veron",
                "email": "brujita75@edlp.com",
                "phone": "54221555232",
                "speciality": "Urgencias",
            },
        )
        vet = Vet.objects.get(pk=1)
        
        self.assertEqual(vet.phone, "54221555232")
        
        vet.update_vet({"phone": "11221555232"})
        vet_updated = Vet.objects.get(pk=1)
        
        self.assertEqual(vet_updated.phone, "54221555232")


class ProviderModelTest(TestCase):
    """
    Pruebas para la gestión de proveedores en el sistema.
    """

    def test_can_create_and_get_provider(self):
        """Prueba que verifica si se puede crear y obtener un proveedor."""

        city = "La Plata"
        self.assertTrue(self.is_valid_city(city))

        Provider.save_provider(
            {
                "name":"Demian",
                "email":"demian@utn.com",
                "city":city,
            },
        )

        providers = Provider.objects.all()
        self.assertEqual(len(providers), 1)

    def test_validate_empty_city_when_create_provider(self):
        """Prueba que valida una ciudad vacía al crear un proveedor."""
        provider_data = {
                "name":"Demian",
                "email":"demian@utn.com",
                "city":"",
            }

        result = validate_provider(provider_data)

        self.assertIn("Por favor seleccione una ciudad", result.values())

    def test_validate_provider_with_everything_ok(self):
        """Prueba la validación de un proveedor con todos los campos válidos."""
        provider_data = {
            "name":"Demian",
            "email":"demian@utn.com",
            "city":"La Plata",
        }

        result = validate_provider(provider_data)

        self.assertDictEqual(result, {})

    def test_validate_empty_data(self):
        """Prueba la validación de un proveedor con datos vacíos."""
        provider_data = {
            "name":"",
            "email":"",
            "city":"",
        }

        result = validate_provider(provider_data)
        self.assertIn("Por favor ingrese un nombre", result.values())
        self.assertIn("Por favor ingrese un email", result.values())
        self.assertIn("Por favor seleccione una ciudad", result.values())

    def test_can_update_provider(self):
        """Prueba que verifica si se puede actualizar un proveedor."""
        Provider.save_provider(
            {
                "name":"Demian",
                "email":"demian@utn.com",
                "city":"La Plata",
            },
        )

        provider = Provider.objects.get(pk=1)

        self.assertEqual(provider.name, "Demian")

        provider.update_provider({
            "name":provider.name,
            "email":provider.email,
            "city":"Berisso",
        })

        updated_provider = Provider.objects.get(pk=1)

        self.assertEqual(updated_provider.city, "Berisso")

    def test_cant_update_with_empty_city(self):
        """Prueba que verifica que no se puede actualizar con una ciudad vacía."""
        Provider.save_provider(
            {
                "name":"Demian",
                "email":"demian@utn.com",
                "city":"La Plata",
            },
        )

        provider = Provider.objects.get(pk=1)

        provider.update_provider({
            "name":provider.name,
            "email":provider.email,
            "city":"",
        })

        updated_provider = Provider.objects.get(pk=1)

        self.assertEqual(updated_provider.city, "La Plata")

    def test_validate_providert_incorrect_name(self):
        """Prueba que verifica que si un nombre es ingresado con algún caracter que no sean letras minúsculas,
        mayúsculas o espacios devuelva el error"""
        
        data = {
            "name":"Demian 7",
            "email":"demian@vetsoft.com",
            "city":"La Plata",
        }

        result = validate_provider(data)

        self.assertIn("El nombre debe contener solo letras y espacios", result.values())

    def test_update_provider_with_empty_name(self):
        """Prueba que verifica si se produce un error al intentar actualizar un proveedor con un campo de nombre vacío.""" 
        Provider.save_provider(
            {
                "name":"Demian",
                "email":"demian@vetsoft.com",
                "city":"La Plata",
            },
        )
        provider = Provider.objects.get(pk=1)
        
        self.assertEqual(provider.name, "Demian")
        
        provider.update_provider({"name": ""})
        provider_updated = Provider.objects.get(pk=1)
        
        self.assertEqual(provider_updated.name, "Demian")

    def test_update_provider_with_incorrect_name(self):
        """Prueba que verifica si se produce un error al intentar actualizar un proveedor con un campo de nombre incorrecto.""" 
        Provider.save_provider(
            {
                "name":"Demian",
                "email":"demian@vetsoft.com",
                "city":"La Plata",
            },
        )
        provider = Provider.objects.get(pk=1)
        
        self.assertEqual(provider.name, "Demian")
        
        provider.update_provider({"name": "Demian 7"})
        provider_updated = Provider.objects.get(pk=1)
        
        self.assertEqual(provider_updated.name, "Demian")

    def is_valid_city(self, city):
        """
        Verifica si una ciudad dada es válida
        """
        return city in [choice.value for choice in City]

class MedicineModelTest(TestCase):
    """
    Pruebas para la gestión de medicamentos en el sistema.
    """

    def test_can_create_and_get_medicine(self):
        """Prueba que verifica si se puede crear y obtener un medicamento."""
        Medicine.save_medicine(
            {
                "name": "Meloxicam",
                "description": "Antiinflamatorio y analgesico",
                "dose": "2",
            },
        )
        medicines = Medicine.objects.all()
        self.assertEqual(len(medicines), 1)
        
        self.assertEqual(medicines[0].name, "Meloxicam")
        self.assertEqual(medicines[0].description, "Antiinflamatorio y analgesico")
        self.assertEqual(medicines[0].dose, 2)
        
    def test_can_update_medicine(self):
        """Prueba que verifica si se puede actualizar un medicamento."""
        Medicine.save_medicine(
            {
                "name": "Meloxicam",
                "description": "Antiinflamatorio y analgesico",
                "dose": "2",
            },
        )
        medicine = Medicine.objects.get(pk=1)
        
        self.assertEqual(medicine.dose, 2)
        
        medicine.update_medicine(
            {
            "name": "Meloxicam",
                "description": "Antiinflamatorio y analgesico",
                "dose": "8",
            },
        )
        
        medicine_updated = Medicine.objects.get(pk=1)
        
        self.assertEqual(medicine_updated.dose, 8)
        
    def test_update_medicine_with_error(self):
        """Prueba que verifica que no se puede actualizar un medicamento con un nombre vacío."""
        Medicine.save_medicine(
            {
                "name": "Meloxicam",
                "description": "Antiinflamatorio y analgesico",
                "dose": "2",
            },
        )
        medicine = Medicine.objects.get(pk=1)
        
        self.assertEqual(medicine.name, "Meloxicam")
        
        medicine.update_medicine({"name": ""})
        
        medicine_updated = Medicine.objects.get(pk=1)
        
        self.assertEqual(medicine_updated.name, "Meloxicam")
    
    def test_validate_medicine_invalid_dose(self):
        """Prueba la validación de un medicamento con dosis inválida."""
        data = {
                "name": "Meloxicam",
                "description": "Antiinflamatorio y analgesico",
                "dose": "41",
            }
        
        result = validate_medicine(data)
        self.assertIn("La dosis debe estar entre 1 y 10", result.values())
        
    def test_validate_medicine_decimal_dose(self):
        """Prueba la validación de un medicamento con dosis decimal."""
        data = {
                "name": "Meloxicam",
                "description": "Antiinflamatorio y analgesico",
                "dose": "4.1",
            }
        
        result = validate_medicine(data)
        self.assertIn("La dosis debe ser un numero entero", result.values())

    def test_validate_medicine_incorrect_name(self):
        """Prueba que verifica que si un nombre es ingresado con algún caracter que no sean letras minúsculas,
        mayúsculas o espacios devuelva el error"""
        
        data = {
            "name": "Meloxicam 700",
            "description": "Antiinflamatorio y analgesico",
            "dose": "2",
        }

        result = validate_medicine(data)

        self.assertIn("El nombre debe contener solo letras y espacios", result.values())

    def test_validate_client_with_empty_name(self):
        """Prueba que verifica que no se pueda crear un medicamento con el campo nombre vacío"""
        data = {
            "name": "",
            "description": "Antiinflamatorio y analgesico",
            "dose": "2",
        }

        errors = validate_medicine(data)

        self.assertIn("Por favor, ingrese un nombre de la medicina", errors.values())

    def test_update_medicine_with_incorrect_name(self):
        """Prueba que verifica si se produce un error al intentar actualizar una medicina con un campo de nombre incorrecto.""" 
        Medicine.save_medicine(
            {
                "name": "Meloxicam",
                "description": "Antiinflamatorio y analgesico",
                "dose": "2",
            },
        )
        medicine = Medicine.objects.get(pk=1)
        
        self.assertEqual(medicine.name, "Meloxicam")
        
        medicine.update_medicine({"name": "Meloxicam 700"})
        medicine_updated = Medicine.objects.get(pk=1)
        
        self.assertEqual(medicine_updated.name, "Meloxicam")
