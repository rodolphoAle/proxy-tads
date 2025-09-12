import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_proxy_request(client):
    data = {'id': 1, 'cpf': '12345678900'}
    response = client.post('/proxy', json=data)
    assert response.status_code == 202
    assert response.get_json()['status'] == 'Request received and queued.'

    # Testa múltiplos CPFs
    for i in range(2, 5):
        data = {'id': i, 'cpf': f'{i:011d}'}
        response = client.post('/proxy', json=data)
        assert response.status_code == 202