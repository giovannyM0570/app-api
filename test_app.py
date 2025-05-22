from main import app

def test_home():
    client = app.test_client()
    response2 = client.get('/test')
    assert response2.data == b"hallo"
