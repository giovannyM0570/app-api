from main import app

def test_home():
    client = app.test_client()
    response = client.get('/')
    assert response.data == b"hallois mijn eerste project"
