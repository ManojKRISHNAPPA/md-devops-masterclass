#!/usr/bin/env python3
"""
Database initialization script.
Run this once to create the users table in RDS.
"""

import os
import sys

# Ensure DB_PASSWORD is set
if not os.getenv('DB_PASSWORD'):
    print("ERROR: DB_PASSWORD environment variable is not set!")
    print("Please set it before running: export DB_PASSWORD='your_password'")
    sys.exit(1)

from database import create_users_table

print("Initializing database...")
print("Creating users table in RDS...")

if create_users_table():
    print("✓ Users table created successfully!")
    print("Database is ready to use.")
else:
    print("✗ Failed to create users table. Check the error messages above.")
    sys.exit(1)
