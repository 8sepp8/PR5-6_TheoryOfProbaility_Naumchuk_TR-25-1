import random
import matplotlib.pyplot as m

print(10*"-","Блок 4 (Варіант 4): Перевірка Failover у кластері БД",10*"-")
N = [100, 1000, 10000, 100000, 1000000]

p1 = 0.95
ps = 0.90
p2 = 0.90

p_theor = 0.9905 # точна теорія: p1 + (1-p1)* ps * p2
frequencies = []

print(f"{'N':<10} | {'P_failover (стат)':<18} | {'P (теор)':<10} | {'Похибка':<10}")
print("-" * 60)

for n in N:
    success_count = 0
    for i in range(n):#перевірка основної бази даних
        if random.random() < p1:
            success_count += 1#фіксуємо успішну роботу системи
        else:
            if random.random() < ps and random.random() < p2:
                success_count += 1# фіксуємо якщо стався збій
                
    w_stat = success_count / n
    frequencies.append(w_stat)
    error = abs(w_stat - p_theor)
    
    print(f"{n:<10} | {w_stat:<18.5f} | {p_theor:<10.5f} | {error:<10.5f}")

m.figure(figsize=(8, 5))
m.plot(N, frequencies, marker='.', color='purple', label='Успіх Failover (стат)')
m.axhline(y=p_theor, color='red', linestyle='--', label=f'Теорія ({p_theor})')
m.xscale('log')
m.xlabel('Кількість сесій (N)')
m.ylabel('Ймовірність безперебійної роботи')
m.title('Блок 4: Ефективність системи резервування (Failover)')
m.legend()
m.grid(True, linestyle="--")
m.show()