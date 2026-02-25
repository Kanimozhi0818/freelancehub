from app import create_app, db
from app.models import User, Project
from datetime import datetime, timedelta

def seed_demo_data():
    app = create_app()
    with app.app_context():
        # 1. Create a Test Client
        client_email = "client@example.com"
        client = User.query.filter_by(email=client_email).first()
        
        if not client:
            client = User(
                name="Demo Client",
                email=client_email,
                role="client",
                bio="A company looking for talented developers.",
                is_admin=False
            )
            client.set_password("client123")
            db.session.add(client)
            db.session.commit()
            print(f"Client created: {client_email}")
        else:
            print(f"Client already exists: {client_email}")

        # 2. Create a Test Project
        project_title = "Modern Flask Web Application"
        existing_project = Project.query.filter_by(title=project_title).first()
        
        if not existing_project:
            project = Project(
                title=project_title,
                description="Looking for an expert to build a freelance marketplace using Flask and Bootstrap.",
                budget=1500.0,
                deadline=datetime.utcnow() + timedelta(days=14),
                client=client,
                status="open"
            )
            db.session.add(project)
            db.session.commit()
            print(f"Project created: {project_title}")
        else:
            print(f"Project already exists: {project_title}")

if __name__ == "__main__":
    seed_demo_data()
