# Bang Stream Backend

This is the backend repository for our Streaming Platform with Real-Time Chat application built with Django, Django REST Framework, and Django Channels.

## Tech Stack

- **Core**: Django 4.2 with Django REST Framework
- **WebSockets**: Django Channels for real-time communication
- **Authentication**: Django's auth system with djangorestframework-simplejwt
- **Real-Time Layer**: Django Channels with Redis channel layer
- **Database**: PostgreSQL
- **ORM**: Django ORM

## Getting Started

### Setup with Docker

1. Clone this repository
2. Create a `.env` file based on `.env.example`
3. Run the application: