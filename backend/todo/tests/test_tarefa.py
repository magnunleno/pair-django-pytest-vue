import pytest
from ..models import Tarefa


@pytest.fixture(scope="function")
def cria2tarefas(db):
    Tarefa.objects.create(descricao='Aprender Django Novamente')
    Tarefa.objects.create(descricao='Aprender Vue.js Novamente')


def test_index(db, client, cria2tarefas):
    response = client.get('/todo/')
    assert response.status_code == 200
    assert 'TODO List' in response.content.decode()
    assert 'Aprender Django Novamente' in response.content.decode()
    assert 'Aprender Vue.js Novamente' in response.content.decode()


def test_sem_fixture(db, client):
    response = client.get('/todo/')
    assert response.status_code == 200
    assert 'TODO List' in response.content.decode()
    assert 'Aprender Django Novamente' not in response.content.decode()
    assert 'Aprender Vue.js Novamente' not in response.content.decode()
