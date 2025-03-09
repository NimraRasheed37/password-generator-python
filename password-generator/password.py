import streamlit as sl
import random
import string
import re

# Function to generate a random password
def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters

    if use_digits:
        characters += string.digits

    if use_special:
        characters += string.punctuation

    return ''.join(random.choice(characters) for _ in range(length))

# Function to check password strength
def check_password_strength(password):
    length = len(password)
    
    has_six_alphabets = len(re.findall(r'[a-zA-Z]', password)) >= 6
    has_number = bool(re.search(r'\d', password))
    has_special = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    if not has_number and not has_special:
        return "Weak"
    elif has_six_alphabets and has_number and not has_special:
        return "Medium"
    elif has_six_alphabets and has_number and has_special:
        return "Strong"
    elif length < 6:
        return "Weak"
    elif length < 10:
        return "Medium"
    else:
        return "Strong"

# Streamlit UI

# 1. Title and description:
sl.title("Password Generator and Strength Checker")
sl.write("Generate strong passwords in clicks & check their strength instantly! 🔒🚀")

# 2. Password Generator
sl.header("🔑 Password Generator")
sl.write("Hackers Hate Strong Passwords – Let’s Build One! 🕵️‍♂️🚫")
sl.write("Select the options below and click on 'Generate Password' to get your strong password!")

length = sl.slider("Select length of the password", min_value=6, max_value=12, value=8, step=1)
use_digits = sl.checkbox("Include Digits (0-9)")
use_special = sl.checkbox("Include Special Characters")

if sl.button("Generate Password"):
    password = generate_password(length, use_digits, use_special)
    sl.success(f"Generated Password: {password}")



# 3. Password Strength Checker
sl.header("🔍 Password Strength Checker")
sl.write("Check how strong your password is! 💪")

# input box for users to add their passwords
password_input = sl.text_input("Enter your password", type="password")

if sl.button("Check Password Strength"):
    if password_input:
        strength = check_password_strength(password_input)
        
        # Define background color based on strength level
        color = {
            "Weak": "#ff4d4d",      # Red
            "Medium": "#ffa500",    # Orange
            "Strong": "#4caf50"     # Green
        }.get(strength, "#ffffff") # Default White
        
        # Styled message with colored background
        sl.markdown(
            f"""
            <div style="
                padding: 10px;
                background-color: {color};
                border-radius: 5px;
                color: white;
                font-weight: bold;
                text-align: center;
            ">
                Password is {strength}
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        sl.warning("Please enter a password to check its strength.")


# Ending message
sl.markdown(
    """
    <hr>
    <p style="text-align:center;">
        Created by <a href="https://nimrarasheed-na-sable.vercel.app/" target="_blank" style="color:#4caf50; font-weight:bold; text-decoration:none;">
        Nimra Rasheed</a> © 2025
    </p>
    """, 
    unsafe_allow_html=True
)
