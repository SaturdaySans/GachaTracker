import streamlit as st
import math
import pandas as pd

#Variables
file_path = "pjsk-data.csv"


#Functions
def load_data():
    return pd.read_csv(file_path)

def save_data():
    data.to_csv(file_path)

def rates(pulls):
    three_stars = round(pulls*0.15,2)
    four_stars = round(pulls*0.03,2)
    featured_four_stars = round(four_stars * 0.4,2)
    st.title("Rates")
    st.write(f"Pulls: {pulls}")
    st.write(f"Featured 4 Stars: {featured_four_stars}")
    st.write(f"4 Stars: {four_stars}")
    st.write(f"3 Stars: {three_stars}")
    st.write(f"Leftover Crystals: {leftover_crystal}")
    st.write(load_data())


st.title("---Project Sekai---")
crystal_count = st.number_input("Crystals",min_value=0,max_value=600000,step=300)
pulls=math.floor(crystal_count/300)
leftover_crystal = crystal_count-pulls*300
rates(pulls)



#new_event = pd.DataFrame([[event_title, event_start, event_end, event_resource]],
                                 #columns=["title", "start", "end", "resourceId"])
        #events = pd.concat([events, new_event], ignore_index=True)
        #save_events(events) #Save events