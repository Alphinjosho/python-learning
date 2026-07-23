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

## Next Goals

- Insert records
- Learn INSERT
- Learn SELECT
- Learn UPDATE
- Learn DELETE
- Connect FastAPI with PostgreSQL
- Learn SQLAlchemy ORM