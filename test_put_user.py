import requests

def test_put_product(base_url):
    url = f"{base_url}/products/1"
    payload = {
        "title": "Updated Product",
        "price": 150
    }

    response = requests.put(url, json=payload, verify=False)

    assert response.status_code == 200
    data = response.json()

    assert data["title"] == "Updated Product"
