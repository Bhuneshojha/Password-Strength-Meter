import re
import streamlit as st

st.set_page_config(page_title="Password Safety Analyzer with Bhunesh Ojha", )

st.markdown("""
 <style>
  .main{text-align:center;}
  .stTextInput{width:60% important!;margin:auto;}
  .stButton button{width:50%; bacground-color:#4CAF50;color:white;font-size:18px;}
  .stButton button:hover{background-color:#45a349;}
  </style>

   """,unsafe_allow_html=True
)
st.title("Password Safety Analyzer 🛡️")
st.write("Enter your password to check its Safety 🕵️‍♂️")

def check_password(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should contain a minimum of 8 characters")

    if re.search(r"[A-Z]",password) and re.search(r"[a-z]",password):
        score +=1
    else:
        feedback.append("❌ Password should contain both uppercase and lowercase letters")
    if re.search(r"/d",password):
        score +=1
    else:
        feedback.append("❌ Ensure your password contains at least one numeric character")
    if re.search(r"[!@#$%^&]",password):
        score +=1
    else:
        feedback.append("❌ Password should contain at least one special character")


    if score == 4:
        st.success("✅ Your password is highly strong and well-secured")
    elif score == 3:
        st.info("🚨 Your password is strong, but consider adding more complexity")
    else:
        st.error("❌ Your password is weak. follow the instructions to improve it")


    if feedback:
        with st.expander("Improve your password 🔑"):
            for issue in feedback:
                st.write(issue)
password = st.text_input("Enter your password:",type="password",help="Ensure password is Strong and Secure 🔐")

if st.button("Check Password"):
    if password:
          check_password(password)
    else:
        st.warning("Please enter a password to check its safety 🦾")










