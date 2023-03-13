# Employee payroll system program

class PayrollSystem:
    def calculate_payroll(self, employees):
        print('Calculating Employee Payroll Details')
        
        for employee in employees:
            print(f'Payroll for: {employee.id} - {employee.name}')
            print(f'-  Amount: {employee.calculate_payroll()}')
            print('')
            


class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        

class SalaryEmployee(Employee):
    def __init__(self, id, name, weekly_salary):
        super().__init__(id, name)
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary
    
class HourlyEmployee(Employee):
    def __init__(self, id, name, hours_worked, hour_rate):
        super().__init__(id, name)
        self.hours_worked = hours_worked
        self.hour_rate = hour_rate

    def calculate_payroll(self):
        return self.hours_worked * self.hour_rate
    
class CommissionEmployee(SalaryEmployee):
    def __init__(self, id, name, weekly_salary, commission):
        super().__init__(id, name, weekly_salary)
        self.commission = commission

    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.commission
    


s = SalaryEmployee(1, 'Dennis Mandela', 2500)
h = HourlyEmployee(2, 'Ian Kanake', 25, 20)
c = CommissionEmployee(3, 'Benard Nderi', 1500, 200)
payroll_system = PayrollSystem()
payroll_system.calculate_payroll([
    s,
    h,
    c
])