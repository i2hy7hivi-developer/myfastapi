# myfastapi
# 🧠 FastAPI Task Manager API

A secure, scalable, and JWT-authenticated REST API for managing user-specific tasks, built using **FastAPI**, **SQLAlchemy**, and **MySQL/MariaDB**.

---

## 🚀 Features

- 🔐 User registration & login with JWT authentication
- 🧾 Passwords hashed using `passlib`
- ✅ Fully authenticated CRUD operations for tasks
- 📎 Tasks are owned by users (foreign key relationship)
- 📂 Clean, modular folder structure (industry standard)
- ⚙️ `.env` for configuration

---

## 🏗️ Tech Stack

- **FastAPI** (web framework)
- **SQLAlchemy** (ORM)
- **MySQL/MariaDB** (database)
- **JWT (python-jose)** (authentication)
- **Pydantic** (schema validation)
- **Uvicorn** (ASGI server)

---

## 📁 Project Structure

app/
├── crud/ # DB logic
├── database/ # DB connection
├── models/ # SQLAlchemy models
├── routers/ # Route handlers
├── schemas/ # Pydantic schemas
├── utils/ # Auth, hashing, token logic
├── main.py # Entry point
.env
README.md


---

## 🔐 Authentication

- Uses **JWT** to protect routes
- Tokens include `user_id` and expire in 60 minutes
- No session or DB storage of tokens (stateless)

---

## 🧪 API Endpoints

### 🔑 Auth

| Method | Endpoint            | Description         |
|--------|---------------------|---------------------|
| POST   | `/api/auth/register` | Register new user  |
| POST   | `/api/auth/login`    | Login & get token  |

### 📝 Tasks

| Method | Endpoint         | Auth | Description        |
|--------|------------------|------|--------------------|
| GET    | `/api/tasks`      | ✅   | Get all user tasks |
| POST   | `/api/tasks`      | ✅   | Create task        |
| GET    | `/api/tasks/{id}` | ✅   | Get task by ID     |
| PUT    | `/api/tasks/{id}` | ✅   | Update task        |
| DELETE | `/api/tasks/{id}` | ✅   | Delete task        |

> All task endpoints require the `Authorization: Bearer <token>` header.

---

## 🛠️ Setup

```bash
git clone <repo>
cd <project>
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # or create your own .env
uvicorn app.main:app --reload

✅ To Do
 Alembic migrations

 Pagination & search

 Task filtering (status, dates)

 Refresh tokens / logout

 Dockerize the project


---

Let me know if you'd like to [add example API responses](f) or [document your schemas with Swagger](f).
