from flask import  jsonify, request
from models import Supplier, Product

def get_products():
    # Get query parameters for filtering (e.g., by brand or category)
    brand = request.args.get('brand', default=None)
    category = request.args.get('category', default=None)
    
    query = Product.query
    
    if brand:
        query = query.filter(Product.brand.ilike(f"%{brand}%"))
    if category:
        query = query.filter(Product.category.ilike(f"%{category}%"))
    
    products = query.all()
    product_list = [
        {
            "id": product.id,
            "name": product.name,
            "brand": product.brand,
            "price": product.price,
            "category": product.category,
            "description": product.description,
            "supplier": product.supplier.name
        }
        for product in products
    ]
    
    return jsonify(product_list)

def get_suppliers():
    # Get query parameters for filtering (e.g., by product category)
    category = request.args.get('category', default=None)
    
    query = Supplier.query
    
    if category:
        query = query.filter(Supplier.product_categories.ilike(f"%{category}%"))
    
    suppliers = query.all()
    supplier_list = [
        {
            "id": supplier.id,
            "name": supplier.name,
            "contact_info": supplier.contact_info,
            "product_categories": supplier.product_categories
        }
        for supplier in suppliers
    ]
    
    return jsonify(supplier_list)
