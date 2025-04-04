# 🔐 Project 02: Password Strength Meter

## *📌 Objective*  
#Build a *Password Strength Meter* in Python that evaluates a user's password based on security rules. The program will:  
#- Analyze passwords based on *length, character types, and patterns*.  
#- Assign a *strength score* (Weak, Moderate, Strong).  
#- Provide *feedback* to improve weak passwords.  
#- Use *control flow, type casting, strings, and functions*.  

## *🔹 Requirements*  

### *1. Password Strength Criteria*
#A strong password should:  
#✅ Be at least *8 characters long*  
#✅ Contain *uppercase & lowercase letters*  
#✅ Include at least *one digit* (0-9)  
#✅ Have *one special character* (!@#$%^&*)  

### *2. Scoring System*
#- *Weak (Score: 1-2)* → Short, missing key elements  
#- *Moderate (Score: 3-4)* → Good but missing some security features  
#- *Strong (Score: 5)* → Meets all criteria  

### *3. Feedback System*
#- If the password is *weak*, suggest improvements.  
#- If the password is *strong*, display a success message.  


## *🔹 Starter Code (Python)*  
import re
import streamlit as st
#page styling
st.set_page_config(page_title=" Project 02: Password Strength Meter")
st.title("🔐 Password Strength Meter")
st.write("Enter your password check your security level:🔑")
#custom css
st.markdown("""
<style>
   .main {text-align: center;}
   .stTextinput {width: 60% !important; margin: auto; }
   .stButton button { width: 50%; background-color: blue; color: white; font-size: 18px; }
   .stButton button: hover { background-color: red; color: white; }
   </style>
""", unsafe_allow_ html=True
    


#function
def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")
    

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")
    
    
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add *at least one number (0-9)*.")
    
    # Special Character 
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include *at least one special character (!@#$%^&).")
    
    # Strength password
    if score == 4:
        st.success("✅ *Strong Password!* your Password is Secure.")
    elif score == 3:
        st.info("⚠ Moderate Password - Consider adding more security features.")
    else:
        st.error("❌ Weak Password - follow the suggestions above.")

     # Get feedback
     if feedback:
         with st.expander("improve your password:"):
             for item in feedback:
                 st.write(item)
 password = st.text_input("Enter your password",type= "password",help="check your password strong 🔐")

# Button working
if st.button("Check strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("⚠please enter a Password ")
