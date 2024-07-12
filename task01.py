def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        total = 0
        count = 0

        for line in lines:
            _, salary = line.strip().split(',')
            total += int(salary)
            count += 1

        average = total / count if count > 0 else 0

        return total, average

    except FileNotFoundError:
        print(f"Error: The file at {path} was not found.")
        return 0, 0

    except Exception as e:
        print(f"An error occurred: {e}")
        return 0, 0

# Приклад використання:
path_to_file = 'salaries.txt'
print(total_salary(path_to_file))
