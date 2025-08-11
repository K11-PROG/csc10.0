import json
import streamlit as st
from datetime import date

# Load data
with open("data/calendar_2025_en.json") as f:
    calendar_data = json.load(f)

with open("data/meditations_2025_en.json") as f:
    meditations_data = json.load(f)

# App title
st.set_page_config(page_title="Catholic Saints Calendar", layout="centered")
st.title("Catholic Saints Calendar - August 2025 (English)")

# Date picker
selected_date = st.date_input("Select a date", date(2025, 8, 1),
                              min_value=date(2025, 8, 1),
                              max_value=date(2025, 8, 31))

date_str = selected_date.strftime("%Y-%m-%d")

if date_str in calendar_data:
    st.subheader(f"Saint/Feast: {calendar_data[date_str]['saint']}")
    st.write(f"Liturgical color: {calendar_data[date_str]['color']}")
    st.write(f"Feast type: {calendar_data[date_str]['type']}")
else:
    st.warning("No data for this date.")

if date_str in meditations_data:
    st.markdown("### Daily Meditation")
    st.write(meditations_data[date_str])
else:
    st.info("No meditation available for this date.")

# Notes feature
st.markdown("### Your Notes")
notes_file = f"notes/{date_str}.txt"

existing_notes = ""
try:
    with open(notes_file, "r") as nf:
        existing_notes = nf.read()
except FileNotFoundError:
    pass

user_notes = st.text_area("Write your notes here:", existing_notes, height=150)

if st.button("Save Notes"):
    with open(notes_file, "w") as nf:
        nf.write(user_notes)
    st.success("Notes saved successfully!")
