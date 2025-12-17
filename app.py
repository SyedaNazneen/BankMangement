# app.py
import streamlit as st
from bank import Bank

bank = Bank()

st.title("🏦 Simple Bank Management System")

menu = st.sidebar.selectbox(
    "Select Option",
    [
        "Create Account",
        "Deposit Money",
        "Withdraw Money",
        "Show Details",
        "Update Details",
        "Delete Account"
    ]
)

if menu == "Create Account":
    st.subheader("Create Account")

    name = st.text_input("Name")
    age = st.number_input("Age", min_value=18)
    email = st.text_input("Email")
    pin = st.text_input("4 Digit PIN", type="password")

    if st.button("Create"):
        success, result = bank.create_account(name, age, email, int(pin))
        st.success("Account Created 🎉") if success else st.error(result)

elif menu == "Deposit Money":
    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amt = st.number_input("Amount", min_value=1)

    if st.button("Deposit"):
        ok, msg = bank.deposit(acc, int(pin), amt)
        st.success(f"Balance: {msg}") if ok else st.error(msg)
