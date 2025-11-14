# Python Software Architecture Patterns

A demonstration of two fundamental software architecture patterns implemented in Python: **Model-View-Controller (MVC)** and **Layered Architecture**. This educational project showcases how different architectural patterns can be applied to solve different types of problems.

## 📋 Table of Contents

- [Overview](#overview)
- [Architecture Patterns](#architecture-patterns)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Testing](#testing)
- [Pattern Comparison](#pattern-comparison)
- [Limitations](#limitations)

## 🎯 Overview

This repository contains two complete applications, each demonstrating a different architectural pattern:

1. **Student Course Registration System** - Implements the MVC (Model-View-Controller) pattern
2. **Invoice Processing System** - Implements the Layered Architecture pattern

Both applications are designed to illustrate when and why to use each architectural pattern in real-world scenarios.

## 🏗️ Architecture Patterns

### Model-View-Controller (MVC)

The Student Course Registration System uses MVC because it's an interactive application where users perform multiple actions and need immediate visual feedback.

**Components:**
- **Model**: `Course` and `Student` classes that represent the data
- **View**: Display functions (`show_menu()`, `display_courses()`, `display_schedule()`)
- **Controller**: `RegistrationController` class that handles user actions and updates the model

**Why MVC?**
- Separates concerns: data, presentation, and business logic
- Makes the code easier to test and maintain
- Ideal for interactive applications with user input

### Layered Architecture

The Invoice Processing System uses a Layered Architecture because it processes data through a sequential pipeline.

**Layers:**
1. **Input Layer**: `get_invoice_input()` - Collects data from user
2. **Validation Layer**: `validate_invoice()` - Ensures data integrity
3. **Processing Layer**: `calculate_invoice()` - Performs business logic (calculates totals and tax)
4. **Output Layer**: `print_invoice()` - Presents results

**Why Layered?**
- Data flows in one direction through well-defined stages
- Each layer has a single responsibility
- Easy to modify or replace individual layers
- Perfect for data processing pipelines

## 📁 Project Structure

```
.
├── Robert Bennethum Individual Assignment 2/
│   ├── Student Course Registration System.py  # MVC implementation
│   ├── Invoice Processing System.py           # Layered implementation
│   ├── main.py                                # Menu launcher
│   └── README.md                              # Assignment documentation
├── test_programs.py                           # Automated tests
├── Course Registration MVC.xml                # Architecture diagram
├── Invoice Processing System Layered.xml      # Architecture diagram
└── README.md                                  # This file
```

## 🚀 Installation

### Prerequisites

- Python 3.6 or higher

### Setup

1. Clone the repository:
```bash
git clone https://github.com/robertbiv/python-list-comprehension-and-decorators.git
cd python-list-comprehension-and-decorators
```

2. No additional dependencies required - uses Python standard library only!

## 💻 Usage

### Option 1: Interactive Menu

Run the main launcher to choose which program to run:

```bash
cd "Robert Bennethum Individual Assignment 2"
python main.py
```

You'll see a menu:
```
Assignment 2

1. Registration (MVC)
2. Invoice (Layered)
3. Exit

Choice:
```

### Option 2: Run Programs Directly

**Student Course Registration System (MVC):**
```bash
cd "Robert Bennethum Individual Assignment 2"
python "Student Course Registration System.py"
```

**Invoice Processing System (Layered):**
```bash
cd "Robert Bennethum Individual Assignment 2"
python "Invoice Processing System.py"
```

## 📝 Examples

### Student Course Registration System

```
Name: John Smith

1. View courses
2. Register
3. Drop
4. View schedule
5. Exit

Choice: 1

Courses:
- CMPSC101: Intro to Computer Science
- CMPSC102: Data Structures
- CMPSC103: Algorithms

Choice: 2
Course code: CMPSC101
Registered: CMPSC101

Choice: 4

John Smith's Schedule:
- CMPSC101: Intro to Computer Science
```

### Invoice Processing System

```
Enter items (blank to finish):
Description: Laptop
Quantity: 1
Price: 999.99
Description: Mouse
Quantity: 2
Price: 25.50
Description: 

INVOICE
Laptop: 1 x $999.99
Mouse: 2 x $25.50
Subtotal: $1050.99
Tax (6%): $63.06
Total: $1114.05
```

## 🧪 Testing

Run the automated test suite:

```bash
python test_programs.py
```

This will test:
- Model components (Course, Student classes)
- Controller functionality (register, drop courses)
- View functions (display methods)
- Input/validation layers
- Processing calculations
- Output formatting

Expected output:
```
==================================================
TESTING REGISTRATION SYSTEM (MVC)
==================================================

1. Testing MODEL...
   ✓ Model works!

2. Testing CONTROLLER...
   ✓ Controller works!

3. Testing VIEW...
   ✓ View works!

==================================================
TESTING INVOICE SYSTEM (Layered)
==================================================

1. Testing INPUT layer...
   ✓ Input works!

2. Testing VALIDATION layer...
   ✓ Validation works!

3. Testing PROCESSING layer...
   ✓ Processing works!

4. Testing OUTPUT layer...
   ✓ Output works!

==================================================
ALL TESTS PASSED! ✓
==================================================
```

## ⚖️ Pattern Comparison

| Aspect | MVC Pattern | Layered Pattern |
|--------|-------------|----------------|
| **Use Case** | Interactive applications | Data processing pipelines |
| **Data Flow** | Bidirectional (user ↔ system) | Unidirectional (top to bottom) |
| **Best For** | UI-driven applications | Sequential processing |
| **Complexity** | Higher (3 components) | Lower (linear flow) |
| **Testability** | Components can be tested separately | Layers can be tested independently |
| **Example** | Course Registration | Invoice Calculation |

## ⚠️ Limitations

### Student Course Registration System
- No data persistence (data is lost when program exits)
- Handles only one student per session
- No concurrent user support
- Basic validation only

### Invoice Processing System
- Fixed 6% tax rate (not configurable)
- No data persistence
- No support for discounts or complex pricing
- Basic error handling

## 📚 Learning Objectives

This project demonstrates:
- How to choose the right architecture pattern for different problems
- Separation of concerns in software design
- Clean code principles and organization
- Python class design and functions
- User input validation and error handling
- Writing testable code

## 👤 Author

Robert Bennethum

## 📄 License

This is an educational project created for academic purposes.
