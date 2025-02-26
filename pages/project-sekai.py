import streamlit as st
import math

#Variables

#Functions
def rates(pulls):
    three_stars = round(pulls*0.15,2)
    four_stars = round(pulls*0.03,2)
    st.write(f"Pulls: {pulls}")
    st.write(f"Four Stars: {four_stars}")
    st.write(f"Three Stars: {three_stars}")
    st.write(f"Leftover Crystals: {leftover_crystal}")


st.title("---Project Sekai---")
crystal_count = st.number_input("Crystals",min_value=0,max_value=600000,step=300)
pulls=math.floor(crystal_count/300)
leftover_crystal = crystal_count-pulls*300
rates(pulls)