1. **Navigate to the Project Directory**:  
   Open Command Prompt and navigate to your project directory:
   ```bash
   cd C:\AKASH\Projects\Django\recipie
   ```

2. **Activate the Virtual Environment**:  
   Run this command to activate your virtual environment:
   ```bash
   .\venv\Scripts\activate
   ```

3. **Install Dependencies**:  
   Install the required packages by running:
   ```bash
   pip install asgiref==3.8.1 Django==5.1.2 pillow==11.0.0 sqlparse==0.5.1 tzdata==2024.2
   ```

4. **Run the Django Development Server**:  
   Go to the Django project directory (the inner `recipie` folder):
   ```bash
   cd C:\AKASH\Projects\Django\recipie\recipie
   ```
   Start the development server with:
   ```bash
   python manage.py runserver
   ```

5. **Access the Website**:  
   Open your browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/). You can now add, delete, or update recipes.

---
