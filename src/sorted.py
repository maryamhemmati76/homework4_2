def sort_numbers(input_,output_):
    with open(input_, 'r') as file:
        make_list = []
        for item in file:
            make_strip = item.strip()
            make_int = int(make_strip)
            make_list.append(make_int)    
            
    increase = sorted(make_list)
    decrease = sorted(make_list, reverse=True)  
    
    with open(output_, 'w') as file:
        file.write("sorted numbers in Ascending order:\n")
        for items in increase:
            file.write(f"{items}\n")
            
        file.write("\nsorted numbers in Descending order:\n")
        for items in decrease:
            file.write(f"{items}\n")
            
    print("numbers has been sorted")
        