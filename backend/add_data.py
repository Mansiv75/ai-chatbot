from app import app
from models import db
import random
from models import Supplier, Product

# Ensure we are inside the application context
with app.app_context():
    # Sample supplier data
    db.create_all()
    suppliers = [
        Supplier(name="ABC Electronics", contact_info="123-456-7890", product_categories="Laptops, Phones"),
        Supplier(name="XYZ Tech", contact_info="987-654-3210", product_categories="Tablets, Accessories"),
        Supplier(name="Gadget World", contact_info="555-555-5555", product_categories="Smartwatches, Headphones"),
        Supplier(name="SuperTech Solutions", contact_info="222-333-4444", product_categories="Monitors, Keyboards"),
        Supplier(name="Home Essentials", contact_info="666-777-8888", product_categories="Smart Home Devices, Speakers"),
        Supplier(name="NextGen Gadgets", contact_info="999-111-2222", product_categories="Gaming Consoles, VR Headsets"),
        Supplier(name="Elite Electronics", contact_info="444-555-6666", product_categories="Cameras, Drones"),
        Supplier(name="MegaMart Tech", contact_info="777-888-9999", product_categories="Printers, Routers"),
        Supplier(name="FutureWare", contact_info="111-222-3333", product_categories="Wearables, Smart Glasses"),
        Supplier(name="Innovatech", contact_info="333-444-5555", product_categories="AI Assistants, IoT Devices")
    ]

    # Add all suppliers and commit
    db.session.add_all(suppliers)
    db.session.commit()

    print("✅ 10 sample suppliers added successfully!")

    # add_sample_data.py


    # List of sample product names and brands
    product_names = [
        "Laptop X", "Smartphone Pro", "Wireless Earbuds", "Smartwatch", "Tablet Z", "Camera 3000", "Smart Speaker", 
        "Gaming Console", "LED TV", "Bluetooth Headphones", "Portable Charger", "Home Security Camera", "Laptop Pro", 
        "Smartphone Lite", "Action Camera", "Smart Thermostat", "Fitness Tracker", "E-reader", "Digital Camera", 
        "Drone Max", "VR Headset", "Smart Light Bulbs", "Soundbar", "Gaming Mouse", "Mechanical Keyboard", 
        "External SSD", "Gaming Monitor", "Projector", "Home Theater System", "Network Router", "Memory Card"
    ]

    brands = [
        "Brand A", "Brand B", "Brand C", "Brand D", "Brand E"
    ]

    categories = [
        "Laptops", "Phones", "Audio", "Wearables", "Cameras", "Gaming", "Home Appliances", "Computing"
    ]

    # Create and add 50 products with random data
    for i in range(1, 51):
        name = random.choice(product_names)
        brand = random.choice(brands)
        category = random.choice(categories)
        price = round(random.uniform(50, 2000), 2)  # Random price between 50 and 2000
        description = f"Description for {name}"
        supplier = random.uniform(1,11)  # Randomly select a supplier from the database for each product

        # Create a product and add it to the session
        product = Product(
            name=name,
            brand=brand,
            price=price,
            category=category,
            description=description,
            supplier_id=supplier.id
        )
        db.session.add(product)

    # Commit the changes to the database
    db.session.commit()

    print("50 sample products added successfully!")