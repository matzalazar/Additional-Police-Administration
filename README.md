# Additional Police Administration

This project is a web application developed in Django to manage Additional Police Services in the Province of Buenos Aires. It streamlines the creation of schedules, shift management, and the generation of documentation for public and private entities. The system includes user role controls (Administrator and Manager), automatic validations for worked hours, and tools for reporting additional and extra hours. It incorporates a calendar view and allows for Excel report exports, minimizing human errors.

As this web application is specifically used by the Buenos Aires Provincial Police, the project's documentation has been written in Spanish to better align with its users. See [here](./docs/documentation.md) the full docs.

## Setup Instructions

Step 1: Clone the repository
First, clone the repository to your local machine:

```bash
$ git clone https://github.com/matzalazar/additional-police-administration.git
$ cd additional-police-administration
```

Step 2: Set up a virtual environment (optional but recommended)
It is recommended to use a virtual environment to avoid conflicts with other Python packages.

```bash
$ python -m venv venv
$ source venv/bin/activate   # On Windows: venv\Scripts\activate
```

Step 3: Install the required dependencies
Install all the project dependencies listed in the requirements.txt file:

```bash
$ pip install -r requirements.txt
```

Step 4: Create and migrate the database
Since the project uses a SQLite database for local testings, you'll need to generate the database and apply the necessary migrations. Run the following commands:

```bash
$ python manage.py migrate
```

Step 5: Create a superuser (optional)
To access the Django admin panel and manage the project, you can create a superuser:

```bash
$ python manage.py createsuperuser
```

Step 6: Run the development server
Start the Django development server to see the project in action:

```bash
$ python manage.py runserver
```

The application should now be running on http://127.0.0.1:8000/.