#!/bin/bash
# get username and password from mysql_credentials file
# user must change values in this file before running this script
MYSQL_OPTION_FILE="mysql_credentials.ini"

# Function to check if a MySQL database exists
check_mysql_database() {
    local database_name="$1"
    # script will not run if mysqlserver 8.0 is not installed, because path requires a mysql.exe file
    local exists=$("C:/Program Files/MySQL/MySQL Server 8.0/bin/mysql.exe" --defaults-extra-file="$MYSQL_OPTION_FILE" -s -N -e "SHOW DATABASES LIKE '$database_name';")

  if [ -n "$exists" ]; then
        echo "MySQL database '$database_name' exists."
    else
        echo "MySQL database '$database_name' does not exist. Attempting to create it..."

        # Attempt to create the database
        create_database "$database_name"

        # Run db.py script to run migrations
        run_db_script
    fi
}

# Function to create a MySQL database
create_database() {
    local database_name="$1"

    # Prompt user for MySQL root password
    read -s -p "Enter MySQL root password: " mysql_root_password
    echo

    # Attempt to create the database
    if "C:/Program Files/MySQL/MySQL Server 8.0/bin/mysql.exe" --defaults-extra-file="$MYSQL_OPTION_FILE" -u root -p"$mysql_root_password" -e "CREATE DATABASE $database_name;"; then
        echo "MySQL database '$database_name' created successfully."

    else
        echo "Error: Failed to create MySQL database '$database_name'."
        exit 1
    fi
}

run_db_script() {
    echo "Running db.py script..."
    python db.py
}

# Function to check if a directory exists
check_directory() {
    local directory_path="$1"
    
    if [ -d "$directory_path" ]; then
        echo "Directory '$directory_path' exists."
    else
        echo "Error: Directory '$directory_path' does not exist."
        exit 1
    fi
}
echo "Info: Script will not run successfully if MySQL Server 8.0 is not installed or mysql_credentials.ini does not contain credentials."
echo ""
# Check MySQL database existence
check_mysql_database "construct"

# Check directory existence for log
check_directory "log"

# Check directory existence for migrations
check_directory "migrations"

# If all checks pass, display success message
echo "All checks passed successfully."