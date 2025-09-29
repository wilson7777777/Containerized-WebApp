# 📦 Containerized Web Application

A **modern, full-stack web application** built with a **multi-tier architecture** and containerized using **Docker Compose**.  
This project demonstrates **best practices** for separation of concerns and **scalable deployment**.

---

## 🚀 Key Technologies  

This application is composed of **five distinct, containerized services**:

| Component        | Technology       | Key Details                                                                 |
|------------------|------------------|-----------------------------------------------------------------------------|
| **Backend API**  | 🐍 **Python (Flask)** | RESTful API handling business logic, database, and cache connections.       |
| **Database**     | 🐘 **PostgreSQL**     | Reliable relational database, initialized via `database/init.sql`.          |
| **Cache/Broker** | ⚡ **Redis**          | Provides high-speed caching and message queuing.                           |
| **Frontend**     | ⚛️ **Node.js / React** | Client-side app (React), built from `frontend/src/` and served via Node.js. |
| **Reverse Proxy**| 🌐 **Nginx**         | Routes traffic to frontend or API, acts as the single entry point.          |
| **Orchestration**| 🐳 **Docker Compose** | Builds and manages the full stack with a single command.                   |

---

## 💻 Architecture Overview  

This project uses a **five-container microservice pattern**, orchestrated via `docker-compose.yml`:

    frontend → served by Nginx
    api      → Flask backend (talks to db + redis)
    db       → PostgreSQL database
    redis    → Redis cache/broker
    nginx    → Reverse proxy, exposes port 80

📊 **High-Level Flow**:  
`User → Nginx → Frontend/API → Database + Redis`

---

## ▶️ Getting Started  

### ✅ Prerequisites  
Make sure you have installed:

- [**Docker**](https://docs.docker.com/get-docker/)  
- [**Docker Compose**](https://docs.docker.com/compose/) (bundled with Docker Desktop)

---

### ⚡ Installation & Run  

Clone the repository:

    git clone https://github.com/wilson7777777/Containerized-WebApp.git
    cd Containerized-WebApp

Build and start the application (first run may take a few minutes):

    docker-compose up --build -d

Access the app in your browser:  
👉 [http://localhost:80](http://localhost:80)

---

### 🛑 Stopping & Cleanup  

To stop and remove containers, networks, and volumes:

    docker-compose down

---

## ⚙️ Configuration & Environment Variables  

Sensitive data and service communication are managed with **environment variables** in `docker-compose.yml`.

| Service  | Variable             | Value     | Purpose                                           |
|----------|----------------------|-----------|---------------------------------------------------|
| **db**   | `POSTGRES_PASSWORD`  | postgres  | Sets the superuser password for PostgreSQL.       |
| **api**  | `DB_HOST`            | db        | Internal Docker hostname for the database.        |
| **api**  | `DB_PASSWORD`        | postgres  | Password for API to connect to PostgreSQL.        |
| **api**  | `REDIS_HOST`         | redis     | Internal Docker hostname for Redis service.       |

---

## 🐳 Docker Compose File (Simplified)

    version: '3.8'

    services:
      db:
        build: ./database
        environment:
          POSTGRES_PASSWORD: postgres

      redis:
        image: redis:alpine

      api:
        build: ./api
        depends_on:
          - db
          - redis
        environment:
          DB_HOST: db
          DB_PASSWORD: postgres
          REDIS_HOST: redis

      frontend:
        build: ./frontend
        depends_on:
          - api
        ports:
          - "3000:3000" # Internal port for frontend

      nginx:
        image: nginx:alpine
        ports:
          - "80:80" # External port exposed
        volumes:
          - ./nginx/nginx.conf:/etc/nginx/nginx.conf
        depends_on:
          - api
          - frontend

---

## 📂 Project Structure  

| Directory/File        | Purpose                          | Tech/Files |
|-----------------------|----------------------------------|------------|
| **api/**              | Backend REST API                 | `app.py`, `requirements.txt`, `Dockerfile` |
| **database/**         | PostgreSQL setup/config          | `Dockerfile`, `init.sql` |
| **frontend/**         | React frontend app               | `src/`, `public/`, `package.json`, `Dockerfile` |
| **nginx/**            | Reverse proxy config             | `nginx.conf` |
| **docker-compose.yml**| Orchestration of all services    | Docker Compose |

---

## 🤝 Contributing  

1. 🍴 **Fork** the repository  
2. 🌿 **Create your feature branch**  
   
       git checkout -b feature/AmazingFeature

3. 💾 **Commit your changes**  
   
       git commit -m 'Add some AmazingFeature'

4. ⬆️ **Push to the branch**  
   
       git push origin feature/AmazingFeature

5. 🔀 **Open a Pull Request**  

---

✨ Built with **love ❤️, containers 🐳, and coffee ☕**
