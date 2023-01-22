
class WageAdjustment:
    def __init__(self, sector, salary):
        self.__sector = sector
        self.__salary = salary
        self.__adjustment = 0
        self.__adjusted_salary = 0

    def adjustment_salary_conditions(self):

        adjustment_salary = 0

        if self.__salary <= 500:
            adjustment_salary = self.__salary * 20 / 100

        elif 500 < self.__salary <= 1000:
            adjustment_salary = self.__salary * 10 / 100

        elif self.__salary > 1000:
            adjustment_salary = self.__salary * 5 / 100

        self.__adjustment = int(adjustment_salary)

    def adjusted_salary(self):
        adjusted_salary = self.__salary + self.__adjustment

        self.__adjusted_salary = int(adjusted_salary)
