import pandas as pd
import matplotlib.pyplot as plt

def load_data():
    df = pd.read_csv("data/mppt_data.csv")
    df["Date"] = pd.to_datetime(df["Date"])
    return df

def remove_zero_yield_days(df):
    original_rows = len(df)
    df_clean = df[df["Yield(Wh)"] > 0]
    removed_rows = original_rows - len(df_clean)

    print("\nData Cleaning:")
    print("Original rows:", original_rows)
    print("Removed zero-yield days:", removed_rows)
    print("Remaining rows:", len(df_clean))
    return df_clean

def solar_summary(df):

    print("\nSolar Summary")
    print("----------------")

    print("Average daily yield (Wh):")
    print(df["Yield(Wh)"].mean())

    print("\nMaximum daily yield (Wh):")
    print(df["Yield(Wh)"].max())

    print("\nMinimum daily yield (Wh):")
    print(df["Yield(Wh)"].min())

    best_day = df.loc[df["Yield(Wh)"].idxmax()]

    print("\nBest solar day:")
    print(best_day["Date"])
    print(best_day["Yield(Wh)"], "Wh")

    worst_day = df.loc[df["Yield(Wh)"].idxmin()]

    print("\nWorst solar day:")
    print(worst_day["Date"])
    print(worst_day["Yield(Wh)"], "Wh")

    total_energy = df["Yield(Wh)"].sum()

    print("\nTotal solar energy produced:")
    print(total_energy, "Wh")

def create_solar_plot(df):

    plt.figure(figsize=(12,5))

    plt.plot(
        df["Date"],
        df["Yield(Wh)"]
    )

    plt.title("Daily Solar Energy Production")
    plt.xlabel("Date")
    plt.ylabel("Energy (Wh)")

    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig("charts/daily_solar_yield.png")

    print("Solar chart created")    

def main():
    df = load_data()
    df_clean = remove_zero_yield_days(df)
    
    print("Victron MPPT Data")
    print("----------------")

    print("\nFirst rows:")
    print(df_clean.head())

    print("\nDataset size:")
    print(df_clean.shape)

    print("\nColumns:")
    print(df_clean.columns)

    solar_summary(df_clean)
    create_solar_plot(df_clean)


    


if __name__ == "__main__":
    main()

