import requests

def test_delete_product(base_url):
    url = f"{base_url}/products/1"

    response = requests.delete(url, verify=False)

    assert response.status_code == 200 or response.status_code == 204
