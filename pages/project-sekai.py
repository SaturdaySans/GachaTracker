import streamlit as st
import math
import pandas as pd

# Variables
file_path = "pjsk-data.csv"

# Functions
def load_data():
    return pd.read_csv(file_path)

def save_data(data):
    data.to_csv(file_path, index=False)  # Save the updated data properly

def rates(pulls):
    three_stars = round(pulls * 0.15, 2)
    four_stars = round(pulls * 0.03, 2)
    featured_four_stars = round(four_stars * 0.4, 2)

    loaded_data = load_data()  # Load existing CSV

    # Ensure loaded_data has the correct columns
    if loaded_data.empty:
        loaded_data = pd.DataFrame(columns=["3rate", "4rate", "frate"])

    for i in range(pulls):
        thstars = round(i * 0.15, 2)
        fostars = round(i * 0.03, 2)
        festars = round(fostars * 0.4, 2)
        loaded_data.loc[len(loaded_data)] = [thstars, fostars, festars]  # FIXED!

    save_data(loaded_data)  # Now correctly saving data

    # Display the results
    st.title("Rates")
    st.write(f"Pulls: {pulls}")
    st.write(f"Featured 4 Stars: {featured_four_stars}")
    st.write(f"4 Stars: {four_stars}")
    st.write(f"3 Stars: {three_stars}")
    st.write(f"Leftover Crystals: {leftover_crystal}")
    st.line_chart(loaded_data)  # Correct variable passed
  

# --- Streamlit App ---
st.title("---Project Sekai---")
crystal_count = st.number_input("Crystals", min_value=0, max_value=600000, step=300)
pulls = math.floor(crystal_count / 300)
leftover_crystal = crystal_count - pulls * 300
rates(pulls)
