# Must Guild Project

## Description
**Must Guild** is a Django-based web application designed to facilitate community engagement and collaboration within a guild. The platform provides features such as user authentication, event management, reviews, and member contributions. It aims to enhance communication and participation among members of the guild.

## Features
- User authentication (Sign up, Login, Logout)
- Event management (View and participate in events)
- Campaigns and activities
- Member reviews and feedback
- Guild leadership and structure representation

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

## Project Structure
- **guild**: Contains the core app for managing events, campaigns, reviews, and guild members.
- **templates**: HTML templates for the frontend.
- **static**: Static files such as images.

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
