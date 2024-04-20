def get_number():
    numbers = input("Enter some numbers with space: ")
    
    list_ = numbers.split()
    
    initial_list = []
    for i in list_:
        string_ = int(i)
        initial_list.append(string_)
    
    return initial_list

def save_numbers(numbers, filename):
    with open(filename, 'w') as file:
        for num in numbers:
            file.write(f"{num}\n")
            
            
   