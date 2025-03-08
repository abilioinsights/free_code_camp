class Category:
    """
    Represents a budget category with a ledger to track deposits and withdrawals.
    """

    def __init__(self, name):
        """
        Initializes a Category object with a name and an empty ledger.

        Args:
            name (str): The name of the budget category.
        """
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        """
        Adds a deposit to the ledger.

        Args:
            amount (float): The amount to deposit.
            description (str): A description of the deposit. Defaults to an empty string.
        """
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        """
        Adds a withdrawal to the ledger if there are sufficient funds.

        Args:
            amount (float): The amount to withdraw.
            description (str): A description of the withdrawal. Defaults to an empty string.

        Returns:
            bool: True if the withdrawal was successful, False otherwise.
        """
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        """
        Calculates the current balance of the category.

        Returns:
            float: The current balance.
        """
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, category):
        """
        Transfers funds from this category to another category.

        Args:
            amount (float): The amount to transfer.
            category (Category): The destination category.

        Returns:
            bool: True if the transfer was successful, False otherwise.
        """
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        """
        Checks if there are sufficient funds for a withdrawal or transfer.

        Args:
            amount (float): The amount to check.

        Returns:
            bool: True if there are sufficient funds, False otherwise.
        """
        return amount <= self.get_balance()

    def __str__(self):
        """
        Returns a string representation of the category's ledger.

        Returns:
            str: A formatted string showing the ledger and total balance.
        """
        title = f"{self.name:*^30}\n"
        items = ""
        for item in self.ledger:
            description = item["description"][:23].ljust(23)
            amount = f"{item['amount']:.2f}".rjust(7)
            items += f"{description}{amount}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total


def create_spend_chart(categories):
    """
    Creates a bar chart showing the percentage spent in each category.

    Args:
        categories (list): A list of Category objects.

    Returns:
        str: A formatted bar chart as a string.
    """
    # Calculate total withdrawals for each category
    withdrawals = [
        sum(item["amount"] for item in category.ledger if item["amount"] < 0)
        for category in categories
    ]
    total_withdrawals = sum(withdrawals)

    # Calculate percentages spent in each category
    percentages = [
        int((withdrawal / total_withdrawals) * 100) if total_withdrawals != 0 else 0
        for withdrawal in withdrawals
    ]

    # Build the chart
    chart = "Percentage spent by category\n"
    for i in range(100, -10, -10):
        chart += f"{i:3}| "
        for percentage in percentages:
            chart += "o  " if percentage >= i else "   "
        chart += "\n"

    # Add the horizontal line
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # Add category names vertically
    max_name_length = max(len(category.name) for category in categories)
    for i in range(max_name_length):
        chart += "     "
        for category in categories:
            if i < len(category.name):
                chart += category.name[i] + "  "
            else:
                chart += "   "
        if i < max_name_length - 1:
            chart += "\n"

    return chart


# Usage example
food = Category("Food")
food.deposit(1000, "deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")

clothing = Category("Clothing")
food.transfer(50, clothing)

print(food)
print(clothing)

categories = [food, clothing]
print(create_spend_chart(categories))
