import random
import matplotlib.pyplot as m

print(10*"-","Блок 3: Надійність розподіленої веб-системи",10*"-")
N = [100, 1000, 10000, 100000, 1000000]

p1_lb = 0.98
p2_web1, p3_web2 = 0.90, 0.90
p4_db1, p5_db2 = 0.95, 0.95

p_sys_theor = 0.9677745
frequencies_sys = []

print(f"{'N':<10} | {'P_sys (стат)':<15} | {'P_sys (теор)':<15} | {'Похибка':<15}")
print("-" * 60)

for n in N:
    success_count = 0
    for i in range(n):# cимуляція кожного окремого компонента
        lb = random.random() < p1_lb# балансувальник навантаження
        web1 = random.random() < p2_web1# перший веб-сервер
        web2 = random.random() < p3_web2# другий веб-сервер
        db1 = random.random() < p4_db1# перша база даних
        db2 = random.random() < p5_db2# друга база даних
        
        if lb and (web1 or web2) and (db1 or db2):
            success_count += 1
            
    p_sys = success_count / n
    frequencies_sys.append(p_sys)
    error = abs(p_sys - p_sys_theor)
    
    print(f"{n:<10} | {p_sys:<15.6f} | {p_sys_theor:<15.6f} | {error:<15.6f}")

m.figure(figsize=(8, 5))
m.plot(N, frequencies_sys, marker='d', color='green', label='Надійність (Монте-Карло)')
m.axhline(y=p_sys_theor, color='red', linestyle='--', label=f'Точна надійність ({p_sys_theor:.4f})')
m.xscale('log')
m.xlabel('Кількість випробувань (N)')
m.ylabel('Надійність системи (P_sys)')
m.title('Блок 3: Збіжність надійності системи')
m.legend()
m.grid(True, linestyle="--")
m.show()