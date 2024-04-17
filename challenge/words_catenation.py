def words_catenation(words_list: list) -> str:
    words_list[-1] = 'and ' + words_list[-1]
    return ', '.join(words_list)

if __name__ == "__main__":
    fruits = ['apples', 'bananas', 'oranges', 'lemons', 'pears']
    print(words_catenation(fruits))