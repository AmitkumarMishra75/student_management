# 🎓 Student Management System
A Student Management web application built using HTML, CSS, Python, and Django Framework. This project enables efficient management of student records by categorizing them into different streams, and it allows CRUD (Create, Read, Update, Delete) operations on student data in an interactive user interface.

# 🌟 Features
**Categorized Data:** <br>
-  Students are displayed in different pages based on their streams.
-  Details are displayed in a visually appealing card format.

**CRUD Operations:**<br>
-  **Add New Student:** Easily create and save new student records.
-  **Edit Student Data:** Update existing student information.
-  **Delete Student:** Remove outdated or unnecessary records.

**Dynamic User Interface:**<br>
-  A responsive design that enhances usability and aesthetics.

# 💻 Tech Stack
**Frontend**<br>
-  **HTML5:** Provides structure and layout.
-  **CSS3:** Ensures styling for an interactive UI.

**Backend**<br>
-  **Python:** For core backend functionality.
-  **Django Framework:** MVC-based backend for dynamic web development.

**Database**<br>
-  Django’s default SQLite database for storing student records.

# 📂 Project Structure

├── student_management/    # Main Django project folder  <br>
│   ├── settings.py        # Project settings  <br>
│   ├── urls.py            # URL configurations  <br>
│   └── wsgi.py            # WSGI application  <br>
├── app/                   # Application folder for student data management  <br>
│   ├── migrations/        # Database migrations  <br>
│   ├── templates/         # HTML files for views  <br>
│   ├── static/            # CSS and other static resources  <br>
│   ├── models.py          # Database models for student records  <br>
│   ├── views.py           # Core logic and functionality for routes  <br>
│   └── urls.py            # App-specific URL routing  <br>
└── manage.py              # Django management script  <br>
 
# 🚦 Application Flow
**Key Views (views.py)**<br>
-  **Home (name):** Displays all student records for a specific category/stream.
-  **Category Pages (py, j, q, pro):** List students from specific streams (e.g., Python, Java, etc.).
-  **Add New Student (create):** Provides a form to input and save new student details.
-  **Edit Student Data (edit):** Modify specific student information by clicking their name.
-  **Delete Student (display):** Delete a student's record and manage database updates dynamically.

# 🛠 Future Enhancements
-  **Filter by Attributes:** Add filters for department, qualifications, or mock ratings.
-  **Sorting Options:** Enable sorting by age, YOP, or other attributes.
-  **Dashboard:** Implement an admin dashboard for managing student details effectively.
-  **Performance Insights: **Generate reports or statistics on student data.


# UI VIEW

![Screenshot 2024-12-18 175130](https://github.com/user-attachments/assets/da9bf31a-8be5-418b-b4d0-ff9ce63a2205)
![Screenshot 2024-12-18 175146](https://github.com/user-attachments/assets/fd66f25d-9916-449f-858c-90bd3b5a29dd)
![Screenshot 2024-12-18 175157](https://github.com/user-attachments/assets/18c640cf-76f6-4946-a00a-7a6b794ee5cb)
![Screenshot 2024-12-18 175207](https://github.com/user-attachments/assets/0feeba89-d39f-4f5b-8746-56eb9ff8df3e)
![Screenshot 2024-12-18 175219](https://github.com/user-attachments/assets/a56766c8-e0a3-4364-94dd-3ca661dc6b9d)
![Screenshot 2024-12-18 180027](https://github.com/user-attachments/assets/0c49956f-737d-4ad7-a597-0637d8d9037c)
![Screenshot 2024-12-18 175231](https://github.com/user-attachments/assets/dc6614c5-7b53-4627-8fd4-c117b15982da)
![Screenshot 2024-12-18 175246](https://github.com/user-attachments/assets/94c32ead-a124-4986-8ddb-084ee1f13350)
![Screenshot 2024-12-18 175257](https://github.com/user-attachments/assets/f1fb2359-0afa-4813-a886-1602bf8eb2b8)
