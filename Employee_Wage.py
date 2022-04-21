import random


class Constants:
    IS_PRESENT = 2
    IS_PART_TIME = 1
    IS_ABSENT = 0
    WAGE_PER_HOUR = 20
    PART_TIME_HOURS = 4
    FULL_DAY_HOURS = 8
    MAX_WORKING_DAYS_PER_MONTH = 20

def get_work_hours():

    work_hrs = 0
    emp_check = random.randint(0,2)

    match emp_check:
        case Constants.IS_PRESENT:
            work_hrs = Constants.FULL_DAY_HOURS
        case Constants.IS_PART_TIME:
            work_hrs = Constants.PART_TIME_HOURS
        case Constants.IS_ABSENT:
            work_hrs = 0
    return work_hrs

monthly_emp_wage = 0
for i in range(1,Constants.MAX_WORKING_DAYS_PER_MONTH + 1):
    monthly_emp_wage += Constants.WAGE_PER_HOUR * get_work_hours()

print(f"Person earns {monthly_emp_wage} rupees this month")