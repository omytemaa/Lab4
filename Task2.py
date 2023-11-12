
import json
import csv

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:

    with open(INPUT_FILENAME, 'r',newline='') as file:
        reader = csv.DictReader(file)
        dannie = [row for row in reader]
    json_dannie = json.dumps(dannie, indent=4)
    with open(OUTPUT_FILENAME, 'w') as json_file:
        json_file.write(json_dannie)





if __name__ == '__main__':
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
