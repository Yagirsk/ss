import os
import time
import keyboard
import random
import asyncio
import aioconsole

low_mn = -50
high_mn = 50
sets_list = []

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def hide_cursor():
    print("\033[?25l", end='')

def show_cursor():
    print("\033[?25h", end='')

class Sets:
    def __init__(self, name: str):
        self.name = name
        self.elements = []

    @property
    def size(self) -> int:
        return len(self.elements)

    def add(self, value):
        self.elements.append(value)

    def update(self, values):
        self.elements.update(values)

    def remove(self, element):
        if element in self.elements:
            self.elements.remove(element)
        else:
            raise ValueError(f"Element {element} not found in the set")

    def contains(self, element) -> bool:
        return element in self.elements

    def __str__(self) -> str:
        elements_str = ', '.join(map(str, self.elements))
        return f"\t{self.name} = {{{elements_str}}} (Size: {self.size})"

def show_menu():
    clear_console()
    print('\n\n\t[1] - Ввести множество\n\t[2] - Калькулятор\n\t[3] - Показать множества\n\t[esc] - Выход')

def enter_self():
    keyboard.press_and_release('enter')
    input()
    clear_console()
    name = input("\n\n\tВведите название множества\n\t> ")
    
    clear_console()
    
    new_set = Sets(name)
    
    while True:
        try:
            print(new_set)
            element = input("\n\tВведите элемент (от -50 до 50, 'esc' + 'enter' для выхода): ")
        
            if keyboard.is_pressed('esc'):
                break
        
            num = int(element)
        
            if low_mn <= num <= high_mn:
                new_set.add(num)
            else:
                clear_console()
                print(f"\n\tОшибка: элемент должен быть от {low_mn} до {high_mn}")
                time.sleep(2)
    
        except ValueError:
            clear_console()
            print("\n\n\tОшибка: вводите только целые числа.")
            time.sleep(2)
        clear_console()
    
    sets_list.append(new_set)
    print(f"\tМножество '{name}' успешно создано!")
    time.sleep(2)
    keyboard.press_and_release('enter')
    input()
    show_menu()
    
def enter_rand():
    keyboard.press_and_release('enter')
    input()
    clear_console()
    name = input("\n\n\tВведите название множества\n\t> ")
    
    clear_console()
    
    new_set = Sets(name)
    
    while True:
        try:
            print(new_set)
            size_i = input("\n\tВведите количество элементов в можестве\n\t> ")
            
            size = int(size_i)
            
            if size<0:
                clear_console()
                print(f"\n\tОшибка: размер не может быть отрицательным")
                time.sleep(2)
            elif 0 <= size <= 101:
                sets = list(range(-50, 51))
                
                if size > len(sets):
                    clear_console()
                    print(f"\n\tОшибка: невозможно создать множество с заданным количеством элементов")
                    time.sleep(2)
                    continue
                
                selected_numbers = random.sample(sets, size) 
                
                for num in selected_numbers:
                    new_set.add(num)
                    sets.remove(num)
                
                clear_console()
                sets_list.append(new_set)
                print(f"\tМножество '{name}' успешно создано!")
                time.sleep(2)
                break
            else:
                clear_console()
                print(f"\n\tОшибка: невозможно создать множество с заданным количеством элементов")
                time.sleep(2)
        
        except ValueError:
            clear_console()
            print("\n\n\tОшибка: вводите только целые числа")
            time.sleep(2)
        clear_console()
    
    keyboard.press_and_release('enter')
    input()
    show_menu()
    
def enter_rule():
    keyboard.press_and_release('enter')
    input()
    clear_console()
    name = input("\n\n\tВведите название множества\n\t> ")

    new_set = Sets(name)
    conditions = []
    last_displayed_conditions = ""
    range_start = None
    range_end = None
    while True:
        current_conditions = ', '.join(conditions) if conditions else 'Нет условий'
        if current_conditions != last_displayed_conditions:
            clear_console()
            print(f"\n\tТекущие условия: {current_conditions}")
        
            print('\n\n\t[1] - Четные\n\t[2] - Нечетные\n\t[3] - Положительные\n\t[4] - Отрицательные\n\t[5] - Кратность числам')
        
            # Убираем кнопку добавления диапазона, если он уже установлен
            if range_start is None or range_end is None:
                print('\t[6] - Диапазон')
        
            print('\t[7] - Сбросить условия\n\t[esc] - Завершить ввод условий')
            last_displayed_conditions = current_conditions

        if keyboard.is_pressed('1'):
            time.sleep(0.1)
            if "Четные" not in conditions:
                conditions.append("Четные")
        elif keyboard.is_pressed('2'):
            time.sleep(0.1)
            if "Нечетные" not in conditions:
                conditions.append("Нечетные")
        elif keyboard.is_pressed('3'):
            time.sleep(0.1)
            if "Положительные" not in conditions:
                conditions.append("Положительные")
        elif keyboard.is_pressed('4'):
            time.sleep(0.1)
            if "Отрицательные" not in conditions:
                conditions.append("Отрицательные")
        elif keyboard.is_pressed('5'):
            clear_console()
            keyboard.press_and_release('enter')
            input()
            time.sleep(0.1)
            divisor = int(input("\n\tВведите число для кратности (положительное)\n\t> "))
            if divisor > 0:
                conditions.append(f"Кратные {divisor}")
            else:
                print("\n\tОшибка: число должно быть положительным.")
                time.sleep(2)
        elif keyboard.is_pressed('6') and (range_start is None or range_end is None):
            clear_console()
            keyboard.press_and_release('enter')
            input()
            time.sleep(0.1)
            while True:
                try:
                    start = int(input("\n\tВведите начало диапазона\n\t> "))
                    end = int(input("\n\tВведите конец диапазона\n\t> "))
                    if low_mn <= start <= high_mn and low_mn <= end <= high_mn:
                        if end >= start:
                            range_start, range_end = start, end
                            conditions.append(f"Диапазон от {range_start} до {range_end}")
                            break
                        else:
                            print("\n\tОшибка: конец диапазона должен быть больше или равен началу.")
                            time.sleep(2)
                    else:
                        print("\n\tОшибка: границы диапазона должны находиться в пределах универсума.")
                        time.sleep(2)
                except ValueError:
                    print("\n\tОшибка: неверный ввод диапазона.")
                    time.sleep(2)
        elif keyboard.is_pressed('7'):
            time.sleep(0.1)
            conditions.clear()
            range_start = None
            range_end = None
        elif keyboard.is_pressed('esc'):
            break
        
    universe = list(range(low_mn, high_mn + 1))
    for condition in conditions:
        print(f"Обрабатываем условие: {condition}")
        if condition == "Четные" and "Нечетные" not in conditions:
            universe = [num for num in universe if num % 2 == 0]
        elif condition == "Нечетные" and "Четные" not in conditions:
            universe = [num for num in universe if num % 2 != 0]
        elif condition == "Положительные" and "Отрицательные" not in conditions:
            universe = [num for num in universe if num >= 0]
        elif condition == "Отрицательные" and "Положительные" not in conditions:
            universe = [num for num in universe if num < 0]
        elif "Кратные" in condition:
            parts = condition.split()
            if len(parts) == 2 and parts[1].isdigit():
                divisor = int(parts[1])
                universe = [num for num in universe if num % divisor == 0]
            else:
                print("Ошибка: неверный формат условия 'Кратные'.")
    if range_start is not None and range_end is not None:
        universe = [num for num in universe if range_start <= num <= range_end]

    for i in universe:
        new_set.add(i)
                
    sets_list.append(new_set)

def enter_mn():
    clear_console()
    print('\n\n\t[1] - Задать вручную\n\t[2] - Задать случайно\n\t[3] - Задать по условиям\n\t[esc] - Назад')
    while True:
        if keyboard.is_pressed('1'):
            time.sleep(0.1)
            enter_self()
            break
        elif keyboard.is_pressed('2'):
            time.sleep(0.1)
            enter_rand()
            break
        elif keyboard.is_pressed('3'):
            time.sleep(0.1)
            enter_rule()
            break
        elif keyboard.is_pressed('esc'):
            time.sleep(0.1)
            break
    show_menu()

def calc_mn():
    clear_console()
    print('\n\n\t[1] - Пересечение\n\t[2] - Объединение\n\t[3] - Разность\n\t[4] - Дополнение до универсума\n\t[esc] - Назад')
    while True:
        if keyboard.is_pressed('1'):
            time.sleep(0.1)
            break
        elif keyboard.is_pressed('2'):
            time.sleep(0.1)
            break
        elif keyboard.is_pressed('3'):
            time.sleep(0.1)
            break
        elif keyboard.is_pressed('4'):
            time.sleep(0.1)
            break
        elif keyboard.is_pressed('esc'):
            time.sleep(0.1)
            break
    show_menu()

def print_sets():
    clear_console()
    print("\n\n\t'esc' для выхода")
    if sets_list:
        for s in sets_list:
            print(s)
    else:
        print("\tНет доступных множеств")
        
    while True:
        if keyboard.is_pressed('esc'):
            break
            
        
    
    clear_console()
    show_menu()

def main_menu():
    hide_cursor()
    show_menu()
    while True:
        if keyboard.is_pressed('1'):
            time.sleep(0.1)
            enter_mn()
        elif keyboard.is_pressed('2'):
            time.sleep(0.1)
            calc_mn()
        elif keyboard.is_pressed('3'):
            time.sleep(0.1)
            print_sets()    
        elif keyboard.is_pressed('esc'):
            time.sleep(0.1)
            clear_console()
            break
        time.sleep(0.1)
    show_cursor()

if __name__ == "__main__":
    main_menu()
