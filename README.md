# Must Guild Project

## Description
**Must Guild** is a Django-based web application designed to facilitate community engagement and collaboration within a guild. The platform provides features such as user authentication, event management, reviews, and member contributions. It aims to enhance communication and participation among members of the guild.

## Features
- User authentication (Sign up, Login, Logout)
- Event management (View and participate in events)
- Campaigns and activities
- Member reviews and feedback
- Guild leadership and structure representation

## Project Structure
- **guild**: Contains the core app for managing events, campaigns, reviews, and guild members.
- **templates**: HTML templates for the frontend.
- **static**: Static files such as images.

## Admin Roles
The admin plays a crucial role in managing the application and ensuring smooth operations. Below are the key responsibilities of the admin:

1. **Event Management**:
   - Create, update, and delete events.
   - Upload images and set event details such as title, description, and date.

2. **Guild Leadership Management**:
   - Add, update, or remove guild leaders.
   - Manage leader profiles, including their name, title, description, and image.

3. **Campaign Management**:
   - Create, update, and delete campaigns.
   - Manage campaign details such as title, description, date, and associated images.

4. **Member Management**:
   - View and manage registered members.
   - Access member details such as name, email, and join date.

5. **Guild Activities**:
   - Link activities to specific events.
   - Manage activity details such as name, description, and date.

6. **Review Moderation**:
   - Monitor and manage user reviews.
   - Delete inappropriate or offensive reviews.

7. **General Administration**:
   - Access the Django admin panel to oversee all models and data.
   - Use search and filtering options to efficiently manage records.


## Installation
Follow these steps to set up the project locally:

```bash
# Clone the repository
git clone https://github.com/Curtis-18/must_guild_takehome.git

# Navigate to the project directory
cd must_guild_takehome

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Run the development server
python manage.py runserver
```

## Usage
1. Start the development server using `python manage.py runserver`.
2. Open your browser and navigate to `http://127.0.0.1:8000/`.
3. Sign up or log in to access features like viewing events, leaving reviews, and more.

## Implementation Details

### Data Validation and Error Handling
- **Forms**: Django forms are used for user input validation. For example, the `SignupForm` ensures that passwords match and fields are not empty.
- **Models**: Custom validation is implemented in models using the `clean` method, such as ensuring event titles and dates are not empty.
- **Error Handling**: Views include `try-except` blocks to catch and handle exceptions gracefully, displaying user-friendly error messages using Django's `messages` framework.

### Design and Styling
- **Frontend Framework**: The project uses Bootstrap for responsive design and consistent styling across pages.
- **Custom CSS**: Additional custom styles are applied for branding and unique design elements, such as gradients and hover effects.
- **Templates**: Django templates are used to structure HTML pages, ensuring reusability and maintainability.
- **User Experience**: Forms and buttons are styled for clarity and ease of use, with error messages displayed prominently.

### Code Quality and Project Structure
- **Project Structure**: The project follows Django's recommended structure, separating concerns into apps, templates, and static files.
- **Code Quality**: Adheres to PEP 8 standards for Python code. Admin classes, models, and views are modular and well-documented.
- **Reusability**: Common components like headers, footers, and navigation bars are included in a base template.
- **Testing**: The `tests.py` file is available for writing unit tests to ensure code reliability and correctness.

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push them to your fork.
4. Submit a pull request with a detailed description of your changes.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact
For any inquiries or support, please contact:
- **Email**: [18vicu@gmail.com](mailto:18vicu@gmail.com)
- **Phone**: +256 751 890 911
