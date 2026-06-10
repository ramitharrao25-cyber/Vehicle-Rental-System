# 🚗 Vehicle Rental System

## Overview

The Vehicle Rental System is a Database Management System (DBMS) mini-project developed using **MySQL**, **Python**, and **Streamlit**. The application provides a user-friendly dashboard for managing customers, vehicles, bookings, rentals, payments, and maintenance records.

This project demonstrates the practical implementation of database concepts such as relational schema design, SQL queries, joins, subqueries, triggers, stored procedures, and database connectivity through a modern web interface.

---

## Features

### 👥 Customer Management

* Add new customers
* View customer details
* Store phone numbers and license information

### 🚙 Vehicle Management

* Add vehicles to the fleet
* Track vehicle type and rental price
* Monitor vehicle availability status

### 📅 Booking Management

* Create vehicle bookings
* Associate customers with vehicles
* Maintain booking records

### 💰 Rental & Payment Management

* Track rental periods
* Calculate rental charges
* Store payment information

### 🔧 Maintenance Management

* Record maintenance details
* Prevent bookings for vehicles under maintenance
* Update maintenance status

### 📊 Reports and Analytics

* View available vehicles
* Customer rental history
* Vehicle rental statistics
* Dashboard metrics and summaries

---

## Database Tables

The project consists of the following tables:

1. Customer
2. Vehicle
3. Booking
4. Rental
5. Payment
6. Maintenance

The tables are connected using primary keys and foreign keys to ensure data integrity.

---

## DBMS Concepts Implemented

* Entity Relationship (ER) Modeling
* Relational Schema Design
* Primary Keys
* Foreign Keys
* Constraints
* SQL Queries
* Joins (INNER JOIN, LEFT JOIN)
* Aggregate Functions
* GROUP BY and HAVING
* Nested Queries
* Stored Procedures
* Triggers
* Data Validation

---

## Technologies Used

### Frontend

* Python Streamlit
* Streamlit Option Menu

### Backend

* Python

### Database

* MySQL

### Python Libraries

* streamlit
* mysql-connector-python
* pandas
* streamlit-option-menu

---

## Project Structure

VehicleRentalSystem/

├── app.py

├── database/

│ ├── schema.sql

│ └── sample_data.sql

├── assets/

│ └── images/

├── requirements.txt

└── README.md

---

## Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/VehicleRentalSystem.git
cd VehicleRentalSystem
```

### Step 2: Install Required Libraries

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install streamlit
pip install mysql-connector-python
pip install pandas
pip install streamlit-option-menu
```

### Step 3: Configure MySQL Database

Create the database and tables in MySQL Workbench.

Update the database credentials in `app.py`:

```python
host="localhost"
user="root"
password="your_password"
database="VehicleRental"
```

### Step 4: Run the Application

```bash
streamlit run app.py
```

---

## Sample Dashboard Features

* Dashboard Overview
* Customer Management
* Vehicle Management
* Booking Creation
* Rental Reports
* Payment Tracking
* Interactive Tables
* Data Visualization

---

## Learning Outcomes

This project helped in understanding:

* Database Design and Normalization
* SQL Query Execution
* Frontend and Database Integration
* CRUD Operations
* Stored Procedures and Triggers
* Real-world DBMS Application Development

---

## Future Enhancements

* User Authentication System
* Vehicle Image Gallery
* Online Payment Integration
* Booking Cancellation Module
* Email Notifications
* Advanced Analytics Dashboard
* Mobile Responsive Interface

---

## Author

**Ramitha R Rao**

DBMS Mini Project – Vehicle Rental System

