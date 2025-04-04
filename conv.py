
# project 3: Password strength Meter

# Objective:
# Build a Password Strength Meter in python that evalutes a user's password based on security rules.
# The program will:

# Analyze paswwords based on length, character types and pattern.
# Assign a strength score (weak, Moderate, Strong)
#provide feedback to improve weak passwords.
# use control flow, type casting, strings and functions.

# Requirements.

#1. Password strength criteria

# A strong password should:
# Be at least 8 Chracters long
# Contain Uppercase & Lowercase letters
# include at least one digit (0-9)
# Have one special character (!@#$%^&*)

#2. Scoring system:

# weak (score: 1-2) -> short, missing key elements
# Moderate (score: 3-4) -> Good, but missing some security features
# Strong (score: 5) -> meets all criteria

#3. feedback system

# if the password is weak suggest improvements.
# if the password is strong, display a success message.

import re
import streamlit as st

# page styling
st.set_page_config(page_title="password Strength cheacker by Usama Sharif", page_icon="🌘", layout="centered")
#custom css
st.markdown("""
<style>
    .main {text-align: center;}
    .stTextinput {width: 60% !important; margin: auto; }
    .stButton button { width: 50%; background- color: blue; color: white; font-size: 18px; }
    .stButton button:hover { background-color: red; color: white;}
     </style>
""", unsafe_allow_html=True)

# page title and description
st.title("🔐 Password Strength Generator")
st.write("Enter your password to below check the its security level. 🔍")

# function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    if len(password)>=8:
        score += 1  #increase score by 1
    else:
        feedback.append("❌ Password should be ** at least 8 characters long**.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Password should include ** both uppercase (A-Z) and lowercase (a-z) letters**.")

    if re.search(r"\d", password): 
        score +=1
    else:
        feedback.append("❌ Password should include ** at least one number (0-9) **.")


     # special characters
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("include ** at least one special character (!@#$%^&*)**.")
    # display password strength result
    if score == 4:
        st.success("✅ **Strong password** - your password is secure.")
    elif score == 3:
        st.info("⚠️ **Moderate password** - consider improving security by adding more feature")
    else:
        st.error("❌ **Weak password** - follow the suggestion below to strength it. ")

    # feedback
    if feedback:
        with st.expander("🔍 ** Improve Your password** "):
            for item in feedback:
                st.write(item)
password = st.text_input("Enter your password:", type="password", help="Ensure Your password is strong 🔐")

# Button working
if st.button("Check strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("⚠️  Please enter a password first!") # showing warning if password is empty
        
