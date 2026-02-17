# MicroDegree Authentication Setup Guide

## Overview

This application now includes complete user authentication with:
- User registration with secure password hashing (bcrypt)
- Login/logout functionality
- User profile page
- Session state management
- AWS RDS MySQL database integration

## Database Schema

The application uses a `users` table with the following structure:

```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    full_name VARCHAR(255) NOT NULL,
    phone_number VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    INDEX idx_email (email)
);
```

## Setup Instructions

### 1. Local Development Setup

#### Prerequisites
- Python 3.10 or higher
- Access to the RDS database

#### Steps

1. **Install dependencies:**
```bash
pip install -r requirements.txt
```

2. **Set up environment variable:**
```bash
# On Linux/Mac:
export DB_PASSWORD='yourpassword'

# On Windows (PowerShell):
$env:DB_PASSWORD='yourpassword'

# On Windows (CMD):
set DB_PASSWORD=yourpassword
```

Or create a `.env` file (copy from `.env.example`):
```bash
cp .env.example .env
# Edit .env and set DB_PASSWORD=yourpassword
```

3. **Initialize the database (first time only):**
```bash
python init_db.py
```

This will create the `users` table in your RDS database if it doesn't exist.

4. **Run the application:**
```bash
streamlit run app.py
```

The application will be available at `http://localhost:8501`

### 2. Docker Development

#### Build and run with Docker:

```bash
# Build the image
docker build -t microdegree-app .

# Run with environment variable
docker run -p 8501:8501 -e DB_PASSWORD='yourpassword' microdegree-app
```

### 3. Kubernetes/EKS Deployment

#### Prerequisites
- EKS cluster configured
- kubectl configured to access your cluster

#### Steps

1. **Create the Kubernetes secret:**
```bash
kubectl apply -f secret.yaml
```

**IMPORTANT:** The `secret.yaml` file contains the actual password. For production:
- Do NOT commit `secret.yaml` to git
- Add `secret.yaml` to `.gitignore`
- Use AWS Secrets Manager or similar for production secrets

2. **Deploy the application:**
```bash
kubectl apply -f deployment.yaml
```

3. **Verify the deployment:**
```bash
kubectl get pods -n microdegree
kubectl get svc -n microdegree
```

4. **Get the LoadBalancer URL:**
```bash
kubectl get svc microdegree-svc -n microdegree
```

## Using the Application

### Registration Flow

1. Navigate to the application URL
2. Click on the "Register" tab
3. Fill in:
   - Full Name (required)
   - Email Address (required)
   - Password (required, min 6 characters)
   - Confirm Password (required)
   - Phone Number (optional)
4. Click "Register Now"
5. After successful registration, switch to the "Login" tab

### Login Flow

1. Navigate to the application URL
2. On the "Login" tab, enter:
   - Email Address
   - Password
3. Click "Login"
4. Upon successful login, you'll see your profile page with:
   - User information card
   - Educational videos
   - Articles and content

### Profile Page

After login, users will see:
- Profile card with their information (name, email, phone, member since date)
- Logout button in the top-right corner
- Educational content (videos and articles)

### Logout

Click the "Logout" button in the top-right corner to end your session.

## Database Connection Details

- **Host:** microdegree.cfoqwaayg09s.us-west-2.rds.amazonaws.com
- **Port:** 3306
- **Database:** mysql
- **User:** admin
- **Password:** Set via `DB_PASSWORD` environment variable

## Security Features

1. **Password Hashing:** Uses bcrypt with salt for secure password storage
2. **SQL Injection Protection:** Uses parameterized queries
3. **Environment Variables:** Sensitive credentials stored in environment variables
4. **Kubernetes Secrets:** Password stored in Kubernetes secrets (not in deployment yaml)
5. **Session Management:** Streamlit session state maintains user login state

## Troubleshooting

### Database Connection Errors

If you see "Database connection error":
1. Verify `DB_PASSWORD` environment variable is set correctly
2. Check RDS security groups allow connections from your IP/EKS cluster
3. Verify RDS instance is running
4. Check RDS endpoint is correct

### "Email already registered"

This means a user with that email already exists. Try:
- Using a different email
- Logging in instead of registering

### Table doesn't exist

Run the initialization script:
```bash
python init_db.py
```

## Files Overview

- `app.py` - Main Streamlit application with login/register/profile pages
- `database.py` - Database connection and user management functions
- `init_db.py` - Database initialization script (creates tables)
- `requirements.txt` - Python dependencies
- `Dockerfile` - Docker container configuration
- `deployment.yaml` - Kubernetes deployment and service manifests
- `secret.yaml` - Kubernetes secret for DB password (DO NOT COMMIT)
- `.env.example` - Template for local environment variables

## Next Steps

1. Add password reset functionality
2. Add email verification
3. Add user profile editing
4. Add remember me functionality
5. Add two-factor authentication
6. Move from RDS `mysql` database to a dedicated application database
