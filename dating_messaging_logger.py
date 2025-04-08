# -*- coding: utf-8 -*-
"""
Created on Sat Apr  5 09:48:45 2025

@author: Joseph Desktop
"""

import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime, date, time
import json


# Google Sheets setup
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# For Offline setup
# credentials = ServiceAccountCredentials.from_json_keyfile_name("C:/Users/admin/Downloads/door-knocking-app-0eed563aaa36.json", scope)
# client = gspread.authorize(credentials)

# Load credentials from Streamlit secrets
creds_dict = {
    "type": st.secrets["type"],
    "project_id": st.secrets["project_id"],
    "private_key_id": st.secrets["private_key_id"],
    "private_key": st.secrets["private_key"],
    "client_email": st.secrets["client_email"],
    "client_id": st.secrets["client_id"],
    "auth_uri": st.secrets["auth_uri"],
    "token_uri": st.secrets["token_uri"],
    "auth_provider_x509_cert_url": st.secrets["auth_provider_x509_cert_url"],
    "client_x509_cert_url": st.secrets["client_x509_cert_url"],
    "universe_domain": st.secrets["universe_domain"]
}

# For Streamlit cloud setup
creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
client = gspread.authorize(creds)


# Connect to your sheet
sheet = client.open("Dating Message Tracker").sheet1

# Streamlit UI
st.title("📱 Online Dating Message Logger")

st.subheader('The Opening Message')

#Match date


#Opener Section
opener = st.text_input('Insert your opener here or hers, put hq for code of her opener')

girl_name = st.text_input("Girls Name or Nickname (optional)")


# Her message section
st.subheader("💬 Her Message")
her_msg = st.text_area("Her message text")
her_date = st.date_input("Date she sent it", date.today(), key="her_date")
her_time = st.time_input("Time she sent it", time(12, 0), key="her_time")
# her_date = st.date_input("Date she sent it", date.today())
# her_time = st.time_input("Time she sent it", time(12, 0))
her_timestamp = datetime.combine(her_date, her_time).strftime("%Y-%m-%d %H:%M:%S")

# Your response section
st.subheader("🧠 Your Response")
your_msg = st.text_area("Your response text")
your_date = st.date_input("Date you replied", date.today(), key="your_date")
your_time = st.time_input("Time you replied", time(12, 5), key="your_time")
your_timestamp = datetime.combine(your_date, your_time).strftime("%Y-%m-%d %H:%M:%S")

if st.button("Save to Google Sheet"):
    if her_msg and your_msg:
        sheet.append_row([opener,girl_name, her_timestamp, her_msg, your_timestamp, your_msg])
        st.success("✅ Messages saved!")
    else:
        st.error("Please fill in both message fields.")        
