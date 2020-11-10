# Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая
# строка должна содержать данные о фирме: название, форма собственности, выручка,
# издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также
# среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать .
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а
# также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в
# словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{ "firm_1" : 5000 , "firm_2" : 3000 , "firm_3" : 1000 }, { "average_profit" : 2000 }]
# Подсказка: использовать менеджер контекста.
import json

profit_firm = {}
loss_firm = {}
total_profit = 0

with open('company.txt', 'r+') as file:
    file_list = file.readlines()
    for firm in file_list:
        name, form, revenue, costs = firm.split()
        profit = round(float(revenue) - float(costs), 2)
        if profit < 0:
            loss_firm[name] = profit
        else:
            profit_firm[name] = profit
            total_profit += profit
        average_profit = round(total_profit, 2) / len(file_list)
    all_firm_list = [profit_firm, loss_firm, {'average_profit': round(average_profit, 2)}]
    print(all_firm_list)

with open('company.json', 'w', encoding='utf=8') as f:
    json.dump(all_firm_list, f)
