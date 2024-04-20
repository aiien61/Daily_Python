#! /usr/bin/env python3
# print_nested_table.py - rotate nested list and print it out in a formatted way

def print_table(table_data: list):
    width = [0] * len(table_data)
    for idx, col in enumerate(table_data):
        width[idx] = max(len(value) for value in col)

    rows = len(table_data)
    columns = len(table_data[0])

    for col in range(columns):
        line = [table_data[i][col].rjust(width[i]) for i in range(rows)]
        print(' '.join(line))    

if __name__ == '__main__':
    table_data = [['apples', 'oranges', 'cherries', 'banana'],
                  ['Alice', 'Bob', 'Carol', 'David'],
                  ['dogs', 'cats', 'moose', 'goose']]
    print_table(table_data)