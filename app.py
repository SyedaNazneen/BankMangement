import streamlit as st
from bank import Bank

bank = Bank()

st.set_page_config(page_title="Bank App", page_icon="🏦")
st.title("🏦 Bank Management System")

menu = st.sidebar.selectbox(
    "Select Operation",
    (
        "Create Account",
        "Deposit Money",
        "Withdraw Money",
        "Show Details",
        "Update Details",
        "Delete Account",
    ),
)

# ---------------- CREATE ---------------- #
if menu == "Create Account":
    st.subheader("Create New Account")

    name = st.text_input("Name")
    age = st.number_input("Age", min_value=18)
    email = st.text_input("Email")
    pin = st.text_input("4 Digit PIN", type="password")

    if st.button("Create Account"):
        if pin.isdigit():
            success, result = bank.create_account(name, age, email, int(pin))
            if success:
                st.success("Account Created Successfully 🎉")
                st.json(result)
            else:
                st.error(result)
        else:
            st.error("PIN must be numeric")

# ---------------- DEPOSIT ---------------- #
elif menu == "Deposit Money":
    st.subheader("Deposit Money")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amt = st.number_input("Amount", min_value=1)

    if st.button("Deposit"):
        if pin.isdigit():
            ok, msg = bank.deposit(acc, int(pin), amt)
            if ok:
                st.success(f"Updated Balance: ₹{msg}")
            else:
                st.error(msg)
        else:
            st.error("Invalid PIN")

# ---------------- WITHDRAW ---------------- #
elif menu == "Withdraw Money":
    st.subheader("Withdraw Money")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amt = st.number_input("Amount", min_value=1)

    if st.button("Withdraw"):
        if pin.isdigit():
            ok, msg = bank.withdraw(acc, int(pin), amt)
            if ok:
                st.success(f"Remaining Balance: ₹{msg}")
            else:
                st.error(msg)
        else:
            st.error("Invalid PIN")

# ---------------- SHOW ---------------- #
elif menu == "Show Details":
    st.subheader("Account Details")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("Show Details"):
        if pin.isdigit():
            user = bank.show_details(acc, int(pin))
            if user:
                st.json(user)
            else:
                st.error("User not found")
        else:
            st.error("Invalid PIN")

# ---------------- UPDATE ---------------- #
elif menu == "Update Details":
    st.subheader("Update Account")

    acc = st.text_input("Account Number")
    pin = st.text_input("Old PIN", type="password")
    name = st.text_input("New Name (optional)")
    email = st.text_input("New Email (optional)")
    new_pin = st.text_input("New PIN (optional)", type="password")

    if st.button("Update"):
        if pin.isdigit():
            success = bank.update_details(
                acc,
                int(pin),
                name,
                email,
                int(new_pin) if new_pin.isdigit() else None,
            )
            if success:
                st.success("Details Updated Successfully ✅")
            else:
                st.error("User not found")
        else:
            st.error("Invalid PIN")

# ---------------- DELETE ---------------- #
elif menu == "Delete Account":
    st.subheader("Delete Account ⚠️")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("Delete Account"):
        if pin.isdigit():
            if bank.delete_account(acc, int(pin)):
                st.success("Account Deleted Successfully")
            else:
                st.error("Invalid credentials")
        else:
            st.error("Invalid PIN")
