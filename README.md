# 🛒 Django Ecommerce Project (Advanced Version – Django 5.2.7)

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Django](https://img.shields.io/badge/Django-5.2.7-success?logo=django)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Status](https://img.shields.io/badge/Project%20Status-Active-brightgreen)
![Last Updated](https://img.shields.io/badge/Updated-October%2023%2C%202025%20|%202:14%20PM%20PKT-blue)

> 🗓️ **Last Updated:** October 23, 2025 | 2:14 PM (Pakistan Standard Time)  
> 🚀 *This project is regularly updated with new features.*

---

A **complete Django Ecommerce Website** built using **Django 5.2.7** and **Django REST Framework**, featuring modern authentication, product management, cart, checkout, and Stripe payment integration.  
Perfect for **students**, **beginner developers**, and anyone learning to build **real-world Django projects**.

---

## 🚀 Features

✅ **User Authentication**
- Register, login, logout, and manage profile  
- JWT or Session-based authentication  
- Role-based access (Admin, Seller, Customer)

✅ **Product Management**
- Add, update, delete, and list products  
- Category and brand filtering  
- Product image upload and search system  

✅ **Cart & Checkout**
- Add to cart, update quantity, remove items  
- Checkout with shipping details and order summary  

✅ **Payment Integration**
- Integrated **Stripe** for secure online payments  
- Test mode supported for development

✅ **Admin Dashboard**
- Manage products, orders, and users  
- Real-time order tracking  

✅ **REST API**
- Built with Django REST Framework (DRF)  
- API endpoints for all ecommerce operations  

✅ **Fully Modular Project Structure**
- Clean, reusable Django apps  
- Scalable for enterprise use  

---

## 🧩 Tech Stack

| Component | Technology |
|------------|-------------|
| Backend | Django 5.2.7 |
| API | Django REST Framework |
| Database | PostgreSQL / SQLite |
| Authentication | Django Auth / JWT |
| Frontend | HTML, CSS, JS (React optional) |
| Payment Gateway | Stripe |
| Deployment | Docker / Render / Railway / Vercel |

---

## ⚙️ Installation Guide

```bash
# 1️⃣ Clone the repository
git clone https://github.com/your-username/django-ecommerce-project.git
cd django-ecommerce-project

# 2️⃣ Create virtual environment
python -m venv venv
venv\Scripts\activate   # On Windows
source venv/bin/activate  # On Mac/Linux

# 3️⃣ Install dependencies
pip install -r requirements.txt

# 4️⃣ Apply migrations
python manage.py makemigrations
python manage.py migrate

# 5️⃣ Create superuser
python manage.py createsuperuser

# 6️⃣ Run server
python manage.py runserver
