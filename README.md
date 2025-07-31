# README.md

## Chat Application Overview

This project implements a microservices-based chat application, comprising three core services:

1. **Profile Service**: Manages user profiles and metadata.
2. **Auth Service**: Handles authentication, authorization, and session management.
3. **Chat Service**: Manages real-time messaging, message persistence, and delivery.

All services are containerized (Docker) and deployed in a Kubernetes cluster. Services communicate over HTTP/REST for management operations and WebSocket/gRPC for chat streaming.

---

## High-Level Design (HLD)

### Architecture Diagram

```
+-------------+      +-------------+      +-------------+
|             |      |             |      |             |
|  Frontend   | <--> | API Gateway | <--> | Auth Service|
|  (React)    |      +-------------+      +-------------+
|             |             |
+-------------+             |
                            v
                     +-------------+
                     | Profile     |
                     | Service     |
                     +-------------+
                            |
                            v
                     +-------------+
                     | Chat Service|
                     +-------------+
```

* **Frontend**: SPA built in React. Connects to API Gateway via HTTPS and to Chat Service via WebSocket.
* **API Gateway**: Routes requests to Auth, Profile, and Chat services; performs rate limiting and JWT validation.
* **Auth Service**: Issues JWT tokens, validates credentials, supports OAuth2.
* **Profile Service**: CRUD operations on `UserProfile` (name, avatar, status, preferences).
* **Chat Service**: WebSocket server; persists messages in NoSQL (e.g., MongoDB) and publishes events.

### Component Roles

#### Profile Service

* **Responsibility**: Create, read, update, delete user profiles.
* **Tech Stack**: Python FastAPI, PostgreSQL.
* **Endpoints**: `/profiles`, `/profiles/{id}`.
* **Auth Guard**: Validates incoming JWT via Auth Service.
* **Data Model**:

  ```yaml
  UserProfile:
    id: UUID
    username: string
    displayName: string
    avatarUrl: string
    statusMessage: string
    createdAt: timestamp
    updatedAt: timestamp
  ```

#### Auth Service

* **Responsibility**: Authenticate users (login, logout), issue/refresh JWT.
* **Tech Stack**: Node.js, Express, Redis (for session blacklisting).
* **Endpoints**: `/auth/login`, `/auth/refresh`, `/auth/logout`.
* **Security**: Password hashing (bcrypt), OAuth2 integration.

#### Chat Service

* **Responsibility**: Real-time messaging via WebSocket; message persistence; offline delivery.
* **Tech Stack**: Go, gRPC/WebSocket, MongoDB, Kafka for event streaming.
* **Features**:

  * User connects via WebSocket. JWT validated at handshake.
  * Pub/Sub model: chat topics per room.
  * Message store in MongoDB; last 100 messages returned on connect.

---

# profile service
**Database Schema (MySQL)**

Below is a documented schema for the `user_profiles` table, including column definitions, data types, constraints, and indexes.

| Column         | Data Type         | Constraints                                                     | Description                                         |
|----------------|-------------------|-----------------------------------------------------------------|-----------------------------------------------------|
| `id`           | `CHAR(36)`        | `NOT NULL`, `PRIMARY KEY`                                        | UUID for each user (e.g., `550e8400-e29b-41d4-a716-446655440000`) |
| `username`     | `VARCHAR(50)`     | `NOT NULL`, `UNIQUE`, indexed (`idx_username`)                  | Unique login identifier                             |
| `display_name` | `VARCHAR(100)`    | `NOT NULL`                                                      | User’s chosen display name                          |
| `avatar_url`   | `VARCHAR(255)`    |                                                                  | Link to the user’s avatar image                     |
| `status_message`| `VARCHAR(255)`   |                                                                  | Short status or bio text                            |
| `created_at`   | `DATETIME`        | `NOT NULL`, `DEFAULT CURRENT_TIMESTAMP`                         | Record creation timestamp                           |
| `updated_at`   | `DATETIME`        | `NOT NULL`, `DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP` | Last update timestamp                               |

```sql
CREATE TABLE user_profiles (
  id CHAR(36) NOT NULL PRIMARY KEY,
  username VARCHAR(50) NOT NULL UNIQUE,
  display_name VARCHAR(100) NOT NULL,
  avatar_url VARCHAR(255),
  status_message VARCHAR(255),
  created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  INDEX idx_username (username)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
```
