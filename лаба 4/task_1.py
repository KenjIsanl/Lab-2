import json


# TODO решите задачу


def task(_) -> float:
    with open('input.json') as file:
        data = json.load(file)
    data_sum = sum(item['score'] * item['weight'] for item in data)
    return round(data_sum, 3)


print(task('input.json'))
