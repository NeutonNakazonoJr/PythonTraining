
class FuelPomp:

    def __init__(self, fuel_stock_initial):
        self.__fuel_stock_initial = fuel_stock_initial
        self.__type_fuel = str()
        self.__value_liter = 0
        self.__fuel_output = 0
        self.__stock_control = 0

    def price_by_liter(self):

        self.__type_fuel = input("Type of fuel ")

        if self.__type_fuel == "gasoline":
            self.__value_liter = 3

        elif self.__type_fuel == "alcohol":
            self.__value_liter = 2

        fuel_price = self.__value_liter

        return print("The price by liter is {} dollars".format(fuel_price))

    def fuel_by_value(self):

        quantity_value = int(input("what value would you like to put  "))
        fuel_by_value = quantity_value / self.__value_liter

        self.__fuel_output = int(self.__fuel_output + fuel_by_value)

        return print("The quantity of liters filled is {}".format(fuel_by_value))

    def fuel_by_liter(self):

        quantity_liter = int(input("how many liters would you like to fill "))
        value_to_pay = quantity_liter * self.__value_liter
        self.__fuel_output = self.__fuel_output + quantity_liter

        print("the amount payable is {}".format(value_to_pay))

    def stock_control(self):

        self.__stock_control = self.__fuel_stock_initial - self.__fuel_output
