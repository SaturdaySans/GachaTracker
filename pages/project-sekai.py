import streamlit as st
import math
import pandas as pd

# Variables
file_path = "pjsk-data.csv"

# Functions
def load_data():
    return pd.read_csv(file_path)

def save_data(data):
    data.to_csv(file_path, index=False)

def rates(pulls):
    loaded_data = load_data()
    
    # Ensure the CSV has correct columns
    if loaded_data.empty:
        loaded_data = pd.DataFrame(columns=["3rate", "4rate", "frate"])
    
    for i in range(1, pulls + 1):  # Start at 1 for natural counting
        thstars = round(i * 0.15, 2)
        fostars = round(i * 0.03, 2)
        festars = round(fostars * 0.4, 2)
        
        loaded_data.loc[len(loaded_data)] = [thstars, fostars, festars]
    
    save_data(loaded_data)
    
    st.title("Rates")
    st.write(f"Pulls: {pulls}")
    st.write(f"Featured 4 Stars: {festars}")
    st.write(f"4 Stars: {fostars}")
    st.write(f"3 Stars: {thstars}")
    st.write(f"Leftover Crystals: {leftover_crystal}")
    st.line_chart(loaded_data)

# Streamlit UI
st.title("---Project Sekai---")
crystal_count = st.number_input("Crystals", min_value=0, max_value=600000, step=300)
pulls = math.floor(crystal_count / 300)
leftover_crystal = crystal_count - pulls * 300
rates(pulls)

# new_event = pd.DataFrame([[event_title, event_start, event_end, event_resource]],
#                          columns=["title", "start", "end", "resourceId"])
# events = pd.concat([events, new_event], ignore_index=True)
# save_events(events) # Save events