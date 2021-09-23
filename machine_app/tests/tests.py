import pytest
from django.test import TestCase
from machine_app.models import Machine
from .utils import fake_machine_data, fake_range


# Create your tests here.
@pytest.mark.django_db
def test_add_machine(client, set_up):
    machines_count = Machine.objects.count()
    new_machine = fake_machine_data()
    response = client.post("/add_machine/", new_machine)
    assert response.status_code == 302
    assert Machine.objects.count() == machines_count + 1


@pytest.mark.django_db
def test_get_machine_list(client, set_up):
    response = client.get("/list_machines/")

    assert response.status_code == 200
    assert Machine.objects.count() == len(response.context['machines'])


@pytest.mark.django_db
def test_get_machine_details(client, set_up):
    machine = Machine.objects.first()
    response = client.get(f"/detail_machine/{machine.pk}/", {})
    print(response.context['machine'])
    assert response.status_code == 200
    assert machine.name == response.context['machine'].name


@pytest.mark.django_db
def test_delete_machine(client, set_up):
    machine = Machine.objects.first()
    response = client.delete(f"/delete_machine/{machine.pk}/", {})
    assert response.status_code == 302
    machines_ids = [machine.id for machine in Machine.objects.all()]
    assert machine.id not in machines_ids


@pytest.mark.django_db
def test_edit_machine(client, set_up):
    machine = Machine.objects.first()
    machine_data = fake_machine_data()
    response = client.post(f"/edit_machine/{machine.pk}/", machine_data)
    assert response.status_code == 302
    machine_obj = Machine.objects.get(pk=machine.pk)
    assert machine_obj.x_max_range == machine_data['x_max_range']
    assert machine_obj.name == machine_data['name']
