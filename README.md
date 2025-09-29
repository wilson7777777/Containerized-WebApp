# Containerized-WebApp: [PROJECT PURPOSE - e.g., Simple Task Manager]

This repository contains a modern, full-stack web application built with a multi-tier architecture and containerized using **Docker Compose**. It demonstrates best practices for separation of concerns and scalable deployment.

## 🚀 Key Technologies

This application is composed of four distinct, containerized services:

| Component | Technology | Key Details |
| :--- | :--- | :--- |
| **Backend API** | **Python** (Flask) | A RESTful API built with **Flask**, managing business logic and connecting to the database. Dependencies are managed via `requirements.txt`. |
| **Frontend** | **Node.js/React** (or similar) | The client-side application, built using a Node.js ecosystem (as indicated by `package.json` and `src/`). |
| **Database** | **PostgreSQL** | A reliable relational database, configured to initialize schema and data using `database/init.sql`. |
| **Reverse Proxy** | **Nginx** | Used to serve the static frontend assets and securely route API calls from the client to the backend container. |
| **Orchestration** | **Docker** & **Docker Compose** | Used to define, build, and run the entire multi-container application stack with a single command. |

---

## 💻 Architecture Overview

The entire application stack is defined in `docker-compose.yml` and structured as follows:

1.  **`frontend`**: Serves the client-side user interface.
2.  **`api`**: Receives requests, processes data, and interacts with the database.
3.  **`database`**: Stores all application data.
4.  **`nginx`**: The entry point, routing requests to either the `frontend` (for the page) or the `api` (for data requests).

---

## ▶️ Getting Started

### Prerequisites

You must have the following software installed:

* **Docker**
* **Docker Compose** (Often bundled with Docker Desktop)

### Installation and Run

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/wilson7777777/Containerized-WebApp.git
    cd Containerized-WebApp
    ```
2.  **Build and Start the Application:**
    Use Docker Compose to build the required images and start all four services in detached mode (`-d`). This step may take a few minutes for initial image building.
    ```bash
    docker-compose up --build -d
    ```

3.  **Access the Application:**
    The application will be accessible via your browser once the services are running:

    $$\text{http://localhost:[PORT DEFINED IN docker-compose.yml]}$$

    *(Please replace `[PORT DEFINED IN docker-compose.yml]` with the actual port used by your Nginx service, e.g., `3000` or `80`.)*

### Stopping and Cleanup

To stop and remove all running containers, associated networks, and temporary volumes:

```bash
docker-compose down
