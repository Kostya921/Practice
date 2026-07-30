#97
'''n = 20
m = 5

father_age = 0
son_age = 0

son_age += m
while father_age != son_age * m and son_age != father_age - n:
    father_age = n + son_age


print(f"{father_age} {son_age}")'''


#199

'''ticket_number1 = "156012"
ticket_number2 = "122005"
ticket_number3 = "045090"

tickets = [ticket_number1, ticket_number2, ticket_number3]

for ticket in tickets:
    if int(ticket[0]) + int(ticket[1]) + int(ticket[2]) == int(ticket[3]) + int(ticket[4]) + int(ticket[5]):
        print("Happy")
    else:
        print("Ordinary")'''





#303

'''a = 1
b = 20

for i in range(a, b+1):
    while i % 2 == 0:
        print(i, end=' ')
        break'''






#398
'''
def letter_to_number(letter):
    if letter.upper() == "I":
        return 1
    elif letter.upper() == "V":
        return 5
    elif letter.upper() == "X":
        return 10
    elif letter.upper() == "L":
        return 50
    elif letter.upper() == "C":
        return 100
    elif letter.upper() == "D":
        return 500
    elif letter.upper() == "M":
        return 1000



# 1 ≤ N ≤ 3999

num1 = "MMMCMXCIX"
num2 = "IV"
num3 = "XXI"

numbers = [num1, num2, num3]


for number in numbers:
    result = 0
    skipNextIter = False


    for i in range(len(number)):


        current_letter = number[i]
        try:
            next_letter = number[i + 1]
        except IndexError:
            next_letter = ""

        #print(type(next_letter), type(current_letter))
        #print(letter_to_number(next_letter), letter_to_number(current_letter))


        if skipNextIter:
            skipNextIter = False
            continue


        if next_letter != "":
            if current_letter != next_letter and letter_to_number(next_letter) > letter_to_number(current_letter):

                result += letter_to_number(next_letter) - letter_to_number(current_letter)
                skipNextIter = True

            else:
                result += letter_to_number(current_letter)

        else:
            result += letter_to_number(current_letter)

        #print("res =", result)
        #print()

    print(result)
    #print()


'''




#503

'''
def letter_to_number(letter):
    if letter.upper() == "I":
        return 1
    elif letter.upper() == "V":
        return 5
    elif letter.upper() == "X":
        return 10
    elif letter.upper() == "L":
        return 50
    elif letter.upper() == "C":
        return 100
    elif letter.upper() == "D":
        return 500
    elif letter.upper() == "M":
        return 1000



# 1 ≤ N ≤ 3999
n = input("Введіть число у римській системі числення або залиште рядок порожнім: ")

num1 = "MCMLXXXI"
num2 = "XXI"
num3 = "IV"

if not n:
    numbers = [num1, num2, num3]
else:
    numbers = [n]


for number in numbers:
    result = []
    skipNextIter = False


    for i in range(len(number)):


        current_letter = number[i]
        try:
            next_letter = number[i + 1]
        except IndexError:
            next_letter = ""


        if skipNextIter:
            skipNextIter = False
            continue


        if next_letter != "":
            if current_letter != next_letter and letter_to_number(next_letter) > letter_to_number(current_letter):

                result.append(letter_to_number(next_letter) - letter_to_number(current_letter))
                skipNextIter = True

            else:
                result.append(letter_to_number(current_letter))

        else:
            result.append(letter_to_number(current_letter))


    print(sum(result))



'''





#603
'''
# 0 ≤ n ≤ 20000
n = input("Введіть кількість слів у словнику або залиште рядок порожнім: ")

words_dict = {}
exercise = ""

if not n:
    n = 4
    words_dict = {
        1: "cAnnot",
        2: "cannOt",
        3: "fOund",
        4: "pAge"}

    exercise = "thE pAge cAnnot be found"
else:


    for i in range(int(n)):
        word = input(f"Введіть слово {i+1} із словника з маленьких і великих латинських букв (не більше 30 символів): ")
        words_dict[i+1] = word





    # len(exercise) ≤ 300000
    # len(exercise[0, 1, 2, ...]) ≤ 30
    exercise = input("Введіть текст завдання: ")

    for char in exercise:
        if char in r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~""":
            exercise = exercise.replace(char, "")



mistakes = 0

for word in exercise.split():
    Pass = False
    capitals = 0

    #print(word in words_dict.values())

    if word in words_dict.values():
        Pass = True

    elif word not in words_dict.values():
        for char in word:
            if char.isupper() and char in "AEIOUY":
                capitals += 1
        if capitals == 1:
            Pass = True

    if Pass == False:
        mistakes += 1


print(mistakes)

'''




#703

'''
def letter_to_number(letter):
    if letter.upper() == "I":
        return 1
    elif letter.upper() == "V":
        return 5
    elif letter.upper() == "X":
        return 10
    elif letter.upper() == "L":
        return 50
    elif letter.upper() == "C":
        return 100
    elif letter.upper() == "D":
        return 500
    elif letter.upper() == "M":
        return 1000



# 1 ≤ N ≤ 3999
n = input("Введіть число у римській системі числення або залиште рядок порожнім: ")

num1 = "MCMLXXXI"
num2 = "XX"
num3 = "IX"

if not n:
    numbers = [num1, num2, num3]
else:
    numbers = [n]


for number in numbers:
    result = []
    skipNextIter = False


    for i in range(len(number)):


        current_letter = number[i]
        try:
            next_letter = number[i+1]
        except IndexError:
            next_letter = ""


        if skipNextIter:
            skipNextIter = False
            continue


        if next_letter != "":
            if current_letter != next_letter and letter_to_number(next_letter) > letter_to_number(current_letter):

                result.append(letter_to_number(next_letter) - letter_to_number(current_letter))
                skipNextIter = True

            else:
                result.append(letter_to_number(current_letter))

        else:
            result.append(letter_to_number(current_letter))


    print(sum(result))



'''





#795

'''
Correct_answers = {
    "A": (1, 3, 6, 10, 14),
    "B": (4, 7, 11, 15, 19),
    "C": (5, 8, 12, 13, 17),
    "D": (2, 9, 16, 18, 20),
}


with open("input1.txt", mode="r", encoding="UTF-8") as file1:
    f1_answers = file1.read()
    f1_answers = f1_answers.split("\n")


with open("input2.txt", mode="r", encoding="UTF-8") as file2:
    f2_answers = file2.read()
    f2_answers = f2_answers.split("\n")


results = [f1_answers, f2_answers]

correct_answers1 = []
correct_answers2 = []
wrong_answers1_indexes = []
wrong_answers2_indexes = []


for test in results:
    c = 1

    for answer in test:
        if answer == "A":
            if c in Correct_answers["A"]:
                if test == f1_answers:
                    correct_answers1.append(answer)
                else:
                    correct_answers2.append(answer)
            else:
                if test == f1_answers:
                    wrong_answers1_indexes.append(str(c))
                else:
                    wrong_answers2_indexes.append(str(c))
        elif answer == "B":
            if c in Correct_answers["B"]:
                if test == f1_answers:
                    correct_answers1.append(answer)
                else:
                    correct_answers2.append(answer)
            else:
                if test == f1_answers:
                    wrong_answers1_indexes.append(str(c))
                else:
                    wrong_answers2_indexes.append(str(c))
        elif answer == "C":
            if c in Correct_answers["C"]:
                if test == f1_answers:
                    correct_answers1.append(answer)
                else:
                    correct_answers2.append(answer)
            else:
                if test == f1_answers:
                    wrong_answers1_indexes.append(str(c))
                else:
                    wrong_answers2_indexes.append(str(c))
        elif answer == "D":
            if c in Correct_answers["D"]:
                if test == f1_answers:
                    correct_answers1.append(answer)
                else:
                    correct_answers2.append(answer)
            else:
                if test == f1_answers:
                    wrong_answers1_indexes.append(str(c))
                else:
                    wrong_answers2_indexes.append(str(c))
        c += 1


final_answers_and_fails = [
    (correct_answers1, wrong_answers1_indexes),
    (correct_answers2, wrong_answers2_indexes)
]

for checked_answers in final_answers_and_fails:
    if len(checked_answers[0]) >= 15:
        print("You passed")
    else:
        print("You failed")

    print(f"Correctly answerd question is {len(checked_answers[0])}")
    print(f"Incorrectly answerd question is {20 - len(checked_answers[0])}")
    print(f"Wrong answers {" ".join(checked_answers[1])}")


'''



#826

'''
class RomanToDecimal:
    def __init__(self, roman_numeral):
        self.roman_numeral = roman_numeral



    def convert_to_decimal(self):

        result = 0
        skipNextIter = False

        for i in range(len(self.roman_numeral)):

            current_letter = self.roman_numeral[i]
            try:
                next_letter = self.roman_numeral[i+1]
            except IndexError:
                next_letter = ""


            if skipNextIter:
                skipNextIter = False
                continue

            if next_letter != "":
                if current_letter != next_letter and letter_to_number(next_letter) > letter_to_number(current_letter):

                    result += letter_to_number(next_letter) - letter_to_number(current_letter)
                    skipNextIter = True

                else:
                    result += letter_to_number(current_letter)

            else:
                result += letter_to_number(current_letter)


        return result




def letter_to_number(letter):
    if letter.upper() == "I":
        return 1
    elif letter.upper() == "V":
        return 5
    elif letter.upper() == "X":
        return 10
    elif letter.upper() == "L":
        return 50
    elif letter.upper() == "C":
        return 100
    elif letter.upper() == "D":
        return 500
    elif letter.upper() == "M":
        return 1000




num1 = RomanToDecimal("MMCMLXXVI")
num2 = RomanToDecimal("LLL")
num3 = RomanToDecimal("IX")

print(num1.convert_to_decimal())
print(num2.convert_to_decimal())
print(num3.convert_to_decimal())

'''






#10*

'''
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests


latitude = 50.45
longitude = 30.52
start_year = 2021
end_year = 2025


def fetch_or_generate_data():
    """Отримує дані з Open-Meteo API або створює CSV з тестовими даними."""
    api_url = "https://archive-api.open-meteo.com/v1/archive"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "start_date": f"{start_year}-01-01",
        "end_date": f"{end_year}-12-31",
        "daily": "temperature_2m_mean",
        "timezone": "auto",
    }

    try:
        print("Завантаження даних з Open-Meteo API...")
        response = requests.get(api_url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        df = pd.DataFrame(
            {
                "date": pd.to_datetime(data["daily"]["time"]),
                "tavg": data["daily"]["temperature_2m_mean"],
            }
        )
        print("Дані успішно завантажені з API")

    except Exception as e:
        print(f"!!! Не вдалося отримати дані з API: {e}")
        print("Генеруємо тестовий CSV-файл з аналогічною структурою...")

        
        np.random.seed(42)
        dates = pd.date_range(
            start=f"{start_year}-01-01", end=f"{end_year}-12-31", freq="D"
        )
        day_of_year = dates.dayofyear

        
        tavg = (
            11
            + 12 * np.sin((day_of_year - 100) * 2 * np.pi / 365)
            + np.random.normal(0, 2.5, len(dates))
            + (dates.year - start_year) * 0.25
        )

        df = pd.DataFrame({"date": dates, "tavg": np.round(tavg, 1)})
        df.to_csv("daily_temperatures.csv", index=False)
        print("Тестовий файл 'daily_temperatures.csv' створено.")

    return df



df_raw = fetch_or_generate_data()

df_veg = df_raw[df_raw["date"].dt.month.between(4, 10)].copy()

df_clean = df_veg.dropna(subset=["tavg"]).copy()

df_clean = df_clean[
    (df_clean["tavg"] >= -20) & (df_clean["tavg"] <= 45)
].copy()

df_clean["year"] = df_clean["date"].dt.year
df_clean["month"] = df_clean["date"].dt.month


active_temps = df_clean[df_clean["tavg"] > 10]
sat_by_year = (active_temps.groupby("year")["tavg"].sum().round(1).reset_index())
sat_by_year.columns = ["Рік", "САТ (°C)"]


sat_by_year.to_csv("sat_summary.csv", index=False)

print("\n" + "=" * 40)
print(" ТАБЛИЦЯ СУМИ АКТИВНИХ ТЕМПЕРАТУР (САТ)")
print("=" * 40)
print(sat_by_year.to_string(index=False))
print("=" * 40 + "\n")


years = sat_by_year["Рік"].values
sat_values = sat_by_year["САТ (°C)"].values


slope, intercept = np.polyfit(years, sat_values, 1)
trend_values = slope * years + intercept


fig, axes = plt.subplots(1, 3, figsize=(18, 5.5), tight_layout=True)
month_names = ["Квiт", "Трав", "Черв", "Лип", "Серп", "Верес", "Жовт"]


monthly_avg = df_clean.groupby(["month", "year"])["tavg"].mean().unstack()
for year in monthly_avg.columns:
    axes[0].plot(
        month_names,
        monthly_avg[year],
        marker="o",
        linewidth=2,
        label=str(year),
    )

axes[0].set_title("1. Динаміка середньомісячних температур\n(Квітень–Жовтень)", fontsize=11)
axes[0].set_ylabel("Середня температура (°C)")
axes[0].grid(True, linestyle="--", alpha=0.6)
axes[0].legend(title="Рік", loc="best")


bars = axes[1].bar(
    sat_by_year["Рік"].astype(str),
    sat_by_year["САТ (°C)"],
    color="#4C72B0",
    edgecolor="black",
    width=0.55,
)

axes[1].set_title("2. Сума активних температур (САТ > 10°C)\nпо роках", fontsize=11)
axes[1].set_ylabel("САТ (°C)")
axes[1].set_xlabel("Рік")
axes[1].grid(axis="y", linestyle="--", alpha=0.6)


for bar in bars:
    yval = bar.get_height()
    axes[1].text(
        bar.get_x() + bar.get_width() / 2.0,
        yval + 15,
        f"{yval:.0f}",
        ha="center",
        va="bottom",
        fontsize=9,
    )


axes[2].plot(
    years,
    sat_values,
    "ro-",
    linewidth=2,
    markersize=7,
    label="Фактичний САТ",
)

axes[2].plot(
    years,
    trend_values,
    "b--",
    linewidth=2,
    label=f"Лінійний тренд\n(y = {slope:.1f}x + {intercept:.0f})",
)

axes[2].set_title("3. Лінійний тренд САТ", fontsize=11)
axes[2].set_xlabel("Рік")
axes[2].set_ylabel("САТ (°C)")
axes[2].set_xticks(years)
axes[2].grid(True, linestyle="--", alpha=0.6)
axes[2].legend(loc="best")

# Збереження у файл
output_img = "agro_analysis.png"
plt.savefig(output_img, dpi=300)
plt.close()
print(f"Графіки збережено у файл '{output_img}'.")


max_year = sat_by_year.loc[sat_by_year["САТ (°C)"].idxmax()]
min_year = sat_by_year.loc[sat_by_year["САТ (°C)"].idxmin()]

trend_text = (
    "позитивний (спостерігається тенденція до потепління)"
    if slope > 0
    else "негативний (спостерігається тенденція до похолодання)"
)

print("\n--- КОРОТКИЙ АГРОКЛІМАТИЧНИЙ ВИСНОВОК ---")
print(f"1. Динаміка тренду: Кутовий коефіцієнт (slope) = {slope:.2f}. Тренд САТ {trend_text}.")
print(f"2. Найтепліший вегетаційний період: {int(max_year['Рік'])} рік (САТ = {max_year['САТ (°C)']} °C).")
print(f"3. Найхолодніший вегетаційний період: {int(min_year['Рік'])} рік (САТ = {min_year['САТ (°C)']} °C).")
print(f"4. Амплітуда коливань САТ за 5 років складає {max_year['САТ (°C)'] - min_year['САТ (°C)']:.1f} °C.")



'''






