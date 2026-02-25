from app import create_app, db
from app.models import User

def seed_admin():
    app = create_app()
    with app.app_context():
        # Check if admin already exists
        admin_email = "admin@freelancerhub.com"
        existing_admin = User.query.filter_by(email=admin_email).first()
        
        if existing_admin:
            print(f"Admin already exists: {admin_email}")
            return

        admin = User(
            name="System Admin",
            email=admin_email,
            role="admin",  # Can be anything, is_admin is the trigger
            is_admin=True
        )
        admin.set_password("admin123")
        db.session.add(admin)
        db.session.commit()
        print(f"Admin created successfully!")
        print(f"Email: {admin_email}")
        print(f"Password: admin123")

if __name__ == "__main__":
    seed_admin()
