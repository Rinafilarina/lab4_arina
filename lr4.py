items = [
    ('винтовка', 'r', 3, 25),
    ('пистолет', 'p', 2, 15), 
    ('боекомплект', 'a', 2, 15),
    ('аптечка', 'm', 2, 20), 
    ('нож', 'k', 1, 15), 
    ('топор', 'x', 3, 20), 
    ('оберег', 't', 1, 25), 
    ('фляжка', 'f', 1, 15), 
    ('еда', 's', 2, 20),  
    ('арбалет', 'c', 2, 20)
]
total = 25+15+15+20+15+20+25+15+20+20
rows=2
cols=4
capacity=rows*cols
score=15
n=10 #количество предметов без ингалятора и антидота, т.к. в моем варианте нет болезней
best_final=-10**10
best_combo = None


#делаю перебор, чтобы вывести все варианты (доп.задание)

def lay(combo):
    global best_final
    grid = [['.' for _ in range(cols)] for _ in range(rows)]
    best_combo.sort(key = lambda item: item[2])
    for name, symbol, volume, val in combo:
        placed = False
        for r in range(rows):
            for c in range(cols - volume + 1):
                if all(grid[r][c + k] == '.' for k in range(volume)):
                    for k in range(volume):
                        grid[r][c + k] = symbol
                    placed = True
                    break
            if placed:
                break
        if not placed:
            print(f"  ! не удалось разместить {name}") #не должно пригодиться
    return grid

def best_option():
    global best_final, best_combo
    flag=False #переменная, которая показывает, что вообще существует такая раскладка
    for mask in range(2**n):
        size=0 #заполненный объем в рюкзаке
        v=0 #сколько очков уже взяли
        combo=[]
        line = bin(mask)[2:].zfill(n) #строка из 0 и 1, где для каждого элемента 0 - не взяли, 1 - взяли
        for j in range(n):
            bit = line[j]
            if bit=='1':
                name, symbol, volume, val = items[j]
                size+=volume
                v+=val
                combo.append(items[j])
        if size>capacity: #если в этом варианте выбора предметов рюкзак переполнен
            continue
        final = v+score-(total-v)
        if final>best_final and final>0:
            best_final=final
            best_combo=combo
            flag=True

    if flag: 
        print(best_final)
        ans = lay(best_combo)
        for i in range(len(ans)):
            for j in range(len(ans[i])):
                print(ans[i][j], end=' ')
            print()
    else:
        print('Для этого варианта ёмкости нет подходящих раскладок')


print('Лучший вариант:')
best_option()

def all_lays(): #выводим все подходящие варианты
    print('Все варианты:')
    global best_final, best_combo
    for mask in range(2**n):
        size=0 #заполненный объем в рюкзаке
        v=0 #сколько очков уже взяли
        combo=[]
        line = bin(mask)[2:].zfill(n) #строка из 0 и 1, где для каждого элемента 0 - не взяли, 1 - взяли
        for j in range(n):
            bit = line[j]
            if bit=='1':
                name, symbol, volume, val = items[j]
                size+=volume
                v+=val
                combo.append(items[j])
        if size>capacity: #если в этом варианте выбора предметов рюкзак переполнен
            continue
        final = v+score-(total-v)
        if final==best_final:
            print(final)
            ans = lay(combo)
            for i in range(len(ans)):
                for j in range(len(ans[i])):
                    print(ans[i][j], end=' ')
                print()

print('Нажмите любую клавишу, чтобы вывести все варианты')
a = input()
all_lays()

print('Нажмите любую клавишу, чтобы уменьшить ёмкость до 7 единиц')
a=input()
capacity=7
best_final=-10**10
best_option()