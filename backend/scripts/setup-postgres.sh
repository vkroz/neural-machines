#!/bin/bash

# Docker PostgreSQL setup script

# Configuration
CONTAINER_NAME="postgreSQL"
DB_NAME="neuman"
DB_USER="neuman_app"
DB_PASSWORD="voo3beiM"

# Function to run SQL commands
run_sql() {
    docker exec -i $CONTAINER_NAME psql -U postgres <<EOF
$1
EOF
}

# Create database
run_sql "CREATE DATABASE $DB_NAME;"

# Create user
run_sql "CREATE USER $DB_USER WITH PASSWORD '$DB_PASSWORD';"

# Grant privileges
run_sql "GRANT ALL PRIVILEGES ON DATABASE $DB_NAME TO $DB_USER;"

# Connect to the new database and set up permissions
docker exec -i $CONTAINER_NAME psql -U postgres -d $DB_NAME <<EOF
GRANT USAGE ON SCHEMA public TO $DB_USER;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO $DB_USER;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO $DB_USER;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON TABLES TO $DB_USER;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON SEQUENCES TO $DB_USER;
EOF

echo "PostgreSQL setup in Docker container completed successfully."