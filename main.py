import tkinter as tk
from tkinter import messagebox

from szjb_sajat_modul import (
    SZJBFitnessCalculator,
    kg_to_lbs,
    lbs_to_kg,
    cm_to_feet,
    inches_to_cm,
    round_result,
    round_up,
    szjb_round_down,
    save_data,
    load_statistics
)


measurement_system = None

current_weight = None
current_bmi = None
current_bmr = None


def choose_eu():
    global measurement_system

    measurement_system = "EU"

    unit_window.destroy()
    create_main_window()


def choose_usa():
    global measurement_system

    measurement_system = "USA"

    unit_window.destroy()
    create_main_window()


def calculate():
    global current_weight
    global current_bmi
    global current_bmr

    try:
        weight_input = float(weight_entry.get())
        height_input = float(height_entry.get())
        age = int(age_entry.get())

        if weight_input <= 0 or height_input <= 0 or age <= 0:
            messagebox.showerror(
                "Error",
                "Please enter positive values."
            )
            return

        if measurement_system == "EU":
            weight_kg = weight_input
            height_cm = height_input

        else:
            weight_kg = lbs_to_kg(weight_input)
            height_cm = inches_to_cm(height_input)

        calculator = SZJBFitnessCalculator(
            weight_kg,
            height_cm,
            age
        )

        bmi = round_result(
            calculator.calculate_bmi()
        )

        bmr = round_result(
            calculator.calculate_bmr()
        )

        ideal_weight = round_result(
            calculator.calculate_ideal_weight()
        )

        weight_lbs = round_result(
            kg_to_lbs(weight_kg)
        )

        height_feet = round_result(
            cm_to_feet(height_cm)
        )

        bmr_up = round_up(bmr)
        bmr_down = szjb_round_down(bmr)

        current_weight = weight_kg
        current_bmi = bmi
        current_bmr = bmr

        save_data(
            weight_kg,
            height_cm,
            age,
            bmi,
            bmr
        )

        if measurement_system == "EU":

            result_label.config(
                text=
                f"BMI: {bmi}\n"
                f"BMR: {bmr} kcal\n"
                f"BMR rounded up: {bmr_up} kcal\n"
                f"BMR rounded down: {bmr_down} kcal\n"
                f"Ideal weight: {ideal_weight} kg\n"
                f"Weight in pounds: {weight_lbs} lbs\n"
                f"Height in feet: {height_feet} ft"
            )

        else:

            ideal_weight_lbs = round_result(
                kg_to_lbs(ideal_weight)
            )

            result_label.config(
                text=
                f"BMI: {bmi}\n"
                f"BMR: {bmr} kcal\n"
                f"BMR rounded up: {bmr_up} kcal\n"
                f"BMR rounded down: {bmr_down} kcal\n"
                f"Ideal weight: {ideal_weight_lbs} lbs\n"
                f"Weight in kg: {round_result(weight_kg)} kg\n"
                f"Height in cm: {round_result(height_cm)} cm"
            )

    except ValueError:

        messagebox.showerror(
            "Error",
            "Please enter valid numbers."
        )


def show_statistics():
    statistics = load_statistics()

    if statistics is None:

        messagebox.showinfo(
            "Statistics",
            "No valid saved data is available yet."
        )

        return

    average_weight_kg = round_result(
        statistics["average_weight"]
    )

    average_bmi = round_result(
        statistics["average_bmi"]
    )

    average_bmr = round_result(
        statistics["average_bmr"]
    )

    if measurement_system == "EU":

        text = (
            f"Number of records: {statistics['count']}\n\n"
            f"Average weight: {average_weight_kg} kg\n"
            f"Average BMI: {average_bmi}\n"
            f"Average BMR: {average_bmr} kcal"
        )

        if current_weight is not None:

            weight_difference = round_result(
                current_weight - average_weight_kg
            )

            bmi_difference = round_result(
                current_bmi - average_bmi
            )

            bmr_difference = round_result(
                current_bmr - average_bmr
            )

            text += "\n\nCurrent result compared to average:\n\n"

            if weight_difference > 0:
                text += (
                    f"Your weight is {weight_difference} kg "
                    f"above the average.\n"
                )

            elif weight_difference < 0:
                text += (
                    f"Your weight is {abs(weight_difference)} kg "
                    f"below the average.\n"
                )

            else:
                text += "Your weight is exactly the average.\n"

            if bmi_difference > 0:
                text += (
                    f"Your BMI is {bmi_difference} "
                    f"above the average.\n"
                )

            elif bmi_difference < 0:
                text += (
                    f"Your BMI is {abs(bmi_difference)} "
                    f"below the average.\n"
                )

            else:
                text += "Your BMI is exactly the average.\n"

            if bmr_difference > 0:
                text += (
                    f"Your BMR is {bmr_difference} kcal "
                    f"above the average."
                )

            elif bmr_difference < 0:
                text += (
                    f"Your BMR is {abs(bmr_difference)} kcal "
                    f"below the average."
                )

            else:
                text += "Your BMR is exactly the average."

    else:

        average_weight_lbs = round_result(
            kg_to_lbs(average_weight_kg)
        )

        text = (
            f"Number of records: {statistics['count']}\n\n"
            f"Average weight: {average_weight_lbs} lbs\n"
            f"Average BMI: {average_bmi}\n"
            f"Average BMR: {average_bmr} kcal"
        )

        if current_weight is not None:

            current_weight_lbs = kg_to_lbs(
                current_weight
            )

            weight_difference_lbs = round_result(
                current_weight_lbs - average_weight_lbs
            )

            bmi_difference = round_result(
                current_bmi - average_bmi
            )

            bmr_difference = round_result(
                current_bmr - average_bmr
            )

            text += "\n\nCurrent result compared to average:\n\n"

            if weight_difference_lbs > 0:
                text += (
                    f"Your weight is {weight_difference_lbs} lbs "
                    f"above the average.\n"
                )

            elif weight_difference_lbs < 0:
                text += (
                    f"Your weight is {abs(weight_difference_lbs)} lbs "
                    f"below the average.\n"
                )

            else:
                text += "Your weight is exactly the average.\n"

            if bmi_difference > 0:
                text += (
                    f"Your BMI is {bmi_difference} "
                    f"above the average.\n"
                )

            elif bmi_difference < 0:
                text += (
                    f"Your BMI is {abs(bmi_difference)} "
                    f"below the average.\n"
                )

            else:
                text += "Your BMI is exactly the average.\n"

            if bmr_difference > 0:
                text += (
                    f"Your BMR is {bmr_difference} kcal "
                    f"above the average."
                )

            elif bmr_difference < 0:
                text += (
                    f"Your BMR is {abs(bmr_difference)} kcal "
                    f"below the average."
                )

            else:
                text += "Your BMR is exactly the average."

    messagebox.showinfo(
        "Statistics",
        text
    )


def create_main_window():
    global main_window
    global weight_entry
    global height_entry
    global age_entry
    global result_label

    main_window = tk.Tk()

    main_window.title(
        "Fitness Calculator"
    )

    main_window.geometry(
        "460x580"
    )

    title_label = tk.Label(
        main_window,
        text="Fitness Calculator",
        font=("Arial", 20)
    )

    title_label.pack(
        pady=20
    )

    system_label = tk.Label(
        main_window,
        text=f"Measurement system: {measurement_system}",
        font=("Arial", 11, "bold")
    )

    system_label.pack(
        pady=5
    )

    if measurement_system == "EU":

        weight_text = "Weight (kg):"
        height_text = "Height (cm):"

    else:

        weight_text = "Weight (lbs):"
        height_text = "Height (inches):"

    weight_label = tk.Label(
        main_window,
        text=weight_text
    )

    weight_label.pack()

    weight_entry = tk.Entry(
        main_window
    )

    weight_entry.pack(
        pady=5
    )

    height_label = tk.Label(
        main_window,
        text=height_text
    )

    height_label.pack()

    height_entry = tk.Entry(
        main_window
    )

    height_entry.pack(
        pady=5
    )

    age_label = tk.Label(
        main_window,
        text="Age:"
    )

    age_label.pack()

    age_entry = tk.Entry(
        main_window
    )

    age_entry.pack(
        pady=5
    )

    calculate_button = tk.Button(
        main_window,
        text="Calculate",
        command=calculate,
        width=18
    )

    calculate_button.pack(
        pady=15
    )

    statistics_button = tk.Button(
        main_window,
        text="Show Statistics",
        command=show_statistics,
        width=18
    )

    statistics_button.pack(
        pady=5
    )

    result_label = tk.Label(
        main_window,
        text="",
        font=("Arial", 11),
        justify="left"
    )

    result_label.pack(
        pady=20
    )

    main_window.mainloop()


unit_window = tk.Tk()

unit_window.title(
    "Choose Measurement System"
)

unit_window.geometry(
    "380x260"
)

title_label = tk.Label(
    unit_window,
    text="Fitness Calculator",
    font=("Arial", 20)
)

title_label.pack(
    pady=25
)

question_label = tk.Label(
    unit_window,
    text="Which measurement system would you like to use?",
    font=("Arial", 11)
)

question_label.pack(
    pady=10
)

eu_button = tk.Button(
    unit_window,
    text="EU - kg / cm",
    command=choose_eu,
    width=20,
    height=2
)

eu_button.pack(
    pady=8
)

usa_button = tk.Button(
    unit_window,
    text="USA - lbs / inches",
    command=choose_usa,
    width=20,
    height=2
)

usa_button.pack(
    pady=8
)

unit_window.mainloop()