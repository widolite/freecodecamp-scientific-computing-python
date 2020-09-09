class Category:
    def __init__(self, name=""):
        self.ledger = []
        self.name = name

    def __str__(self):
        title = "{:*^30}\n".format(self.name)
        items = [
            "{:<23}{:>7.2f}\n".format(item['description'][:23], item['amount'])
            for item in self.ledger
        ]
        total = "Total: {}".format(self.get_balance())

        return "{}{}{}".format(title, "".join(items), total)

    def deposit(self, amount, description=""):

        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=""):

        if self.check_funds(amount):
            self.ledger.append({
                'amount': amount * -1,
                'description': description
            })
            return True
        return False

    def transfer(self, amount, budget):
        if self.withdraw(amount, "Transfer to {}".format(budget.name)):
            budget.deposit(amount, "Transfer from {}".format(self.name))
            return True
        return False

    def get_balance(self):
        return float("{:.2f}".format(
            sum([item['amount'] for item in self.ledger])))

    def check_funds(self, amount):
        """ this method is used by withdraw and transfer """
        if amount > sum([item['amount'] for item in self.ledger]):
            return False
        return True


def create_spend_chart(categories):

    title_bar = 'Percentage spent by category\n'
    withdraw_percents = {}
    withdraw_categories = []
    withdraw_sum = {}
    for categorie in categories:
        temp_sum = []
        for withdraw in categorie.ledger:
            if withdraw['amount'] < 0:
                temp_sum.append(withdraw['amount'])
        withdraw_sum[categorie.name] = sum(temp_sum)
        withdraw_categories.append(categorie.name)
    withdraw_average = sum(withdraw_sum.values())
    withdraw_percents = {
        key: (value / withdraw_average) * 100
        for key, value in withdraw_sum.items()
    }
    #rounded down to the nearest 10.
    for key, value in withdraw_percents.items():
        if value < 10:
            withdraw_percents[key] = 0
            continue
        withdraw_percents[key] = int("{}0".format(str(value)[0]))

    categories_len = len(withdraw_categories)
    categories_max = max([len(categorie) for categorie in withdraw_categories])
    categories_footer = ""
    categories_percents = ""
    for x in range(categories_max):
        for y in range(categories_len):
            try:
                if y == 0:
                    categories_footer += "     "
                categories_footer += "{}  ".format(withdraw_categories[y][x])
            except:
                categories_footer += "{}  ".format(" ")
            if y == categories_len - 1:
                categories_footer += "\n"
        if x == 0:
            horizontal_line = "    {}\n".format(
                "-" * (len(categories_footer) - 5))

    for percent in range(100, -1, -10):
        if percent == 100:
            categories_percents += "{}| ".format(percent)
        elif percent == 0:
            categories_percents += "  {}| ".format(percent)
        else:
            categories_percents += " {}| ".format(percent)
        for category, c_percent in withdraw_percents.items():
          if c_percent >= percent:
            categories_percents += "{}  ".format("o")
          else:
            categories_percents += "{}  ".format(" ")
        categories_percents += "\n"
    spend_chart = "{}{}{}{}".format(title_bar,categories_percents, horizontal_line,
                          "{}  ".format(categories_footer.rstrip()))
    return spend_chart
