from views import get_products, get_suppliers

def register_routes(app):
    app.add_url_rule('/api/products', view_func=get_products, methods=['GET'])
    app.add_url_rule('/api/suppliers', view_func=get_suppliers, methods=['GET'])
