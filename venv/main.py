import pandas as pd
import matplotlib.pyplot as plt

# Завдання 1: Створення таблиці замовлень клієнтів
data = {
    'OrderID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'CustomerName': ['Іван', 'Марія', 'Петро', 'Іван', 'Ольга', 
                     'Марія', 'Петро', 'Ольга', 'Іван', 'Марія'],
    'Product': ['Ноутбук', 'Телефон', 'Навушники', 'Монітор', 'Клавіатура',
                'Миша', 'Ноутбук', 'Телефон', 'Навушники', 'Монітор'],
    'Category': ['Електроніка', 'Електроніка', 'Аксесуари', 'Електроніка', 'Аксесуари',
                 'Аксесуари', 'Електроніка', 'Електроніка', 'Аксесуари', 'Електроніка'],
    'Quantity': [1, 2, 3, 1, 5, 10, 1, 1, 2, 2],
    'Price': [25000, 15000, 500, 8000, 300, 200, 27000, 16000, 600, 8500],
    'OrderDate': ['2024-06-01', '2024-06-03', '2024-06-05', '2024-06-07', 
                  '2024-06-08', '2024-06-09', '2024-06-10', '2024-06-12', 
                  '2024-06-15', '2024-06-18']
}

# 1. Створення DataFrame та конвертація OrderDate у datetime
df = pd.DataFrame(data)
df['OrderDate'] = pd.to_datetime(df['OrderDate'])

print("=" * 80)
print("ПОЧАТКОВА ТАБЛИЦЯ:")
print("=" * 80)
print(df)
print()

# 2. Додавання стовпця TotalAmount
df['TotalAmount'] = df['Quantity'] * df['Price']

print("=" * 80)
print("ТАБЛИЦЯ З ДОДАНИМ СТОВПЦЕМ TotalAmount:")
print("=" * 80)
print(df)
print()

# 3. Статистика
print("=" * 80)
print("3. СТАТИСТИКА:")
print("=" * 80)

# a. Сумарний дохід магазину
total_revenue = df['TotalAmount'].sum()
print(f"a. Сумарний дохід магазину: {total_revenue} грн")

# b. Середнє значення TotalAmount
avg_amount = df['TotalAmount'].mean()
print(f"b. Середнє значення TotalAmount: {avg_amount:.2f} грн")

# c. Кількість замовлень по кожному клієнту
orders_per_customer = df['CustomerName'].value_counts()
print(f"c. Кількість замовлень по кожному клієнту:")
print(orders_per_customer)
print()

# 4. Замовлення з сумою > 500
print("=" * 80)
print("4. ЗАМОВЛЕННЯ З СУМОЮ БІЛЬШЕ 500 ГРН:")
print("=" * 80)
high_value_orders = df[df['TotalAmount'] > 500]
print(high_value_orders)
print()

# 5. Сортування за OrderDate у зворотному порядку
print("=" * 80)
print("5. ТАБЛИЦЯ, ВІДСОРТОВАНА ЗА ДАТОЮ (ЗВОРОТНИЙ ПОРЯДОК):")
print("=" * 80)
df_sorted = df.sort_values('OrderDate', ascending=False)
print(df_sorted)
print()

# 6. Замовлення з 5 по 10 червня включно
print("=" * 80)
print("6. ЗАМОВЛЕННЯ З 5 ПО 10 ЧЕРВНЯ ВКЛЮЧНО:")
print("=" * 80)
start_date = pd.to_datetime('2024-06-05')
end_date = pd.to_datetime('2024-06-10')
june_orders = df[(df['OrderDate'] >= start_date) & (df['OrderDate'] <= end_date)]
print(june_orders)
print()

# 7. Групування за Category (додаткове завдання)
print("=" * 80)
print("7. ГРУПУВАННЯ ЗА КАТЕГОРІЄЮ:")
print("=" * 80)
category_stats = df.groupby('Category').agg({
    'Quantity': 'sum',
    'TotalAmount': 'sum'
}).rename(columns={'Quantity': 'Кількість товарів', 'TotalAmount': 'Загальна сума продажів'})
print(category_stats)
print()

# 8. ТОП-3 клієнтів за загальною сумою покупок
print("=" * 80)
print("8. ТОП-3 КЛІЄНТІВ ЗА ЗАГАЛЬНОЮ СУМОЮ ПОКУПОК:")
print("=" * 80)
top_customers = df.groupby('CustomerName')['TotalAmount'].sum().sort_values(ascending=False).head(3)
print(top_customers)
print()

# ЗАВДАННЯ 2: Графіки
print("=" * 80)
print("ЗАВДАННЯ 2: ПОБУДОВА ГРАФІКІВ")
print("=" * 80)

# Підготовка даних для графіків
orders_by_date = df.groupby('OrderDate').size()
revenue_by_category = df.groupby('Category')['TotalAmount'].sum()

# Створення фігури з двома графіками
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))

# Графік 1: Кількість замовлень по датах
ax1.plot(orders_by_date.index, orders_by_date.values, marker='o', linewidth=2, markersize=8)
ax1.set_xlabel('Дата замовлення', fontsize=12)
ax1.set_ylabel('Кількість замовлень', fontsize=12)
ax1.set_title('Кількість замовлень по датах', fontsize=14, fontweight='bold')
ax1.grid(True, alpha=0.3)
ax1.tick_params(axis='x', rotation=45)

# Графік 2: Діаграма розподілу доходів по категоріях
colors = ['#FF6B6B', '#4ECDC4']
ax2.pie(revenue_by_category.values, labels=revenue_by_category.index, autopct='%1.1f%%',
        startangle=90, colors=colors, textprops={'fontsize': 11})
ax2.set_title('Розподіл доходів по категоріях', fontsize=14, fontweight='bold')

plt.tight_layout()
plt.savefig('orders_analysis.png', dpi=300, bbox_inches='tight')
print("Графіки збережено у файл 'orders_analysis.png'")
plt.show()

print("\n" + "=" * 80)
print("АНАЛІЗ ЗАВЕРШЕНО!")
print("=" * 80)