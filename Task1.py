
import json
def task() -> float:
    with open("input.json","r") as input_file:
        dannie = json.load(input_file)
    summ = sum(item["score"]*item["weight"] for item in dannie)
    summ = round(summ,3)
    return summ
task()



print(task())
