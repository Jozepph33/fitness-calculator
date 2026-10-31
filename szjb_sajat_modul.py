import math
import csv
import os


class SZJBFitnessCalculator:
    def __init__(self, weight, height_cm, age):
        self.weight = weight
        self.height_cm = height_cm
        self.age = age

    def calculate_bmi(self):
        height_m = self.height_cm / 100
        return self.weight / math.pow(height_m, 2)

    def calculate_bmr(self):
        return 10 * self.weight + 6.25 * self.height_cm - 5 * self.age + 5

    def calculate_ideal_weight(self):
        height_m = self.height_cm / 100
        return 22 * math.pow(height_m, 2)


def kg_to_lbs(kg):
    return kg * 2.20462


def lbs_to_kg(lbs):
    return lbs / 2.20462


def cm_to_feet(cm):
    return cm / 30.48


def inches_to_cm(inches):
    return inches * 2.54


def round_result(value):
    return round(value, 2)


def round_up(value):
    return math.ceil(value)


def szjb_round_down(value):
    return math.floor(value)


def save_data(weight, height, age, bmi, bmr):
    file_name = "fitness_data.csv"
    file_exists = os.path.isfile(file_name)

    with open(file_name, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(
                ["weight_kg", "height_cm", "age", "bmi", "bmr"]
            )

        writer.writerow([
            round_result(weight),
            round_result(height),
            age,
            round_result(bmi),
            round_result(bmr)
        ])


def load_statistics():
    file_name = "fitness_data.csv"

    if not os.path.isfile(file_name):
        return None

    weights = []
    bmis = []
    bmrs = []

    with open(file_name, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            try:
                weight = float(row["weight_kg"])
                bmi = float(row["bmi"])
                bmr = float(row["bmr"])

                if weight <= 0 or weight > 500:
                    continue

                if bmi < 5 or bmi > 100:
                    continue

                if bmr < 500 or bmr > 10000:
                    continue

                weights.append(weight)
                bmis.append(bmi)
                bmrs.append(bmr)

            except (ValueError, KeyError):
                continue

    if len(weights) == 0:
        return None

    return {
        "count": len(weights),
        "average_weight": sum(weights) / len(weights),
        "average_bmi": sum(bmis) / len(bmis),
        "average_bmr": sum(bmrs) / len(bmrs)
    }