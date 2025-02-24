# HRMS-HD

## Overview
HRMS-HD is a comprehensive Human Resource Management System designed to streamline HR processes, ensuring efficiency and compliance for businesses of all sizes. The system provides a secure and centralized platform for managing employees, payroll, attendance, and performance evaluation.

## Features (Current Scope: User Management)
The current version of HRMS-HD includes the following user management functionalities:

- **User Authentication**
  - Login
  - Logout
- **User Registration & Management**
  - Create User
  - Get User Information
  - Update User Details
- **Password Management**
  - Change Password
  - Forgot Password
  - Reset Password

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/hrms-hd.git
   ```
2. Navigate to the project directory:
   ```sh
   cd hrms-hd
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Run the application:
   ```sh
   python main.py
   ```

## API Endpoints
### User Management
- **POST** `/api/login` - Authenticate user
- **POST** `/api/logout` - Log out user
- **POST** `/api/create_user` - Register a new user
- **GET** `/api/get_info/{user_id}` - Retrieve user details
- **PUT** `/api/change_password` - Change user password
- **POST** `/api/forgot_password` - Initiate password reset process
- **POST** `/api/reset_password` - Reset password with verification

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

## Contact
For any issues or feature requests, please open an issue on [GitHub](https://github.com/your-username/hrms-hd/issues).
