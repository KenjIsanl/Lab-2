def enumerates(item_list, finds_item):
    index = 0
    for i in item_list:
        if i == finds_item:
            return index
        index += 1
    return None


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = enumerates(items_list, find_item)
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")

# неудачные и грустные попытки понять работу enumerate ... Первая идея как-то поприятнее. Внутри дефа уже нахожу индекс. 
def enumerates(item_list, start=0):
    index = start
    for elem in item_list:
        yield index, elem
        index += 1
    return None


# yield Как понимаю делает мне ненужную генерацию, но я это обошла распаковкой в 24 строке.
# Проблема во 2 вхождении и персике. help.


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for index_item, find_items, in enumerate(items_list):
    if find_items == 'банан' or find_items == 'груша' or find_items == 'персик' and [ind for ind, ele in items_list if
                                                                                     ele == 1]:
        if index_item is not None:
            print(f"Первое вхождение товара '{find_items}' имеет индекс {index_item}.")
        else:
            print(f"Товар '{find_items}' не найден в списке.")
