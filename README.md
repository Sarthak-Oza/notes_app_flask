# Flask Notes App

Welcome to the Flask Notes App! This application allows users to manage their notes with features like user authentication, signup, signin, create, update, and delete notes.

## Features:

- **User Authentication**: Users can sign up and sign in securely to access their notes.
- **Note Management**: Users can create, update, and delete their notes.
- **Security**: Secure authentication and authorization mechanisms are implemented to protect user data.

## Demo:

Check out the live demo of the Flask Notes App [here](https://sarthak0499.pythonanywhere.com/login?next=%2F).

## Screenshots:

![image](https://github.com/Sarthak-Oza/notes_app_flask/assets/68885011/3f615258-50b8-4082-89a8-2c19c6e8516c)

![image](https://github.com/Sarthak-Oza/notes_app_flask/assets/68885011/e954879b-5634-4a79-a51e-f13a803606f2)



## Local Setup:

To set up the Flask Notes App on your local machine, follow these steps:

1. Clone the repository:

   ```bash
   git clone <repository-url>
Replace <repository-url> with the URL of the repository.

2. Navigate to the project directory:
```
cd flask-notes-app
```
Create a virtual environment (optional but recommended):
```
python -m venv venv
```
Activate the virtual environment:

On Windows:
```
venv\Scripts\activate
```

On Unix/MacOS:
```
source venv/bin/activate
```
Install dependencies:
```
pip install -r requirements.txt
```
Set up the database:
```
flask db upgrade
```
Run the Flask app:
```
flask run
```
Open your web browser and go to http://localhost:5000 to access the app.

Contributing:
Contributions are welcome! If you'd like to contribute to the Flask Notes App, please follow these steps:

Fork the repository.
Create a new branch (git checkout -b feature/new-feature).
Make your changes.
Commit your changes (git commit -am 'Add new feature').
Push to the branch (git push origin feature/new-feature).
Create a new Pull Request.
