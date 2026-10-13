import random
import matplotlib.pyplot as m

print(10*"-","Блок 1: Симуляція умовної ймовірності",10*"-")
N = [100, 1000, 10000, 100000, 1000000]

pB = 0.30
pA_given_B = 0.70
pA_given_not_B = 0.10
pB_given_A_theor = 0.75

frequencies = []

print(f"{'N':<10} | {'P(A|B) (стат)':<15} | {'P(A|B) (теор)':<15} | {'Похибка':<15}")
print("-" * 60)

for n in N:
    count_B, count_A, count_A_and_B = 0, 0, 0 # Обнулення лічильників для нової вибірки
    
    for i in range(n):
        is_B = random.random() < pB
        if is_B:
            count_B += 1    # Фіксуємо настання B
            is_A = random.random() < pA_given_B
        else:
            is_A = random.random() < pA_given_not_B
            
        if is_A:
            count_A += 1    # Фіксуємо настання A
            if is_B:
                count_A_and_B += 1
                
    w_B_given_A = count_A_and_B / count_A if count_A > 0 else 0
    frequencies.append(w_B_given_A)
    error = abs(w_B_given_A - pB_given_A_theor)
    
    print(f"{n:<10} | {w_B_given_A:<15.5f} | {pB_given_A_theor:<15.5f} | {error:<15.5f}")

m.figure(figsize=(8, 5))# Графік
m.plot(N, frequencies, marker='o', color='blue', label='Статистична P(A|B)')
m.axhline(y=pB_given_A_theor, color='red', linestyle='--', label=f'Теорія ({pB_given_A_theor})')
m.xscale('log')
m.xlabel('Кількість симуляцій (N)')
m.ylabel('Ймовірність P(A|B)')
m.title('Блок 1: Збіжність умовної ймовірності P(A|B))')
m.legend()
m.grid(True, linestyle="--")
m.show()