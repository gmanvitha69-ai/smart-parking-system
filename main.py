from collections import deque

class SmartParking:
    def __init__(self, total_slots):
        self.total_slots = total_slots
        self.available_slots = list(range(1, total_slots + 1))
        self.parked_vehicles = {}  # HashMap {vehicle_number: slot}
        self.waiting_queue = deque()  # Queue
        self.parking_history = []  # Stack
        self.total_earnings = 0

    def park_vehicle(self, vehicle_number):
        if vehicle_number in self.parked_vehicles:
            print("Vehicle already parked!")
            return

        if self.available_slots:
            slot = self.available_slots.pop(0)
            self.parked_vehicles[vehicle_number] = slot
            self.parking_history.append(vehicle_number)
            print(f"Vehicle {vehicle_number} parked at slot {slot}")
        else:
            self.waiting_queue.append(vehicle_number)
            print("Parking full! Vehicle added to waiting queue.")

    def remove_vehicle(self, vehicle_number):
        if vehicle_number in self.parked_vehicles:
            slot = self.parked_vehicles.pop(vehicle_number)
            self.available_slots.append(slot)
            self.total_earnings += 50  # Fixed parking fee
            print(f"Vehicle {vehicle_number} removed from slot {slot}")
            
            if self.waiting_queue:
                next_vehicle = self.waiting_queue.popleft()
                self.park_vehicle(next_vehicle)
        else:
            print("Vehicle not found!")

    def search_vehicle(self, vehicle_number):
        if vehicle_number in self.parked_vehicles:
            print(f"Vehicle is parked at slot {self.parked_vehicles[vehicle_number]}")
        else:
            print("Vehicle not found!")

    def show_available_slots(self):
        print("Available Slots:", sorted(self.available_slots))

    def show_earnings(self):
        print("Total Earnings:", self.total_earnings)


# ----------- MAIN PROGRAM -----------

parking = SmartParking(5)

while True:
    print("\n1. Park Vehicle")
    print("2. Remove Vehicle")
    print("3. Search Vehicle")
    print("4. Show Available Slots")
    print("5. Show Total Earnings")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        vehicle = input("Enter vehicle number: ")
        parking.park_vehicle(vehicle)

    elif choice == "2":
        vehicle = input("Enter vehicle number: ")
        parking.remove_vehicle(vehicle)

    elif choice == "3":
        vehicle = input("Enter vehicle number: ")
        parking.search_vehicle(vehicle)

    elif choice == "4":
        parking.show_available_slots()

    elif choice == "5":
        parking.show_earnings()

    elif choice == "6":
        print("Exiting system...")
        break

    else:
        print("Invalid choice!")