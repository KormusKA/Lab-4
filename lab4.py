class Item:
    def __init__(self, sign, weight, value):
        self.sign = sign
        self.weight = weight
        self.value = value

def knapsack(items, capacity):
    def node_bound_count(i, weight, value):
        if weight > capacity:
            return 0
        node_value = value
        j = i
        total_weight = weight

        while j < len(items) and total_weight + items[j].weight <= capacity:
            node_value += items[j].value
            total_weight += items[j].weight
            j += 1

        if j < len(items):
            node_value += (capacity - total_weight) * (items[j].value / items[j].weight)

        return node_value


    def branch_bound(i, weight, value):
        nonlocal max_value, combination

        if weight <= capacity and value > max_value:
            max_value = value
            combination = current_combination.copy()
        if i == len(items):
            return
        if node_bound_count(i, weight, value) > max_value:
            branch_bound(i + 1, weight, value)
        if value + (capacity - weight) * (items[i].value / items[i].weight) > max_value:
            for _ in range(items[i].weight):
                current_combination.append(items[i].sign)
            branch_bound(i + 1, weight + items[i].weight, value + items[i].value)
            for _ in range(items[i].weight):
                current_combination.pop()

    items = sorted(items, key=lambda x: x.value / x.weight, reverse=True)
    max_value = 0
    combination = [items[-1].sign]
    current_combination = [items[-1].sign]
    branch_bound(0, 1, 15+items[-1].value)
    for elem in items:
        if elem.sign not in combination:
            max_value -= elem.value
    return max_value, combination


if __name__ == '__main__':
    items = {Item('r',3,25), 
             Item('p',2,15), 
             Item('a',2,15), 
             Item('m',2,20), 
             Item('i',1,5), #обяз
             Item('k',1,15), 
             Item('x',3,20),
             Item('t',1,25),
             Item('f',1,15), 
             Item('d',1,10), 
             Item('s',2,20),
             Item('c',2,20)}
    
    capacity = 9
    max_value, combination = knapsack(items, capacity)

    bag = [[''  for _ in range(3)] for _ in range(3)]
    ind = 0
    for symbol in combination:
        i = ind // 3
        j = ind % 3
        bag[i][j] = symbol
        ind += 1

    print(f'\nОчки выживания: {max_value}')
    print('\nТом возьмет с собой:')
    for row in bag:
        print(f"[{row[0]}] [{row[1]}] [{row[2]}]")


    print('\nДоп задание:')
    capacity = 7
    max_value, combination = knapsack(items, capacity)

    if max_value > 0:
        bag = [[''  for _ in range(2)] for _ in range(4)]
        ind = 0
        for symbol in combination:
            i = ind % 4
            j = ind // 4
            bag[i][j] = symbol
            ind += 1

        print(f'\nОчки выживания: {max_value}')
        print('\nТом возьмет с собой:')
        for row in bag:
            if row[1] == '':
                print(f'[{row[0]}]')
            else:
                print(f"[{row[0]}] [{row[1]}]")
    else:
        print(f'Том не выживет, при аналогичных условиях, но с инвентарем в 7 ячеек, ведь его очки выживания равны {max_value}\n')
