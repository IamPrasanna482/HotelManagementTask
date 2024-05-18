
# Task => Hotel Management System 


# Singleton Classes => UserManagementSystem, HotelManagementSystem
# FactoryClass => UserFactory, based on the roles, we can create users



# Implemented Concepts - 
    # 1. Inheritance
    # 2. Association
    # 3. SOLID Principles

# Implemented Design Patterns - 
    # 1. Singleton Design Pattern (UserManagementSystem, HotelManagementSystem) to have one instance throughout the program
    # 2. Factory Design Pattern ( Creation of different types of user objects (NormalUser, HotelAgent, and Administrator) )




# Class User acting as base class for NormalUser, HotelAgent
class User:
    def __init__(self, name):
        self.name = name


# Class NormalUser
class NormalUser(User):
    def __init__(self, name):
        super().__init__(name)


# Class HotelAgent
class HotelAgent(User):
    def __init__(self, name):
        super().__init__(name)

# Class Admin
class Admin(User):
    def __init__(self, name):
        super().__init__(name)


# Factory Class to provide and return roles of the userObjects
class UserFactory:
    @staticmethod
    def createUser(name, role):
        if role == "normal":
            return NormalUser(name)
        elif role == "agent":
            return HotelAgent(name)
        elif role == "admin":
            return Admin(name)
        else:
            print("This role is not present !")


# Singleton Class UMS to provide all the functionalities of the user management

# UserManagementSystem 'has a' User  (Association)
# UserManagementSystem 'has a' Admin  (Association)


class UserManagementSystem:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'users'):
            self.users = {}  # stores user information

    # method to add a new user
    def addUser(self, userObj,adminObj):
        if isinstance(adminObj,Admin):
            if userObj.name not in self.users:
                self.users[userObj.name] = userObj
                print(f"User {userObj.name} is added successfully !")
            else:
                print(f"User {userObj.name} already exists in the DB.")
        else:
            print("Only admin can add a user !")

    # method to remove a existing user
    def removeUser(self, name,adminObj):
        if isinstance(adminObj,Admin):

            if name in self.users:
                del self.users[name]
                print(f"User {name} deleted successfully.")
            else:
                print(f"User {name} not found.")
        else:
            print("Only admin can add a user !")

    # method to print all the current users
    def printAllUsers(self):
        print(self.users)

    # method to get a user by name
    def getUser(self, name):
        return self.users.get(name, None)


# Hotel Class to make hotel object
class Hotel:
    def __init__(self, name, location, numOfRooms, facilities):
        self.name = name # hotelName
        self.location = location  # hotelLocation
        self.numOfRooms = numOfRooms  # hotelNumberOfRooms
        self.roomsAvailability = numOfRooms  # hotelRoomsAvaiable
        self.facilities = facilities  # hotelFacilities => list



# Singleton Class UMS to provide all the functionalities of the user management

# HotelManagementSystem 'has a' hotel ( association )

class HotelManagementSystem:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'hotels'):
            self.hotels = {}  # stores hotel information

    # method to add a hotel
    def addHotel(self, name, location, numOfRooms, facilities, adminObj):
        if isinstance(adminObj,Admin):

            if name not in self.hotels:
                self.hotels[name] = Hotel(name, location, numOfRooms, facilities)
                print(f"Hotel {name} is added successfully !")
            else:
                print(f"Hotel {name} already exists !")
        else:
            print("Only admin can add hotel")

    # method to update a hotel information
    def updateHotel(self, name, location, numOfRooms, facilities,adminObj):
        if isinstance(adminObj,Admin):

            if name in self.hotels:
                self.hotels[name] = Hotel(name, location, numOfRooms, facilities)
                print(f"Hotel {name} updated successfully !")
            else:
                print(f"Hotel {name} not found !")
        else:
            print("Only admin can update hotel")

    
    
    # method to remove the hotel
    def removeHotel(self, name,adminObj):
        if isinstance(adminObj,Admin):
            if name in self.hotels:
                del self.hotels[name]
                print(f"Hotel {name} deleted successfully !")
            else:
                print(f"Hotel {name} not found !")
        else:
            print("Only admin can update hotel")

    # method to show hotel on the basis of name or location
    def showHotelsOnCriteria(self, criteria):  
        print(f"Listing hotels based on criteria: {criteria}")
        for hotel in self.hotels.values():
            if criteria in hotel.name or criteria in hotel.location:
                print(f"Hotel Name: {hotel.name}, Location: {hotel.location}, Rooms: {hotel.numOfRooms}, Facilities: {hotel.facilities}")

    # method to book hotel room on basis of roomsAvailability
    def bookHotelRoom(self, userObj, hotelName):
        if hotelName in self.hotels:
            hotel = self.hotels[hotelName]
            if hotel.roomsAvailability > 0:
                hotel.roomsAvailability -= 1
                print(f"Room booked in {hotelName}. Rooms left: {hotel.roomsAvailability} !")
            else:
                print(f"No rooms are available in {hotelName} . !")
        else:
            print(f"Hotel {hotelName} not found.")

    # method to display reservation if rooms are available or not
    def displayReservation(self):
        print("Reservation status is : ")
        for hotel in self.hotels.values():
            print(f"Hotel Name: {hotel.name}, Rooms Available: {hotel.roomsAvailability}")

    # method to approve hotel by admin only
    def approveHotel(self,adminObj):
        if isinstance(adminObj,Admin):
            print("Hotel details are approved")
        else:
            print("Only admin can approve the hotel")


if __name__ == "__main__":
    # Singleton instances
    hms = HotelManagementSystem()
    ums = UserManagementSystem()

    # Register users
    prasanna = UserFactory.createUser("prasanna", "normal")
    prasoon = UserFactory.createUser("prasoon", "agent")
    pragyan = UserFactory.createUser("pragyan", "admin")


    ums.addUser(prasanna,pragyan)  # added as a normalUser
    ums.addUser(prasoon,pragyan)   # added as a agent
    ums.addUser(pragyan,pragyan)   # added as an admin

    # Add and update hotel details
    hms.addHotel("Trident", "GZB", 50, ["swimming pool", "gym", "park", "wifi"],pragyan)
    hms.updateHotel("Taj", "Delhi", 45, ["WiFi", "park"],pragyan)

    # List all the hotels on criteria hotels
    hms.showHotelsOnCriteria("GZB")

    # Book hotel room
    hms.bookHotelRoom(prasanna,"Taj")

    # Display reservation status
    hms.displayReservation()

    # Admin actions
    admin = ums.getUser("pragyan")
   
    hms.approveHotel(admin)
    hms.removeHotel('Trident',pragyan)

