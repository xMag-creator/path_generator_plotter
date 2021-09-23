import pytest

from .utils import create_fake_machine
from django.test import Client


@pytest.fixture
def client():
    client = Client()
    return client


@pytest.fixture
def set_up():
    for _ in range(5):
        create_fake_machine()
