import json
import random
import string
from pathlib import Path


class Bank:
    database = "data.json"
    data = []

    if Path(database).exists():
        with open(database, "r") as f:
            data = json.load(f)

    @classmethod
    def _update(cls):
        with open(cls.database, "w") as f:
            json.dump(cls.data, f, indent=4)

    @staticmethod
    def _generate_account():
        chars = random.choices(string.ascii_letters + string.digits, k=6)
        return "".join(chars)

    @staticmethod
    def _get_user(acc, pin):
        for user in Bank.data:
            if user["AccountNo"] == acc and user["Pin"] == pin:
                return user
        return None

    # ---------------- METHODS ---------------- #

    def create_account(self, name, age, email, pin):
        if age < 18:
            return False, "Age must be 18 or above"

        if len(str(pin)) != 4:
            return False, "PIN must be 4 digits"

        user = {
            "name": name,
            "Age": age,
            "Email": email,
            "Pin": pin,
            "AccountNo": Bank._generate_account(),
            "Balance": 0
        }

        Bank.data.append(user)
        Bank._update()
        return True, user

    def deposit(self, acc, pin, amount):
        user = Bank._get_user(acc, pin)
        if not user:
            return False, "Invalid credentials"

        user["Balance"] += amount
        Bank._update()
        return True, user["Balance"]

    def withdraw(self, acc, pin, amount):
        user = Bank._get_user(acc, pin)
        if not user:
            return False, "Invalid credentials"

        if amount > user["Balance"]:
            return False, "Insufficient balance"

        user["Balance"] -= amount
        Bank._update()
        return True, user["Balance"]

    def show_details(self, acc, pin):
        return Bank._get_user(acc, pin)

    def update_details(self, acc, pin, name="", email="", new_pin=None):
        user = Bank._get_user(acc, pin)
        if not user:
            return False

        if name:
            user["name"] = name
        if email:
            user["Email"] = email
        if new_pin:
            user["Pin"] = new_pin

        Bank._update()
        return True

    def delete_account(self, acc, pin):
        user = Bank._get_user(acc, pin)
        if not user:
            return False

        Bank.dat
