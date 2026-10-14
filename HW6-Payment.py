class FullTimeEmployee:
    def __init__(self, payroll):
        self.payroll = payroll

    def calculate_payment(self):
        return self.payroll

class HourlyEmployee:
    def __init__(self, hours_worked, hourly_rate):
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_payment(self):
        return self.hours_worked * self.hourly_rate

def process_payment(worker):
    Amount = worker.calculate_payment()
    print(f'Pay ${Amount} to {worker.__class__.__name__}')

FullTimeWorker = FullTimeEmployee(18000)
HourlyWorker = HourlyEmployee(40, 150)

process_payment(FullTimeWorker)
process_payment(HourlyWorker)