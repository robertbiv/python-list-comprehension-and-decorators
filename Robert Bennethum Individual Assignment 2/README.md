# Robert Bennethum
# README

## Programs
1. Student Course Registration
2. Invoice Processing

## How to Run

python main.py

Pick option 1 or 2 from the menu.

Or run directly:

python "Student Course Registration System.py"
python "Invoice Processing System.py"

Enter information as requested

## Why These Patterns?

**MVC** - Registration is interactive. User does multiple things. MVC separates data, display, and logic.

**Layered** - Invoice is a pipeline. Data flows: input -> validate -> calculate -> output.

## Limitations
- Registration: No saves, one student at a time
- Invoice: 6% tax only, no saves

## Dependancies
- N/A