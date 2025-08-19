# OOP Assignment 1

## Description

This assignment demonstrates the basics of **Object-Oriented Programming (OOP)** in Python.We explore the four main principles:

- **Encapsulation**
- **Inheritance**
- **Polymorphism**
- **Constructors**

We use a `Smartphone` example to bring these concepts to life.

## Features Implemented

### 1. Base Class: Smartphone

- Attributes: `brand`, `model`, `storage`, `battery`
- Methods: `make_call()`, `install_app()`, `check_battery()`

### 2. Inheritance: SmartphonePro

- Extends `Smartphone`
- Adds new attribute: `camera_quality`
- New method: `take_photo()`
- Overrides `check_battery()` to show warnings when battery is low

### 3. Encapsulation: SecureSmartphone

- Introduces private attribute `__pin`
- Provides controlled access through `set_pin()` and `unlock()` methods

### 4. Demonstration

Objects created from each class showcase:

- Initialization using constructors (`__init__`)
- Inherited and overridden methods
- Encapsulation in action with private data

## Example Usage

```python
# Base smartphone
phone1 = Smartphone("Samsung", "Galaxy S21", 128, 75)
print(phone1.make_call("0712345678"))
print(phone1.install_app("WhatsApp"))
print(phone1.check_battery())

# Pro smartphone with inheritance + polymorphism
phone2 = SmartphonePro("Apple", "iPhone 15 Pro", 256, 15, 48)
print(phone2.take_photo())
print(phone2.check_battery())

# Secure smartphone with encapsulation
phone3 = SecureSmartphone("Google", "Pixel 8", 128, 60)
print(phone3.set_pin("1234"))
print(phone3.unlock("1234"))
print(phone3.unlock("0000"))
```

### Expected Output

```
Calling 0712345678 from Galaxy S21...
Installing WhatsApp on Galaxy S21...   
Battery level: 75%
Taking a 48MP photo with iPhone 15 Pro!
Low Battery! Only 15% left
PIN updated successfully.
Phone unlocked
Incorrect PIN
```

## Conclusion

This assignment covers:

- **Encapsulation**: Protecting data with private attributes
- **Inheritance**: Reusing and extending parent class features
- **Polymorphism**: Overriding methods for different behaviors
- **Constructors**: Initializing objects with unique values

The example provides a complete and practical demonstration of **OOP in Python**.
