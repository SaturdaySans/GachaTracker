import streamlit as st
import math


def rates(crystal_count):
    three_stars = round(crystal_count/300*0.15,2)
    four_stars = round(crystal_count/300*0.03,2)
    st.write(f"Four Stars: {four_stars}")
    st.write(f"Three Stars: {three_stars}")


st.title("---Project Sekai---")
crystal_count = 300*round(st.number_input("Crystals",step=300)/300)
rates(crystal_count)