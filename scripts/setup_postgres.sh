#!/bin/bash

# PostgreSQL setup script

# Configuration
DB_NAME="your_app_db"
DB_USER="your_app_user"
DB_PASSWORD="your_secure_password"

# Check if psql is available
if ! command -v psql &> /dev/null; then
    echo "Error: psql could not be found. Please ensure PostgreSQL is installed and in your PATH."
    exit 1
fi

# Function to run SQL commands
run_sql() {
    psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
        $1
EOSQL
}

# Create database
run_sql "CREATE DATABASE $DB_NAME;"

# Create user
run_sql "CREATE USER $DB_USER WITH PASSWORD '$DB_PASSWORD';"

# Grant privileges
run_sql "GRANT ALL PRIVILEGES ON DATABASE $DB_NAME TO $DB_USER;"

# Connect to the new database and set up permissions
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$DB_NAME" <<-EOSQL
    GRANT USAGE ON SCHEMA public TO $DB_USER;
    GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO $DB_USER;
    GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO $DB_USER;
    ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON TABLES TO $DB_USER;
    ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON SEQUENCES TO $DB_USER;
EOSQL

echo "PostgreSQL setup completed successfully."
