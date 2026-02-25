import sys
from app import create_app, db
from app.models import User

def make_admin(email):
    app = create_app()
    with app.app_context():
        user = User.query.filter_by(email=email).first()
        if user:
            user.is_admin = True
            db.session.commit()
            print(f"Success: {email} is now an admin.")
        else:
            print(f"Error: User with email {email} not found.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        make_admin(sys.argv[1])
    else:
        print("Usage: python make_admin.py <email>")
