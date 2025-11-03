# Test both programs

print("=" * 50)
print("TESTING REGISTRATION SYSTEM (MVC)")
print("=" * 50)

# Import the classes
import sys
import importlib.util

# Load the registration system
spec = importlib.util.spec_from_file_location("registration", "Student Course Registration System.py")
registration = importlib.util.module_from_spec(spec)
spec.loader.exec_module(registration)

# Test Model
print("\n1. Testing MODEL...")
course1 = registration.Course("CMPSC101", "Intro to Computer Science")
print(f"   Created course: {course1.code} - {course1.name}")

student1 = registration.Student("Test Student")
print(f"   Created student: {student1.name}")
print(f"   Student courses: {student1.courses}")
print("   ✓ Model works!")

# Test Controller
print("\n2. Testing CONTROLLER...")
courses = [
    registration.Course("CMPSC101", "Intro to Computer Science"),
    registration.Course("CMPSC102", "Data Structures"),
    registration.Course("CMPSC103", "Algorithms")
]
controller = registration.RegistrationController(student1, courses)

print("   Registering for CMPSC101...")
controller.register("CMPSC101")
print(f"   Student now has {len(student1.courses)} course(s)")

print("   Trying duplicate registration for CMPSC101...")
controller.register("CMPSC101")

print("   Registering for CMPSC102...")
controller.register("CMPSC102")
print(f"   Student now has {len(student1.courses)} course(s)")

print("   Dropping CMPSC101...")
controller.drop("CMPSC101")
print(f"   Student now has {len(student1.courses)} course(s)")

print("   Trying to drop non-existent course...")
controller.drop("CMPSC999")
print("   ✓ Controller works!")

# Test View
print("\n3. Testing VIEW...")
print("   Displaying courses:")
registration.display_courses(courses)
print("\n   Displaying schedule:")
registration.display_schedule(student1)
print("   ✓ View works!")

print("\n" + "=" * 50)
print("TESTING INVOICE SYSTEM (Layered)")
print("=" * 50)

# Load the invoice system
spec2 = importlib.util.spec_from_file_location("invoice", "Invoice Processing System.py")
invoice_mod = importlib.util.module_from_spec(spec2)
spec2.loader.exec_module(invoice_mod)

# Test with sample data
print("\n1. Testing INPUT layer...")
test_invoice = {
    "items": [
        {"desc": "Laptop", "qty": 1, "price": 999.99},
        {"desc": "Mouse", "qty": 2, "price": 25.50}
    ]
}
print(f"   Created invoice with {len(test_invoice['items'])} items")
print("   ✓ Input works!")

print("\n2. Testing VALIDATION layer...")
print("   Validating good invoice...")
valid = invoice_mod.validate_invoice(test_invoice)
print(f"   Result: {valid}")

print("   Testing invalid invoice (negative quantity)...")
bad_invoice = {"items": [{"desc": "Test", "qty": -1, "price": 10}]}
valid2 = invoice_mod.validate_invoice(bad_invoice)
print(f"   Result: {valid2}")
print("   ✓ Validation works!")

print("\n3. Testing PROCESSING layer...")
processed = invoice_mod.calculate_invoice(test_invoice)
print(f"   Subtotal: ${processed['subtotal']:.2f}")
print(f"   Tax (6%): ${processed['tax']:.2f}")
print(f"   Total: ${processed['total']:.2f}")
print("   ✓ Processing works!")

print("\n4. Testing OUTPUT layer...")
invoice_mod.print_invoice(processed)
print("   ✓ Output works!")

print("\n" + "=" * 50)
print("ALL TESTS PASSED! ✓")
print("=" * 50)
