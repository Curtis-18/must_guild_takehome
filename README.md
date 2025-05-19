# MUST Students Guild Web Application

## Description
**Must Guild** is a Django-based web application for MUST guild  designed to facilitate community engagement and collaboration within the guild. The platform provides features such as user authentication, event management, reviews, and member contributions. It aims to enhance communication and participation among members of the guild.

## Features
- Modern, responsive UI with consistent styling across all pages
- User authentication (sign up, login, logout)
- Events, campaigns, and activities management
- Reviews: users can leave reviews, like reviews, and see review counts
- **Volunteer System:**
  - Users can submit volunteer requests from the Get Involved page
  - Users see the status of their requests (pending, approved, rejected)
  - Admin can approve or reject volunteer requests in the Django admin panel
- **Notifications** (coming soon):
  - Users will receive notifications for volunteer request status and other important actions
- **Advanced Search & Filter** (coming soon):
  - Search and filter events, campaigns, members, and reviews with advanced options
- **Q&A Section** (coming soon):
  - Users can post questions and answers, upvote, and mark as solved
- Dashboard with analytics for logged-in users
- Newsletter and social media links in the footer

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

## Setup Instructions

1. **Clone the repository**
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```
4. **Create a superuser (for admin access):**
   ```bash
   python manage.py createsuperuser
   ```
5. **Run the development server:**
   ```bash
   python manage.py runserver
   ```
6. **Access the site:**
   - Home: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
   - Admin: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

## Volunteer Feature Usage
- Go to the **Get Involved** page and click **Volunteer Now**
- Fill out the volunteer form and submit
- View your request status on the Volunteer page
- Admins can approve/reject requests in the admin panel

## Planned Features
- In-app notifications for important actions
- Advanced search and filtering for all content
- Q&A section for student questions and answers

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
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](LICENSE)

## Contact
For any inquiries or support, please contact:
- **Email**: [18vicu@gmail.com](mailto:18vicu@gmail.com)
- **Phone**: +256 751 890 911
