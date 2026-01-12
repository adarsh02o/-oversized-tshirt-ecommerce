# Oversized T-Shirts E-Commerce Store

A Django-based e-commerce website specializing in oversized t-shirts with user authentication and admin dashboard.

## 🚀 Features

- **User Authentication**: Login, registration, and user profiles
- **Admin Dashboard**: Product management with inventory tracking
- **Product Catalog**: Browse oversized t-shirts with detailed views
- **Responsive Design**: Modern UI built with Bootstrap 5
- **Indian Rupee Pricing**: Localized currency display
- **Media Management**: Image upload for products

## 📦 Installation

### Prerequisites
- Python 3.8+
- Git

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <your-repository-url>
   cd windsurf-project
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # Mac/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create superuser (admin)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Main Store: http://127.0.0.1:8000/
   - Admin Panel: http://127.0.0.1:8000/admin/
   - Admin Dashboard: http://127.0.0.1:8000/accounts/admin-dashboard/

## 🔑 Default Admin Credentials

If you want to use the pre-configured admin account:
- Username: `admin`
- Password: `admin123`

## 🛠️ Project Structure

```
windsurf-project/
├── accounts/                 # User authentication app
│   ├── forms.py             # Custom registration form
│   ├── views.py             # Login, signup, admin dashboard views
│   └── templates/           # Authentication templates
├── products/                # Product management app
│   ├── models.py            # TShirt model
│   ├── views.py             # Product display views
│   └── templates/           # Product templates
├── tshirt_ecommerce/        # Main Django project
│   ├── settings.py          # Django settings
│   └── urls.py              # Main URL configuration
├── media/                   # Product images
├── static/                  # Static files (CSS, JS)
├── requirements.txt         # Python dependencies
└── manage.py               # Django management script
```

## 🎯 Usage

### For Regular Users:
1. Visit the home page to browse products
2. Register for an account or login
3. View product details and pricing

### For Admin Users:
1. Login with admin credentials
2. Access the admin dashboard to manage products
3. Add/edit t-shirts with pricing and inventory
4. Use Django admin for advanced management

## 🌐 Deployment

This project can be deployed on various platforms:

### Heroku
1. Install Heroku CLI
2. Login to Heroku: `heroku login`
3. Create app: `heroku create your-app-name`
4. Add buildpacks: `heroku buildpacks:set heroku/python`
5. Push to Heroku: `git push heroku main`

### PythonAnywhere
1. Create a PythonAnywhere account
2. Upload your code
3. Configure web app
4. Install requirements and migrate

### VPS/Dedicated Server
1. Install Python and required packages
2. Configure web server (Nginx/Apache)
3. Set up Gunicorn or uWSGI
4. Configure SSL certificate

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Commit and push to your branch
5. Create a Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 📞 Support

For support and questions, please open an issue in the GitHub repository.

---

**Built with Django 6.0.1, Bootstrap 5, and lots of ❤️**
