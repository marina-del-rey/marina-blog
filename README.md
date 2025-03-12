# Marina's blog
A simple blog built with Django, allowing users to create, manage, and categorize posts. Includes password-protected pages for enhanced privacy and control.

## Installation & Setup
### 1. Clone the repository  
```bash
git clone https://github.com/marina-del-rey/marina-blog.git
cd marina-blog
```

### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate # Linux/macOS
venv\Scripts\activate # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up the database
```bash
python manage.py migrate
python manage.py createsuperuser  # Create an admin user
```

### 5. Run the development server
```bash
python manage.py runserver
```

## Setting Up Environment Variables
Create a `.env` file inside the `mysite` directory and add:
```env
LOCKDOWN_PASSWORD=password1
```
Replace `password1` with your desired password for protected pages.


## To-do list
- Add a custom "Page Not Found" (404) template
- Enable blog post images
- Add a custom cursor

