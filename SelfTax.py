import sys

def tax_indeed(salary):
    if salary <= 1500:
        return salary * 0.03
    elif salary > 1500 and salary <= 4500:
        return 0.03*1500 + (salary-1500)*0.1
    elif salary > 4500 and salary <= 9000:
        return 0.03*1500 + 0.1*3000 + (salary-4500)*0.2
    elif salary > 9000 and salary <= 35000:
        return 0.03*1500 + 0.1*3000 + 0.2*4500 + (salary-9000)*0.25
    elif salary > 35000 and salary <= 55000:
        return 0.03*1500 + 0.1*3000 + 0.2*4500 + 0.25*26000 + (salary-35000)*0.30
    elif salary > 55000 and salary <= 80000:
        return 0.03*1500 + 0.1*3000 + 0.2*4500 + 0.25*26000 + 0.30*20000 + (salary-55000)*0.35
    else:
        return 0.03*1500 + 0.1*3000 + 0.2*4500 + 0.25*26000 + 0.30*20000 + 0.35*25000 + (salary-80000)*0.45

def tax_dec(salary):
    former_tax = tax_indeed(salary-3500)
    latter_tax = tax_indeed(salary-5000)
    return former_tax-latter_tax


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: {} <salary>".format(sys.argv[0]))
        sys.exit(1)

    salary = float(sys.argv[1])
    dec = tax_dec(salary)
    print("工资总额: {}, 多拿: {}".format(salary, dec))