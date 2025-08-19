class Smartphone:
    def __init__(self, brand, model, storage, battery):
        self.brand = brand
        self.model = model
        self.storage = storage  # in GB
        self.battery = battery  # percentage
    
    def make_call(self, number):
        return f"Calling {number} from {self.model}..."
    
    def install_app(self, app):
        return f"Installing {app} on {self.model}..."
    
    def check_battery(self):
        return f"Battery level: {self.battery}%"
    
class SmartphonePro(Smartphone):
    def __init__(self, brand, model, storage, battery, camera_quality):
        super().__init__(brand, model, storage, battery)  # inherit from parent
        self.camera_quality = camera_quality  # in megapixels
    
    def take_photo(self):
        return f"Taking a {self.camera_quality}MP photo with {self.model}!"
    
    # Polymorphism: Override check_battery()
    def check_battery(self):
        if self.battery < 20:
            return f"Low Battery! Only {self.battery}% left"
        return f"Battery level: {self.battery}%"
    
class SecureSmartphone(Smartphone):
    def __init__(self, brand, model, storage, battery):
        super().__init__(brand, model, storage, battery)
        self.__pin = "0000"  # private attribute
    
    def set_pin(self, new_pin):
        if len(new_pin) == 4 and new_pin.isdigit():
            self.__pin = new_pin
            return "PIN updated successfully."
        return "PIN must be a 4-digit number."
    
    def unlock(self, pin):
        if pin == self.__pin:
            return "Phone unlocked"
        return "Incorrect PIN"
    
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



