# FreelancerHub - Mini Freelance Marketplace

FreelancerHub is a full-stack Flask application that connects clients with freelancers.

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- pip

### Local Setup
1. **Clone the repository** (if applicable) or navigate to the project folder.
2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Initialize the Database**:
   ```bash
   set FLASK_APP=run.py
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```
5. **Run the application**:
   ```bash
   python run.py
   ```
6. Access the app at `http://127.0.0.1:5000`.

## 📂 Project Structure
- `app/`: Main application package.
  - `auth.py`: Blueprint for user authentication.
  - `routes.py`: Blueprint for dashboard, projects, and bids.
  - `models.py`: SQLAlchemy database models.
  - `forms.py`: Flask-WTF form classes.
- `config.py`: Environment and app configurations.
- `run.py`: Entry point for starting the server.

## 🛠 Features
- **Client**: Post projects, view bids, and accept freelancers.
- **Freelancer**: Browse open projects, submit proposals with custom pricing.
- **Unified Dashboard**: Real-time status tracking for all roles.
- **Responsive UI**: Built with Bootstrap 5.

## 🚢 Deployment Guide

### Render / Railway (Recommended)
1. **Connect your GitHub** to Render or Railway.
2. **Setup**:
   - Environment: `Python`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn run:app` (Note: Add `gunicorn` to requirements.txt for production)
3. **Environment Variables**:
   - `SECRET_KEY`: A long random string.
   - `DATABASE_URL`: Your PostgreSQL connection string.

### PythonAnywhere
1. Upload your code to the "Files" tab.
2. Setup a Virtualenv and install requirements.
3. Configure the WSGI file to point to `run.py`.

## ✨ Future Improvements
- **Escrow System**: Secure payments.
- **Messenging**: Real-time chat between clients and freelancers.
- **Ratings & Reviews**: Feedback system for both roles.
- **Notification System**: Email alerts for new bids or project assignments.
