participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"


def find_common_participants(str_1, str_2):
    list_1 = str_1.split('|')
    list_2 = str_2.split('|')
    list_1_2 = list()
    for i in range(len(list_1)):
        for j in range(len(list_2)):
            if list_1[i] == list_2[j]:
                list_1_2.append(list_1[i])
    return list_1_2


print(find_common_participants(participants_first_group,participants_second_group))
# str_1_2 = str_1 + str_2
# list_1_2 = str_1_2.split()
