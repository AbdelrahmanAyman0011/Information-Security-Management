# Information-Security-Management

## Abdelrahman Ayman Saad Abdelhalim Mohamed

**ID:** 2205033

## API for User Authentication and Product Management

This project is a RESTful API built with Flask that provides user authentication and product management functionalities. The API includes features such as user signup, login, JWT authentication, and CRUD operations for products.

---

## 🛠️ Requirements

- Python 3.x
- MySQL Database
- Flask and required dependencies (See `requirements.txt`)

## 📦 Installation

1. Clone the repository:
   ```sh
   git clone <repository_url>
   cd Information-Security-Management/task2/API
   ```
2. Create a virtual environment and activate it:
   ```sh
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## 🛠️ Database Setup

1. Make sure MySQL is running and create a database:
   ```sql
   CREATE DATABASE infosec_db;
   ```
2. Update the database connection string in `app.config`:
   ```python
   app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/infosec_db'
   ```
3. Initialize the database tables:
   ```sh
   flask db upgrade
   ```

## 🚀 Running the Application

1. Start the Flask app:
   ```sh
   python app.py
   ```
2. The API will be available at: `http://127.0.0.1:5000/`

## 📌 API Endpoints

### 🧑 User Authentication

- **Signup:** `POST /signup`
- **Login:** `POST /login`
- **Update User (Protected):** `PUT /users/<id>`

### 📦 Product Management

- **Add Product (Protected):** `POST /products`
- **Get All Products:** `GET /products`
- **Get Product by ID:** `GET /products/<pid>`
- **Update Product (Protected):** `PUT /products/<pid>`
- **Delete Product (Protected):** `DELETE /products/<pid>`

## 🔑 JWT Authentication

- The API uses JSON Web Tokens (JWT) for authentication.
- Include the token in requests using the `Authorization: Bearer <token>` header.

## 🛠️ Environment Variables

Create a `.env` file and define:

```env
JWT_SECRET=your_secret_key
```

## 📄 License

This project is for educational purposes only. No license is provided.

## ✨ Author

- **Abdelrahman Ayman**

---

Happy Coding! 🚀
