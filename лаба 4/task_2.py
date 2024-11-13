import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task(input_filename, output_filename) -> None:
    result = []
    with open(input_filename) as file:  # TODO считать содержимое csv файла
        data = csv.DictReader(file)
        for row in data:
            result.append(row)
    with open(output_filename, 'w') as file:
        json.dump(result, file, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task(INPUT_FILENAME, OUTPUT_FILENAME)

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
