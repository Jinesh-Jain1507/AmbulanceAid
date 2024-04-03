# Django Blog Website

Welcome to the Ambulance Booking System project! This system provides a convenient way for users to book ambulances near their location using their pincode. 
It offers a user-friendly interface for both patients and hospitals, allowing them to register, manage bookings, and track ambulance availability in real-time.
The Ambulance Booking System is a web application built using Django, a Python web framework. It serves as a centralized platform for ambulance booking, catering to the needs 
of patients and hospitals alike. Patients can quickly request ambulances based on their pincode, while hospitals can register and manage ambulance drivers to fulfill these requests efficiently.

## Features

- **Ambulance Booking**: Users can search and book various types of ambulances according to their needs near their location using their pincode.
- **User Registration**: Patients and hospitals can register accounts to access the booking system.
- **Real-time Availability**: Ambulance availability is updated in real-time, ensuring prompt response to booking requests.
- **Hospital Management**: Hospitals can manage ambulance drivers and track their availability and assigned tasks.
- **Patient Details**: Medical History and other relevant details of the patient are shared with the Ambulance drivers for better service.
- **Responsive Design**: Optimized for both desktop and mobile devices for seamless user experience.

## Technologies Used

- **Django**: Python web framework for building the backend of the website.
- **HTML/CSS**: Frontend markup and styling.
- **Bootstrap**: Frontend framework for responsive design.
- **SQLite**: Database system for storing blog posts, comments, and user data.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Jinesh-Jain1507/AmbulanceAid.git

2. **Navigate to the project directory**:
   ```bash
   cd Ambulance aid

3. **Create a virtual environment (optional but recommended)**:
   ```bash
   python -m venv env

4. **Activate the virtual environment**:

   - **On Windows:
     ```bash
     .\env\Scripts\activate
   - **On macOS/Linux:
     ```bash
     source env/bin/activate

5. Install python (https://www.python.org/downloads/) then install django:
   ```bash
   pip install django

6. Create the database schema
   ```bash
   python manage.py migrate

7. Create a superuser (admin user) for accessing the admin panel:
   ```bash
   python manage.py createsuperuser

8. Start the development server:
   ```bash
   python manage.py runserver

Open your web browser and navigate to http://localhost:8000 to access the website.


