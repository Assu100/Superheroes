from superhero_api import create_app, db
from superhero_api.models import Hero, Power  # Adjust the import based on your models

app = create_app()

# with app.app_context():
#     db.create_all()  # Create tables if not already created

#     # Now you can populate your database here
#     hero1 = Hero(name="Kamala Khan", super_name="Ms. Marvel")
#     db.session.add(hero1)
#     db.session.commit()

def seed_data():
    hero1 = Hero(name="Kamala Khan", super_name="Ms. Marvel")
    hero2 = Hero(name="Peter Parker", super_name="Spider-Man")
    
    power1 = Power(description="Super Strength")
    power2 = Power(description="Web-slinging")

    db.session.add_all([hero1, hero2, power1, power2])
    db.session.commit()
    print("Database seeded!")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Ensure tables exist
        seed_data()      # Seed the database
