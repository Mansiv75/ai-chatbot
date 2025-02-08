from views import *

def register_routes(app):
    app.add_url_rule('/products', view_func=get_products, methods=['GET'])
    app.add_url_rule('/suppliers', view_func=get_suppliers, methods=['GET'])
    app.add_url_rule('/products/brand/<brand>', view_func=get_products_by_brand, methods=['GET'])
    app.add_url_rule('/suppliers/category/<category>', view_func=get_suppliers_by_category, methods=['GET'])
    app.add_url_rule('/products/<int:product_id>', view_func=get_product_details, methods=['GET'])