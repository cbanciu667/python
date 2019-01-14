import sys
# Enter your code here. Read input from STDIN. Print output to STDOUT

lines = []
total_lines_input = 0

for line in sys.stdin:
    lines.append(line.rstrip())
    total_lines_input += 1
lines_count = int(lines[0])
phone_book = {}
pb_element = []
for inputs in range(1, lines_count+1):
    pb_element_line = lines[inputs]
    pb_element = pb_element_line.split(" ")
    phone_book.update({pb_element[0]: pb_element[1]})
for search_item_counter in range (lines_count+1,total_lines_input):
    if lines[search_item_counter] in phone_book:
        name = lines[search_item_counter]
        phone_number = phone_book.get(lines[search_item_counter])
        response = name + '=' + phone_number
        response.strip()
        print(response)
    else:
        print('Not found')
