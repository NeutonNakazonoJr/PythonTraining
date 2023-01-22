class PaymentCalculator:
    def __init__(self, work_hours, hour_value):
        self.__work_hours = int(work_hours)
        self.__hour_value = int(hour_value)

    def gross_salary(self):
        gross_salary = self.__work_hours * self.__hour_value

        return gross_salary

    def ir_calculator(self):
        ir = 11
        ir_discount = self.gross_salary() * ir / 100

        return ir_discount

    def inss_calculator(self):
        inss = 8
        inss_discount = self.gross_salary() * inss / 100

        return inss_discount

    def syndicate_discount(self):
        discount = 5
        syndicate_discount = self.gross_salary() * discount / 100

        return syndicate_discount

    def net_salary(self):

        net_salary = self.gross_salary() - self.ir_calculator() - self.inss_calculator() - self.syndicate_discount()

        return net_salary
