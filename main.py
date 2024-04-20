from src.number_list import get_number , save_numbers
from src.sorted import sort_numbers

numbers = get_number()
save_numbers(numbers,"file_input.txt")

sort_numbers("file_input.txt", "file_sorted.txt" )