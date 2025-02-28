import streamlit as st
import math
import pandas as pd

# Variables
file_path = "pjsk-data.csv"

# Function
def rates(pulls):
    # Ensure the CSV has correct columns
    loaded_data = pd.DataFrame(columns=["3rate", "4rate", "frate"])
    
    three_stars = round(pulls*0.15,2)
    four_stars = round(pulls*0.03,2)
    featured_four_stars = round(four_stars * 0.4,2)

    for i in range(1, pulls + 1):  # Start at 1 for natural counting
        thstars = round(i * 0.15, 2)
        fostars = round(i * 0.03, 2)
        festars = round(fostars * 0.4, 2)
        
        loaded_data.loc[len(loaded_data)] = [thstars, fostars, festars]
    
    
    st.title("Rates")
    st.write(f"Pulls: {pulls}")
    st.write(f"Featured 4 Stars: {featured_four_stars}")
    st.write(f"4 Stars: {four_stars}")
    st.write(f"3 Stars: {three_stars}")
    st.write(f"Leftover Crystals: {leftover_crystal}")
    n = st.checkbox("Display Three Stars")
    if n:
        st.line_chart(loaded_data)
    else:
        loaded_data = loaded_data.drop(columns=["3rate"])
        loaded_data = loaded_data[]

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