import requests

def test_post_product(base_url):
    url = f"{base_url}/products/add"
    payload = {
        "title": "Test Product",
        "price": 100
    }

    response = requests.post(url, json=payload, verify=False)

    # DummyJSON returns 201 for successful creation
    assert response.status_code == 201

    data = response.json()
    assert data["title"] == "Test Product"
