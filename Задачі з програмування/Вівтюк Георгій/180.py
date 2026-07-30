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

        # Генерація синтетичних даних
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
sat_by_year = (
    active_temps.groupby("year")["tavg"].sum().round(1).reset_index()
)
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
