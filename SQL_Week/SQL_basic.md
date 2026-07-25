# SQL Basics

## Database
A database is a collection of related data.

## Table
A table stores one type of data.

## Row
A row is one record.

## Column
A column represents one property.

## Primary Key
A unique value that identifies each row.

## CRUD

Create -> INSERT
Read -> SELECT
Update -> UPDATE
Delete -> DELETE

Examples:

SELECT * FROM students;

SELECT name FROM students;

SELECT name, age FROM students;

SELECT * FROM students
WHERE id = 3;


# Week 4 - Day 2
## PostgreSQL Setup & Database Basics

**Date:** 24 July 2026

## Topics Learned

### 1. What is PostgreSQL?
- PostgreSQL is an open-source Relational Database Management System (RDBMS).
- It stores data permanently, unlike Python lists.

### 2. Why PostgreSQL?
- Data remains even after the application closes.
- Used in real-world backend applications.
- Commonly used with FastAPI and SQLAlchemy.

### 3. PostgreSQL Installation
- Installed PostgreSQL 17.
- Configured password for the `postgres` user.
- Learned the default port: `5432`.
- Installed and opened pgAdmin.
- Learned that Stack Builder is optional.

### 4. Database Structure

```
PostgreSQL Server
│
├── Database
│     ├── Tables
│     ├── Rows
│     └── Columns
```

 

### 6. Created Columns

- id
- name
- age
- course

### 7. Concepts Learned

- Database
- Table
- Row
- Column
- Primary Key
- Identity Column
- Port 5432
- pgAdmin
- PostgreSQL Server

## Progress

✅ PostgreSQL Installed

✅ Connected pgAdmin to PostgreSQL

✅ Created first database

✅ Created first table

 # Week 4 - Day 3
## SQL CRUD Operations

**Date:** 24 July 2026

---

## Topics Learned

### PostgreSQL Practice

- Connected to PostgreSQL using pgAdmin
- Worked with the `student_db` database
- Used the `students` table

### SQL Commands Practiced

#### SELECT
- Retrieved all records
- Retrieved specific columns

#### WHERE
- Filtered records using conditions

#### INSERT
- Added new student records

#### UPDATE
- Updated existing student data

#### DELETE
- Deleted records from the table

---

## Concepts Understood

- SQL CRUD Operations
- Reading data using SELECT
- Filtering data using WHERE
- Updating records
- Deleting records

---

## Practical Work

- Created 4 student records
- Practiced SQL queries in the Query Tool
- Verified changes using SELECT

---

## Week 4 Progress

- PostgreSQL Installation ✅
- Database Creation ✅
- Table Creation ✅
- SQL CRUD Operations ✅

Overall Progress: **75%**

---

## Next Goal (Day 4)

- Learn SQLAlchemy
- Understand ORM
- Create database connection in Python
- Create SQLAlchemy models
- Connect Python to PostgreSQL


# Week 4 - Day 4
## SQLAlchemy Fundamentals (Session 1)

**Date:** 25 July 2026

---

# Goal

Learn the core concepts of SQLAlchemy and understand how Python communicates with PostgreSQL.

---

# Topics Learned

## 1. What is SQLAlchemy?

- SQLAlchemy is a Python library.
- It helps Python communicate with relational databases such as PostgreSQL.
- It converts Python operations into SQL queries.

---

## 2. What is ORM?

ORM = Object Relational Mapper

ORM maps Python classes to database tables.

### Mapping

| PostgreSQL | Python |
|------------|--------|
| Table | Class |
| Row | Object |
| Column | Attribute |

---

## 3. Engine

The Engine creates and manages the connection between Python and PostgreSQL.

Database URL contains:

- Database Type
- Username
- Password
- Host (localhost)
- Port (5432)
- Database Name (student_db)

---

## 4. Session

Session acts as a workspace for database operations.

Changes are not permanently saved until:

```python
db.commit()
```

`commit()` saves changes to PostgreSQL.

---

## 5. Models

A Model is a Python class that represents a database table.

Example Concept:

```
students table
      │
      ▼
class Student
```

---

# Architecture

```
FastAPI
    │
    ▼
SQLAlchemy
    │
    ▼
PostgreSQL
```

---

# Concepts Understood

- SQLAlchemy
- ORM
- Engine
- Database URL
- Session
- commit()
- Models

 
# Progress

Week 4 Progress: **~82% Complete**

Completed:

- PostgreSQL Installation ✅
- Database Creation ✅
- Table Creation ✅
- SQL CRUD Operations ✅
- SQLAlchemy Concepts ✅

Remaining:

- SQLAlchemy Practical Coding
- Connect Python to PostgreSQL
- FastAPI + PostgreSQL
- Alembic

---

# Next Goal

- Create `database.py`
- Create `models.py`
- Connect SQLAlchemy to PostgreSQL
- Create tables using SQLAlchemy