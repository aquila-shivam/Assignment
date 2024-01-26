# Task

This is a curd django application 

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed
- pip package manager installed

## Getting Started

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/your-repo.git
    cd your-repo
    ```

2. **Set up a virtual environment:**

    ```bash
    python -m venv env
    ```

3. **Activate the virtual environment:**

    - On Windows:

        ```bash
        .\env\Scripts\activate
        ```

    - On macOS/Linux:

        ```bash
        source env/bin/activate
        ```

4. **Install project dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

5. **Apply database migrations:**

    ```bash
    python manage.py migrate
    ```

6. **Create a superuser for accessing the admin panel:**

    ```bash
    python manage.py createsuperuser
    ```

7. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

    The API will be accessible at [http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api/).

## API Endpoints

### List all tasks

- **URL:** `/api/tasks/`
- **Method:** `GET`

### Retrieve a single task by ID

- **URL:** `/api/tasks/{id}/`
- **Method:** `GET`

### Create a new task

- **URL:** `/api/tasks/`
- **Method:** `POST`

### Update an existing task

- **URL:** `/api/tasks/{id}/`
- **Method:** `PUT`

### Delete a task

- **URL:** `/api/tasks/{id}/`
- **Method:** `DELETE`

## Authentication

Token-based authentication is required to perform CRUD operations. Obtain a token by making a POST request to `/auth/token/login/`.

## Testing

Run unit tests using:

```bash
python manage.py test
