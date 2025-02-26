import streamlit as st
import math


def rates(crystal_count):
    three_stars = crystal_count/300*0.15
    four_stars = crystal_count/300*0.03
    st.write(f"""
Four Stars: {four_stars}
Three Stars: {three_stars}
             """)


st.title("---Project Sekai---")
crystal_count = st.number_input("Crystals",step=300)