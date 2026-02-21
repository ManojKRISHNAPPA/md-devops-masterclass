import psycopg2
import psycopg2.extras
import bcrypt
import os
from typing import Optional, Dict

def get_db_connection():
    """Create and return a PostgreSQL database connection."""
    try:
        conn = psycopg2.connect(
            host='itkanndigaru.c83m8iawyz1n.us-east-1.rds.amazonaws.com',
            port=5432,
            database='postgres',
            user='postgres',
            password=os.getenv('DB_PASSWORD', ''),
            sslmode='verify-full',
            sslrootcert=os.getenv('DB_SSL_ROOT_CERT', '/certs/global-bundle.pem')
        )
        return conn
    except psycopg2.Error as err:
        print(f"Database connection error: {err}")
        return None

def create_users_table():
    """Create the users table if it doesn't exist."""
    conn = get_db_connection()
    if not conn:
        return False

    try:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                email VARCHAR(255) UNIQUE NOT NULL,
                password_hash VARCHAR(255) NOT NULL,
                full_name VARCHAR(255) NOT NULL,
                phone_number VARCHAR(20),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()
        cursor.close()
        conn.close()
        return True
    except psycopg2.Error as err:
        print(f"Error creating table: {err}")
        if conn:
            conn.close()
        return False

def hash_password(password: str) -> str:
    """Hash a password using bcrypt."""
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')

def verify_password(password: str, password_hash: str) -> bool:
    """Verify a password against its hash."""
    return bcrypt.checkpw(password.encode('utf-8'), password_hash.encode('utf-8'))

def register_user(email: str, password: str, full_name: str, phone_number: str = None) -> tuple[bool, str]:
    """
    Register a new user in the database.
    Returns (success: bool, message: str)
    """
    conn = get_db_connection()
    if not conn:
        return False, "Database connection failed"

    try:
        cursor = conn.cursor()

        # Check if email already exists
        cursor.execute("SELECT id FROM users WHERE email = %s", (email,))
        if cursor.fetchone():
            cursor.close()
            conn.close()
            return False, "Email already registered"

        # Hash password and insert user
        password_hash = hash_password(password)
        cursor.execute(
            "INSERT INTO users (email, password_hash, full_name, phone_number) VALUES (%s, %s, %s, %s)",
            (email, password_hash, full_name, phone_number)
        )
        conn.commit()
        cursor.close()
        conn.close()
        return True, "Registration successful"

    except psycopg2.Error as err:
        print(f"Error registering user: {err}")
        if conn:
            conn.close()
        return False, f"Registration failed: {err}"

def authenticate_user(email: str, password: str) -> Optional[Dict]:
    """
    Authenticate a user with email and password.
    Returns user data dict if successful, None otherwise.
    """
    conn = get_db_connection()
    if not conn:
        return None

    try:
        cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cursor.execute(
            "SELECT id, email, password_hash, full_name, phone_number FROM users WHERE email = %s",
            (email,)
        )
        user = cursor.fetchone()
        cursor.close()
        conn.close()

        if user and verify_password(password, user['password_hash']):
            user_dict = dict(user)
            del user_dict['password_hash']
            return user_dict
        return None

    except psycopg2.Error as err:
        print(f"Error authenticating user: {err}")
        if conn:
            conn.close()
        return None

def get_user_by_email(email: str) -> Optional[Dict]:
    """Get user data by email (without password hash)."""
    conn = get_db_connection()
    if not conn:
        return None

    try:
        cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cursor.execute(
            "SELECT id, email, full_name, phone_number, created_at FROM users WHERE email = %s",
            (email,)
        )
        user = cursor.fetchone()
        cursor.close()
        conn.close()
        return dict(user) if user else None

    except psycopg2.Error as err:
        print(f"Error fetching user: {err}")
        if conn:
            conn.close()
        return None
