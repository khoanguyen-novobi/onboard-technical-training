#!/usr/bin/env python3

#This is  parking lot assignment code file

import sys

from prettytable import PrettyTable

class Car:
    """
    Class of Car 
    """
    def __init__(self, registration_number, color):
        # car registration number
        self.registration_number = registration_number
        # car color
        self.color = color

class Slot:
    """
    Class of Slot
    """
    def __init__(self, id):
        # slot id
        self.id = id
        # car in current slot
        self.car = None

    def park_car(self, car: Car):
        """
        This function is to park a car in a slot
        """
        status = ''
        if self.car is None:
            self.car = car
            status = 'OK'
        else:
            status = 'This slot is not empty!'
        return status
    
    def get_registration_number(self):
        """
        This function is to get registration number of the car in the current slot
        """
        if self.car is not None:
            return str(self.car.registration_number)
        else:
            return ('No car in this slot!')
    
    def get_color(self):
        """
        This function is to get color of the car in the current slot
        """
        if self.car is not None:
            return str(self.car.color)
        else:
            return ('No car in this slot!')

class ParkingLot:
    """
    Class of Parking Lot 
    """
    def __init__(self):
        #parking lot size
        self.size = 0
        #current car number in the parking lot
        self.car_count = 0
        #Slot array
        self.parking_lot_list = []
        #Create status table
        self.table = PrettyTable()

    def create_parking_lot(self, capacity):
        """
        This function is to create a parking lot with specific slots
        """
        if capacity % 2 != 0 or capacity <= 0:
            return 'No of slot must be even positive!'
        self.size = capacity
        for i in range(self.size):
            self.parking_lot_list.append(Slot(i + 1))
        return 'OK'
        
    def park(self, registration_number, color):
        """
        This function is to park a car in current slot
        """
        if self.car_count == self.size:
            return 'Parking slot is full!'
        else:
            for slot in self.parking_lot_list:
                if slot.car is None:
                    slot.park_car(Car(registration_number, color))
                    self.car_count += 1
                    break
            return 'OK'

    def leave(self, slot):
        """
        This function is to leave a car in current slot
        """
        if self.car_count == 0:
            return 'No car to leave!'
        elif slot > self.size or slot < 0:
            return 'No slot in this parking lot'
        else:
            if self.parking_lot_list[slot - 1].car is not None:
                self.parking_lot_list[slot - 1].car = None
                self.car_count -= 1
                return 'OK'
            else:
                return 'No car to leave in this slot!'
    
    def get_status(self):
        """
        This function is to get the current status of the parking lot
        """
        self.table.clear()
        self.table.field_names = ['Slot No.', 'Reg No.', 'Color']
        for slot in self.parking_lot_list:
            if slot.car is None:
                continue
            else:
                self.table.add_rows([[str(slot.id), str(slot.get_registration_number()), str(slot.get_color())]])
        print(self.table)
        return 'OK'
    
    def get_slot_number_by_color(self, color):
        """
        This function is to find a list of slot number based on car color
        """
        slot_list = []
        if self.car_count == 0:
            return 'No car in parking lot!'
        for slot in self.parking_lot_list:
            if slot.car is None:
                continue
            else:
                if slot.get_color() == color:
                    slot_list.append(slot.id)
        if len(slot_list) == 0:
            return 'No car with this color!'
        else:
            id_with_color = ' '.join([str(id) for id in slot_list])
            print(f'Id list:{id_with_color}')
            return id_with_color

    def get_slot_number_by_registration_number(self, registration_number):
        """
        This function is to get the slot number based on car registration number
        """
        if self.car_count == 0:
            return 'No car in parking lot!'
        for slot in self.parking_lot_list:
            if slot.car is None:
                continue
            else:
                if slot.get_registration_number() == registration_number:
                    print(f'Id: {slot.id}')
                    return slot.id
        return 'Car not found!'
    
    def get_registration_numbers_with_colour(self, color):
        """
        This function is to get the registration number list based on car color
        """
        reg_num_list = []
        if self.car_count == 0:
            return 'No car in parking lot!'
        for slot in self.parking_lot_list:
            if slot.car is None:
                continue
            else:
                if slot.get_color() == color:
                    reg_num_list.append(slot.get_registration_number())
        if len(reg_num_list) == 0:
            return 'No car with this color!'
        else:
            reg_num_with_color = ' '.join([str(id) for id in reg_num_list])
            print(f'Registration number list: {reg_num_with_color}')
            return reg_num_with_color

def execute(parking_lot: ParkingLot, command):
    """
    This function is to execute the command from input file or interactive mode
    """
    if command[0] == 'create_parking_lot':
        parking_lot.create_parking_lot(int(command[1]))
    elif command[0] == 'park':
        parking_lot.park(command[1], command[2])
    elif command[0] == 'leave':
        parking_lot.leave(int(command[1]))
    elif command[0] == 'status':
        parking_lot.get_status()
    elif command[0] == 'slot_numbers_for_cars_with_colour':
        parking_lot.get_slot_number_by_color(command[1])
    elif command[0] == 'slot_number_for_registration_number':
        parking_lot.get_slot_number_by_registration_number(command[1])
    elif command[0] == 'registration_numbers_for_cars_with_colour':
        parking_lot.get_registration_numbers_with_colour(command[1])
    else:
        print('Command is not found, please try again !!!')

def interactive_mode(parking_lot: ParkingLot):
    """
    This function is to use in the interactive mode
    """
    try:
        command = input().split()
        while command[0] != 'exit':
            execute(parking_lot, command)
            command = input().split()
    except Exception as e:
        print(e)

def input_file_mode(parking_lot: ParkingLot, filename):
    """
    This function is to use in the input file mode
    """
    try:
        with open(filename) as file:
            commands = file.readlines()
            for command in commands:
                parkingLot = execute(parking_lot, command.replace('\n', '').split())
    except Exception as e:
        print(e)

def main():
    """
    Main driven code
    """
    parking_lot = ParkingLot()
    if len(sys.argv) > 1:
        input_file_mode(parking_lot, sys.argv[1])
    else:
        interactive_mode(parking_lot)

if __name__ == '__main__':
    main()
