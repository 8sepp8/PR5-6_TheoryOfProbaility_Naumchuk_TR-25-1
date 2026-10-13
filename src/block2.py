import random
import matplotlib.pyplot as m

print(10*"-","Блок 2 (Варіант 1): Відмова маршрутизаторів",10*"-")
N = [100, 1000, 10000, 100000, 1000000]

p_Aheor = 0.15
p_Bheor = 0.10
p_AUB = 0.235  # теоретична ймовірність відмови хоча б одного

frequencies = []#список для розрахованої частоти

print(f"{'N':<10} | {'P(A U B) (стат)':<15} | {'P(A U B) (теор)':<15} | {'Похибка':<15}")
print("-" * 63)

for n in N:
    count_union = 0
    for i in range(n):
        is_A = random.random() < p_Aheor
        is_B = random.random() < p_Bheor
        if is_A or is_B:# перевірка умови
            count_union += 1# лічильник
            
    w_union = count_union / n# oбчислення статистичної частоти
    frequencies.append(w_union)
    error = abs(w_union - p_AUB)#повертає абсолютне число
    
    print(f"{n:<10} | {w_union:<15.5f} | {p_AUB:<15.5f} | {error:<15.5f}")

m.figure(figsize=(8, 5))# графік
m.plot(N, frequencies, marker='s', color='blue', label='Статистична P(A U B)')
m.axhline(y=p_AUB, color='red', linestyle='--', label=f'Теорія ({p_AUB})')
m.xscale('log')
m.xlabel('Кількість днів (N)')
m.ylabel('Ймовірність відмови P(A U B)')
m.title('Блок 2: Ймовірність відмови хоча б одного маршрутизатора')
m.legend()
m.grid(True, linestyle="--")
m.show()