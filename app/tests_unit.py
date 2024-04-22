from django.test import TestCase
from app.models import Client

class ClientModelTest(TestCase):
    def test_can_create_and_get_client(self):
        Client.objects.create(
            name="Juan Sebastian Veron",
            phone="221555232",
            address="13 y 44",
            email="brujita75@hotmail.com",
        )
        clients = Client.objects.all()
        self.assertEqual(len(clients), 1)

        self.assertEqual(clients[0].name, "Juan Sebastian Veron")
        self.assertEqual(clients[0].phone, "221555232")
        self.assertEqual(clients[0].address, "13 y 44")
        self.assertEqual(clients[0].email, "brujita75@hotmail.com")

    def test_can_update_client(self):
        Client.objects.create(
            name="Juan Sebastian Veron",
            phone="221555232",
            address="13 y 44",
            email="brujita75@hotmail.com",
        )
        client = Client.objects.get(pk=1)
        
        self.assertEqual(client.phone, "221555232")

        client.phone="221555233"

        client.save()

        client_updated = Client.objects.get(pk=1)

        self.assertEqual(client_updated.phone, "221555233")

    def test_can_delete_client(self):
        Client.objects.create(
            name="Juan Sebastian Veron",
            phone="221555232",
            address="13 y 44",
            email="brujita75@hotmail.com",
        )
        clients = Client.objects.all()
        self.assertEqual(len(clients), 1)

        clients[0].delete()

        clients_updated = Client.objects.all()

        self.assertEqual(len(clients_updated), 0)
