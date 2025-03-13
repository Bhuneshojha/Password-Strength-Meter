import re
import streamlit as st
import time
import random
import string
import base64

st.set_page_config(page_title="Password Safety Analyzer", layout="wide")

# Function to set background image
st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            padding: 20px;
            color: black;
            border-radius: 10px;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.1);

        }
       div.stButton > button {
            background-color: white;
            color: black;
            font-size: 18px;
            padding: 10px 20px;
            border-radius: 10px;
            transition: 0.3s;
            
        }
        div.stButton > button:hover {
            background-color: #00A36C;
        }  
        
       
    </style>l
""", unsafe_allow_html=True)

def set_background(image_url):
    st.markdown(
        f"""
        <style>
            html, body, .stApp {{
                background: url('{image_url}');
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
                color: white;
                
                
            }}
            
        </style>
        """,
        unsafe_allow_html=True
    )

# Set Background Image (Online Image)
set_background("data:image/jpeg;base64,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")

# Sidebar Navigation
st.sidebar.title("Navigation 🛠️")
page = st.sidebar.radio("Go to", ["Home", "Password Tips", "Password Generator"])

if page == "Home":
    st.title("🔐 Password Safety Analyzer")
    st.subheader("Check the strength of your password and improve security!")
    
    password = st.text_input("Enter your password:", type="password", help="Ensure your password is strong and secure.")
    
    if st.button("Check Password"):
        if password:
            with st.spinner("Analyzing Password..."):
                time.sleep(1)
            
            def check_password(password):
                score = 0
                feedback = []
                
                if len(password) >= 8:
                    score += 1
                else:
                    feedback.append("❌ Password should contain at least 8 characters")
                
                if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
                    score += 1
                else:
                    feedback.append("❌ Use both uppercase and lowercase letters")
                
                if re.search(r"\d", password):
                    score += 1
                else:
                    feedback.append("❌ Add at least one numeric character")
                
                if re.search(r"[!@#$%^&*.?/]", password):
                    score += 1
                else:
                    feedback.append("❌ Include at least one special character")
                
                return score, feedback
            
            score, feedback = check_password(password)
            
            st.subheader("Password Strength 🔎")
            
            if score == 4:
                st.success("✅ Your password is highly strong and secure!")
                st.progress(100)
            elif score == 3:
                st.warning("🚨 Your password is strong, but consider adding more complexity.")
                st.progress(75)
            else:
                st.error("❌ Your password is weak. Follow the tips to improve it.")
                st.progress(40)
            
            if feedback:
                with st.expander("Improve your password 🔑"):
                    for issue in feedback:
                        st.write(issue)
        else:
            st.warning("Please enter a password to check its safety 🦾")

elif page == "Password Tips":
    st.title("🔑 Password Security Tips")
    st.write("Follow these best practices to create a strong password:")
    
    tips = [
        "✅ Use at least 12-16 characters",
        "✅ Mix uppercase and lowercase letters",
        "✅ Include numbers and special characters",
        "✅ Avoid common words and personal info",
        "✅ Use a password manager for storage"
    ]
    
    for tip in tips:
        st.write(tip)

elif page == "Password Generator":
    st.title("🔑 Password Generator")
    st.write("Generate a strong password instantly!")
    
    length = st.slider("Select password length", min_value=8, max_value=32, value=12)
    include_upper = st.checkbox("Include Uppercase Letters", value=True)
    include_digits = st.checkbox("Include Numbers", value=True)
    include_special = st.checkbox("Include Special Characters", value=True)
    
    def generate_password(length, upper, digits, special):
        characters = string.ascii_lowercase
        if upper:
            characters += string.ascii_uppercase
        if digits:
            characters += string.digits
        if special:
            characters += "!@#$%^&*?."  
        return ''.join(random.choice(characters) for _ in range(length))
    
    if st.button("Generate Password"):
        password = generate_password(length, include_upper, include_digits, include_special)
        st.success(f"Your Generated Password: `{password}`")
