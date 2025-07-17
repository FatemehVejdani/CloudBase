# 🌩️ CloudBase – Scalable On-Demand MariaDB Cloud Provisioning

**CloudBase is a lightweight Flask-based platform that enables users to deploy on-demand, cloud-hosted MariaDB instances with custom specifications.**

---

## 📌 Project Overview

CloudBase streamlines the process of creating and managing MariaDB databases by allowing users to configure their instance's storage, CPU, server location, and custom domain. Once a request is submitted, a MariaDB instance is automatically provisioned, and access credentials are shown in the user dashboard.

> **Tech Highlights:** Built with Flask, secured with Flask-Login, and architected for modular scalability.

---

## 🚀 Key Features

- 🔐 **Secure Authentication**  
  User login and registration with session handling via Flask-Login.

- 📄 **Custom Order Interface**  
  Interactive web form to configure storage size, CPU count, region, and domain.

- ⚙️ **Automated Provisioning**  
  MariaDB databases are automatically created upon form submission.

- 🖥️ **User Dashboard**  
  Displays all orders with their specifications and connection credentials.

- 🧱 **Clean & Modular Codebase**  
  Structured Flask project, easy to scale and maintain.

---

## 🖼️ Pages Overview

## 🖼️ Pages Overview

| Page       | URL Route     | Description                                                             |
|------------|---------------|-------------------------------------------------------------------------|
| Home       | `/`           | Form for submitting custom MariaDB instance requests                    |
| Login      | `/login`      | User login page for accessing the dashboard                             |
| Sign Up    | `/signup`     | New user registration page                                              |
| Dashboard  | `/dashboard`  | Displays all ordered databases along with their specifications & details |

---

## 🧭 Tech Stack

- **Backend:** Python (Flask)  
- **Authentication:** Flask-Login  
- **Database Engine:** MariaDB (or MySQL-compatible)  
- **Frontend:** HTML5, CSS3 (with Jinja2 templates)  
- **Others:** Werkzeug, Jinja2  


---

## ⚙️ Installation & Usage

### ✅ Prerequisites

- Python 3.7 or higher  
- MariaDB or MySQL installed and running

### 📦 Setup Instructions

```bash
# Clone the repository
git clone https://github.com/FatemehVejdani/CloudBase.git
cd CloudBase

# Install Python dependencies
pip install -r requirements.txt

# Run the Flask app
python app.py


