# 🌩️ CloudBase – Scalable On-Demand MariaDB Cloud Provisioning

**A lightweight Flask-based platform for deploying cloud-hosted MariaDB instances with custom specifications.**

---

📌 **Project Summary**

CloudBase is a streamlined cloud provisioning platform that allows users to create MariaDB instances by selecting desired specifications such as storage, CPU count, server region, and custom domain. Upon submitting a request, a MariaDB instance is automatically provisioned and credentials are provided via the user dashboard. The platform is built using Flask, and user authentication is handled securely through Flask-Login.
گ

🚀 Key Features

    🔐 Authentication System
    User login and registration with session management via Flask-Login.

    📄 Custom Order Interface
    Interactive UI for selecting storage, CPU, region, and domain.

    ⚙️ Automated Database Provisioning
    On form submission, a MariaDB database is created and assigned to the user.

    🖥️ User Dashboard
    Displays all order specifications and connection credentials.

    🧱 Clean, Modular Architecture
    Organized Flask project structure for scalability and maintainability.

🖼️ Pages Overview
Page	URL Route	Description
Home	/	Database order form
Login	/login	User login interface
Register	/register	New user registration
Dashboard	/dashboard	View ordered resources and DB info
🧭 Tech Stack

    Backend: Python (Flask)

    Authentication: Flask-Login

    Database Engine: MariaDB (or compatible MySQL)

    Frontend: HTML5, CSS3

    Others: Werkzeug, Jinja2

📁 Project Structure

CloudBase/
├── app.py           # Main application
├── models.py        # Database models and schema
├── utils.py         # Utility functions
├── static/          # CSS, JS, and assets
├── templates/       # HTML templates
└── README.md        # Project documentation

⚙️ Installation & Usage
Prerequisites:

    Python 3.7+

    MariaDB or MySQL installed and accessible

Setup Instructions:

# Clone the repository
git clone https://github.com/FatemehVejdani/CloudBase.git
cd CloudBase

# Install dependencies
pip install -r requirements.txt

# Run the Flask app
python app.py

Open your browser and navigate to http://localhost:5000.
⚠️ Known Limitations

    User-selected resources (CPU, storage) are not enforced at the system level.

    Admin panel not yet implemented.

    Database access control is simplistic and intended for prototype use only.

📬 Contact & Contribution

Contributions, bug reports, and suggestions are highly welcome.

    GitHub: @FatemehVejdani

    Open an Issue / Submit a Pull Request

<div align="center">

Crafted with care by Fatemeh Vejdani
</div>
