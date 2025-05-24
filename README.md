# AutoHunt 🚗

![AutoHunt Banner](https://github.com/user-attachments/assets/aa14d770-9976-4d73-bf6a-ae3d790340ab) 
![Screenshot 2025-05-23 223846](https://github.com/user-attachments/assets/6d78184f-9d37-413d-8f37-cbf74fbff8ac)
![Screenshot 2025-05-23 223905](https://github.com/user-attachments/assets/5439d3b5-2454-4f6b-97dc-55f0eba0cf74)
![Screenshot 2025-05-23 224117](https://github.com/user-attachments/assets/92546502-d21f-421d-8399-095faf08042e)

*A modern web app to track vehicles you're considering purchasing*

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.3.x-green.svg)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-purple.svg)](LICENSE)

## 🌟 Features

### Vehicle Tracking
- 📅 Year, Make, Model
- 💰 Price & Mileage
- ⚙️ Engine specs (cylinders, displacement)
- 🚗 Drivetrain type
- 🔗 Listing & Carfax links

### Organization Tools
- 🏷️ Status tracking (Available → Called → Viewed → Sold)
- 🖼️ Image uploads with gallery view
- 🔍 Advanced filtering & sorting
- 📱 Fully responsive design

### User Experience
- 🌙 Dark/Light mode toggle
- 🎨 Purple-themed UI
- 📊 Dashboard view
- 🚀 Quick actions

## 🛠️ Tech Stack

| Component       | Technology |
|----------------|-----------|
| **Frontend**   | Bootstrap 5, JavaScript, CSS3 |
| **Backend**    | Python 3, Flask |
| **Database**   | SQLite (with SQLAlchemy ORM) |
| **Deployment** | Replit/Heroku/Render ready |

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip package manager

### Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/autohunt.git
cd autohunt

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt

# Initialize database
flask db upgrade

# Run the application
python app.py
