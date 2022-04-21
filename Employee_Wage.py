import random

IS_PRESENT = 2
IS_PART_TIME = 1
IS_ABSENT = 0
WAGE_PER_HOUR = 20
FULL_DAY_HOUR = 8
PART_TIME_HOURS = 4

def get_work_hours():

    work_hrs = 0
    emp_check = random.randint(0,2)

    if emp_check == IS_PRESENT:
        work_hrs = FULL_DAY_HOUR
    elif emp_check == IS_PART_TIME:
        work_hrs == PART_TIME_HOURS
    else:
        work_hrs = 0
    return work_hrs

daily_emp_wage = WAGE_PER_HOUR * get_work_hours()
print(f"Person Earn  {daily_emp_wage} Rupees this day")

