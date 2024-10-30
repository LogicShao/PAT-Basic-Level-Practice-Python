def f(salary):
    if salary < 0:
        raise ValueError('Invalid salary')
    if salary <= 3000:
        return 0.5 / 100 * salary
    if salary <= 5000:
        return 0.1 / 100 * salary
    if salary <= 10000:
        return 0.15 / 100 * salary
    return 2 / 100 * salary


salary = eval(input('请输入有固定工资收入的党员的月工资：'))
print('月工资 = {}，交纳党费 = {:.1f}'.format(salary, f(salary)))
