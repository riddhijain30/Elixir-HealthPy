Welcome to Elixir-Healthpy

An interactive Python and MySQL-based health and wellness companion application.

Developed By
Riddhi Jain and Sarjana Shankar
---
Features:
Elixir acts as a digital wellness companion providing customized tracks based on your personal metrics:
* User Management: Supports profile creation for **New Users** and saves data securely for **Existing Users** using MySQL.
* BMI Calculator: Automatically computes and displays your Body Mass Index (BMI) based on your height and weight.
* Goal-Oriented Focus Tracks: Offers customized sub-menus for Physical Health, Mental Health, and Lifestyle routines.
* Interactive CLI UI: Beautiful color-coded terminal interfaces utilizing the `clrprint` library.
---
Tech Stack:
* Programming Language: Python 3.x
* Database Management: MySQL 
* Key Python Modules: `mysql-connector-python`, `clrprint`
---
Prerequisites & Installation

1. Download or clone this repository.
2. Make sure you have MySQL Server installed and running on your system.
3. Update the MySQL connection settings in the script (`host`, `user`, `password`) to match your local setup.
4. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
