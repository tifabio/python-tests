from flask import json
from app import app

product = {
    'id': '1',
    'title': 'Book',
    'price': 15
}

def testAddProduct():        
    response = app.test_client().post(
        '/cart/product',
        data=json.dumps(product),
        content_type='application/json',
    )

    assert response.status_code == 201

    response = app.test_client().get('/cart')
    json_response = response.get_json()

    assert len(json_response) == 1


def testRemoveProduct():        
    response = app.test_client().post(
        '/cart/product',
        data=json.dumps(product),
        content_type='application/json',
    )

    assert response.status_code == 201

    response = app.test_client().get('/cart')
    json_response = response.get_json()

    assert len(json_response) == 1

    response = app.test_client().delete(f"/cart/product/{product['id']}")

    assert response.status_code == 200