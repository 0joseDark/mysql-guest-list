# mysql-guest-list
 - Guest list with MySQL

### Steps to install the required modules

1. **Install Python**:
   - Make sure Python is installed on Windows 10. It can be downloaded from [python.org](https://www.python.org/). Remember to check the "Add Python to PATH" option during installation.

2. **Install pip** (package manager):
   - Pip comes with recent versions of Python. To confirm, run in the terminal:
     ```bash
     python -m ensurepip
     ```

3. **Install `mysql-connector-python`**:
   - Run the following command in the terminal to install the MySQL connector:
     ```bash
     pip install mysql-connector-python
     ```

4. **Set up MySQL**:
   - Ensure MySQL is installed and running on your system. You can download it from [MySQL](https://www.mysql.com/).
   - Create a database named `guest_list`:
     ```sql
     CREATE DATABASE guest_list;
     ```

5. **Run the program**:
   - Save the code in a file named `guest_list.py` and execute it with:
     ```bash
     python guest_list.py
     ```

You can now add, list, and remove guests directly from the graphical interface!