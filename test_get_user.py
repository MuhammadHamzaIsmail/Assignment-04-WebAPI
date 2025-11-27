import requests

def test_get_product(base_url):
    url = f"{base_url}/products/1"
    response = requests.get(url, verify=False)

    assert response.status_code == 200
    data = response.json()

    assert "title" in data
    assert data["id"] == 1
