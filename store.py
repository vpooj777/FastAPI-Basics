from typing import Union, Optional
from fastapi import FastAPI

app = FastAPI()

# Fake Product Data
products = [
    {'id': 1, 'name': 'Laptop', 'category': 'electronics', 'price': 800, 'rating': 4.5},
    {'id': 2, 'name': 'Phone', 'category': 'electronics', 'price': 500, 'rating': 4.0},
    {'id': 3, 'name': 'Shirt', 'category': 'clothing', 'price': 20, 'rating': 3.8},
    {'id': 4, 'name': 'Shoes', 'category': 'clothing', 'price': 50, 'rating': 4.2},
    {'id': 5, 'name': 'Headphones', 'category': 'electronics',
        'price': 100, 'rating': 4.3},
]


@app.get('/products/')
def get_products(category: Optional[str] = None, sort_by_price: Optional[str] = None,
                 name: Optional[str] = None, min_price: Optional[int] = None,
                 max_price: Optional[int] = None, min_rating: Optional[float] = None,
                 max_rating: Optional[float] = None, limit: Optional[int] = 10,
                 search: Optional[str] = None, skip: Optional[int] = 0):

    # Filter products by category
    result = products
    if name:
        result = [p for p in products if p['name'] == name]
    if category:
        result = [p for p in products if p['category'] == category]
    if sort_by_price == 'asc':
        result = sorted(result, key=lambda x: x['price'])
    else:
        result = sorted(result, key=lambda x: x['price'], reverse=True)
    if min_price is not None:
        result = [p for p in products if p['price'] >= min_price]
    if max_price is not None:
        result = [p for p in products if p['price'] <= max_price]
    if min_rating is not None:
        result = [p for p in products if p['rating'] >= min_rating]
    if max_rating is not None:
        result = [p for p in products if p['rating'] <= max_rating]
    if search is not None:
        result = [p for p in products if search.lower() in p['name'].lower()]

    # if limit is not None:
    #     result = result[:limit]
    result=result[skip: skip + limit]
    return result
