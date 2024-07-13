def get_cats_info(path):
    cats_info = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                id, name, age = line.split(',')
                cat_info = {
                    "id": id,
                    "name": name,
                    "age": int(age)
                }
                cats_info.append(cat_info)
    except FileNotFoundError:
        print(f"Error: File {path} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return cats_info

cats_list = get_cats_info('cats.txt')
print(cats_list)
