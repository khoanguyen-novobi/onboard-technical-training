#!/usr/bin/env python3
import unittest

from parking_lot import Car, Slot, ParkingLot

class TestSlotFunctions(unittest.TestCase):
    """
    This test class is for testing function in Slot class
    """
    def test_park(self):
        """
        This function test the normal flow of park function
        """
        car = Car('VH1234', 'White')
        slot = Slot(1)
        self.assertEqual(slot.park_car(car), 'OK')

    def test_park_invalid(self):
        """
        This function test if park the car in the slot with car is already there
        """
        car1 = Car('VH1234', 'White')
        car2 = Car('VH1242', 'Black')
        slot = Slot(1)
        slot.park_car(car1)
        self.assertEqual(slot.park_car(car2), 'This slot is not empty!')

    def test_get_registration_number(self):
        """
        This function is test normal flow of get registration number of current slot
        """
        car = Car('VH1234', 'White')
        slot = Slot(1)
        slot.park_car(car)
        self.assertEqual(slot.get_registration_number(), 'VH1234')

    def test_get_registration_number_invalid(self):
        """
        This function is test if the slot with no car available
        """
        slot = Slot(1)
        self.assertEqual(slot.get_registration_number(), 'No car in this slot!')

    def test_get_color(self):
        """
        This function is test normal flow of get car color of current slot
        """
        car = Car('VH1234', 'Black')
        slot = Slot(1)
        slot.park_car(car)
        self.assertEqual(slot.get_color(), 'Black')

    def test_get_color_invalid(self):
        """
        This function is test if the slot with no car available
        """
        slot = Slot(1)
        self.assertEqual(slot.get_color(), 'No car in this slot!')

class TestParkingLotFunctions(unittest.TestCase):
    """
    This test class is for testing function in ParkingLot class
    """
    def test_create_parking_lot(self):
        """
        This function is test for creating parking lot slot
        """
        parking_lot = ParkingLot()
        self.assertEqual(parking_lot.create_parking_lot(6), 'OK')

    def test_create_parking_lot_invalid(self):
        """
        This function is test for creating parking lot slot with negative number of slot
        """
        parking_lot = ParkingLot()
        self.assertEqual(parking_lot.create_parking_lot(3), 'No of slot must be even positive!')
        self.assertEqual(parking_lot.create_parking_lot(-4), 'No of slot must be even positive!')

    def test_park(self):
        """
        This function is test for parking a car to the parking lot
        """
        parking_lot = ParkingLot()
        parking_lot.create_parking_lot(2)
        self.assertEqual(parking_lot.park('VH1234','Black'), 'OK')

    def test_park_invalid(self):
        """
        This function is test for parking a car to the parking lot with full capacity
        """
        parking_lot = ParkingLot()
        parking_lot.create_parking_lot(2)
        parking_lot.park('VH1234','Black')
        parking_lot.park('VH6346','Black')
        self.assertEqual(parking_lot.park('VH1235','White'), 'Parking slot is full!')

    def test_leave(self):
        """
        This function is test for leaving the parking lot
        """
        parking_lot = ParkingLot()
        parking_lot.create_parking_lot(2)
        parking_lot.park('VH1234','Black')
        self.assertEqual(parking_lot.leave(1), 'OK')

    def test_leave_no_car(self):
        """
        This function is test for leaving the car when there is no car in the parking lot
        """
        parking_lot = ParkingLot()
        parking_lot.create_parking_lot(2)
        self.assertEqual(parking_lot.leave(1), 'No car to leave!')

    def test_leave_no_car_in_slot(self):
        """
        This function is test for leaving the empty slot
        """
        parking_lot = ParkingLot()
        parking_lot.create_parking_lot(2)
        parking_lot.park('VH1234','Black')
        self.assertEqual(parking_lot.leave(2), 'No car to leave in this slot!')

    def test_get_status(self):
        """
        This function is test for getting status in the parking lot
        """
        parking_lot = ParkingLot()
        parking_lot.create_parking_lot(2)
        parking_lot.park('VH1234','Black')
        parking_lot.park('VH4345','Pink')
        self.assertEqual(parking_lot.size, 2)
        self.assertEqual(parking_lot.car_count, 2)
        self.assertEqual(parking_lot.get_status(), 'OK')

    def test_get_slot_number_by_color(self):
        """
        This function is test for getting slot number list with specific color
        """
        parking_lot = ParkingLot()
        parking_lot.create_parking_lot(2)
        parking_lot.park('VH1234','Black')
        parking_lot.park('VH4345','Black')
        self.assertEqual(parking_lot.get_slot_number_by_color('Black'), '1 2')

    def test_get_slot_number_by_color_no_car(self):
        """
        This function is test for getting slot number list with specific color when there is no car
        """
        parking_lot = ParkingLot()
        parking_lot.create_parking_lot(2)
        self.assertEqual(parking_lot.get_slot_number_by_color('Black'), 'No car in parking lot!')

    def test_get_slot_number_by_color_no_car_with_color(self):
        """
        This function is test for getting slot number list with specific color when there is no car with 
        predetermine color
        """
        parking_lot = ParkingLot()
        parking_lot.create_parking_lot(2)
        parking_lot.park('VH1234','Black')
        parking_lot.park('VH4345','Black')
        self.assertEqual(parking_lot.get_slot_number_by_color('White'), 'No car with this color!')

    def test_get_slot_number_by_registration_number(self):
        """
        This function is test for getting slot number with specific registration number
        """
        parking_lot = ParkingLot()
        parking_lot.create_parking_lot(4)
        parking_lot.park('VH1234','Black')
        parking_lot.park('VH4345','Black')
        parking_lot.park('VH5555','Black')
        self.assertEqual(parking_lot.get_slot_number_by_registration_number('VH1234'), 1)
        self.assertEqual(parking_lot.get_slot_number_by_registration_number('VH4345'), 2)
        self.assertEqual(parking_lot.get_slot_number_by_registration_number('VH5555'), 3)

    def test_get_slot_number_by_registration_number_no_car(self):
        """
        This function is test for getting slot number with specific registration number when there is no car in the parking lot
        """
        parking_lot = ParkingLot()
        parking_lot.create_parking_lot(2)
        self.assertEqual(parking_lot.get_slot_number_by_registration_number('VH1234'), 'No car in parking lot!')

    def test_get_slot_number_by_registration_number_car_not_found(self):
        """
        This function is test for getting slot number with specific registration number when there is no car in the parking lot
        """
        parking_lot = ParkingLot()
        parking_lot.create_parking_lot(4)
        parking_lot.park('VH1234','Black')
        parking_lot.park('VH4345','Black')
        parking_lot.park('VH5555','Black')
        self.assertEqual(parking_lot.get_slot_number_by_registration_number('VH6666'), 'Car not found!')

    def test_get_registration_numbers_with_colour(self):
        """
        This function is test for getting registration number list with specific color
        """
        parking_lot = ParkingLot()
        parking_lot.create_parking_lot(4)
        parking_lot.park('VH1234','Black')
        parking_lot.park('VH4345','White')
        parking_lot.park('VH5555','Black')
        self.assertEqual(parking_lot.get_registration_numbers_with_colour('Black'), 'VH1234 VH5555')
        self.assertEqual(parking_lot.get_registration_numbers_with_colour('White'), 'VH4345')

    def test_get_registration_numbers_with_colour_no_car(self):
        """
        This function is test for getting registration number list with specific color when there is no car in the parking lot
        """
        parking_lot = ParkingLot()
        parking_lot.create_parking_lot(4)
        self.assertEqual(parking_lot.get_registration_numbers_with_colour('Black'), 'No car in parking lot!')

    def test_get_registration_numbers_with_colour_no_car(self):
        """
        This function is test for getting registration number list with specific color when there is no car with this color
        """
        parking_lot = ParkingLot()
        parking_lot.create_parking_lot(4)
        parking_lot.park('VH1234','Black')
        self.assertEqual(parking_lot.get_registration_numbers_with_colour('White'), 'No car with this color!')

if __name__ == '__main__':
    unittest.main(verbosity=0)
