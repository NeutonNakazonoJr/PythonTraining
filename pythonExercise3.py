stock_error_message = "insufficient stock"


def get_amount_supply():

    input_amount_supply = int(input("how many do you want to supply? "))

    return input_amount_supply


class FuelPomp:
    def __init__(self, get_initial_stock_alcohol, get_initial_stock_gasoline):
        self.__get_initial_stock_alcohol = int(get_initial_stock_alcohol)
        self.__get_initial_stock_gasoline = int(get_initial_stock_gasoline)
        self.__output_alcohol = 0
        self.__output_gasoline = 0
        self.__alcohol_price = 2
        self.__gasoline_price = 3
        self.__fuel_options = ("alcohol", "gasoline")
        self.__supply_options = ("money", "liters")

    def get_supply_option(self):
        input_option_supply = input("Supply options: in MONEY or by LITERS? ").lower()

        if input_option_supply in self.__supply_options:
            return input_option_supply
        else:
            return print("Invalid supply option")

    def get_fuel_option(self):
        input_fuel_option = input("Fuel options: ALCOHOL or GASOLINE ").lower()

        if input_fuel_option in self.__fuel_options:
            return input_fuel_option
        else:
            return print("Invalid fuel option")

    def liter_supply_option(self):

        input_amount_supply = get_amount_supply()
        input_fuel_option = self.get_fuel_option()
        output_message = "the value of supplying {} liters of {} is {} dollars"

        if input_fuel_option == self.__fuel_options[0]:
            result = self.__alcohol_price * input_amount_supply

            if self.__get_initial_stock_alcohol - input_amount_supply >= 0:
                self.__output_alcohol = self.__output_alcohol + input_amount_supply
                self.__get_initial_stock_alcohol = self.__get_initial_stock_alcohol - input_amount_supply
                print(output_message.format(input_amount_supply, self.__fuel_options[0], result))
            else:
                print(stock_error_message)

        elif input_fuel_option == self.__fuel_options[1]:
            result = self.__gasoline_price * input_amount_supply

            if self.__get_initial_stock_gasoline - input_amount_supply >= 0:
                self.__output_gasoline = self.__output_gasoline + input_amount_supply
                self.__get_initial_stock_gasoline = self.__get_initial_stock_gasoline - input_amount_supply
                print(output_message.format(input_amount_supply, self.__fuel_options[1], result))
            else:
                print(stock_error_message)

    def cash_supply_option(self):

        input_amount_supply = get_amount_supply()
        input_fuel_option = self.get_fuel_option()
        output_message = "The amount of fuel supplied is {}"

        if input_fuel_option == self.__fuel_options[0]:
            result = int(input_amount_supply / self.__alcohol_price)

            if self.__get_initial_stock_alcohol - result >= 0:
                self.__output_alcohol = self.__output_alcohol + result
                self.__get_initial_stock_alcohol = self.__get_initial_stock_alcohol - result
                print(output_message.format(result))
            else:
                print(stock_error_message)

        elif input_fuel_option == self.__fuel_options[1]:
            result = int(input_amount_supply / self.__gasoline_price)

            if self.__get_initial_stock_gasoline - result >= 0:
                self.__output_gasoline = self.__output_gasoline + result
                self.__get_initial_stock_gasoline = self.__get_initial_stock_gasoline - result
                print(output_message.format(result))
            else:
                print(stock_error_message)

    def supply(self):

        supply = self.get_supply_option()

        if supply == self.__supply_options[0]:
            self.cash_supply_option()

        elif supply == self.__supply_options[1]:
            self.liter_supply_option()
