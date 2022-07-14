from fastapi import APIRouter
from Config.db import conn
from sqlalchemy import select

from models.Product import products

from schema.Product import Product, ProductUpdate

product_router = APIRouter()

@product_router.get('/products/{menu_id}')
def get_product(menu_id:int):
    try:
        list_product = []
        result_products = conn.execute(select(products).where(products.c.menu_id == menu_id)).fetchall()
    
        for product in result_products: 
            product_response = {
                'name' : product[1],
                'img_saucer' : product[2],
                'description' : product[3],
                'price' : float(product[4]),
            }
            list_product.append(product_response)

        return {'products': list_product}
    except Exception as e:
        return {'Error' : str(e)}

@product_router.post('/product/add')
def create_product(product:Product):
    try:
        new_product = {
            'name': product.name,
            'img_saucer': product.img_saucer,
            'description': product.description,
            'price': product.price,
            'menu_id': product.menu_id,
        }
        result_product = conn.execute(select(products).where(products.c.name == new_product['name'])).first()
        if result_product == None:
            conn.execute(products.insert(), new_product)
            return {'Success' : 'Producto creado correctamente'}       
        else:
            return {'Error': 'El producto ya existe'}
    except Exception as e:
        return {'Error' : str(e)}

@product_router.put('/product/update')
def update_product(product_update : ProductUpdate):
    try:
        update = {
            'name': product_update.name,
            'img_saucer': product_update.img_saucer,
            'description': product_update.description,
            'price': product_update.price
        }
        conn.execute(products.update().where(products.c.id == product_update.id), update)
        return {'success': 'Producto actualizado'}
    except Exception as e:
        return {'Error' : str(e)}

@product_router.delete('/product/delete/{id_product}')
def delete_product(id_product:int):
    try:
        conn.execute(products.delete().where(products.c.id== id_product))
        return {'Success' : 'Producto eliminado'}
    except Exception as e:
        return {'Error': str(e)}
        
