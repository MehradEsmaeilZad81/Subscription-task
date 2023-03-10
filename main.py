from datetime import datetime, timedelta


class User:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.credit = 0
        self.subscriptions = []

    def add_subscription(self, subscription):
        self.subscriptions.append(subscription)
        print(
            f"Subscription {subscription.name} added for user {self.username}")

    def remove_subscription(self, subscription):
        self.subscriptions.remove(subscription)
        print(
            f"Subscription {subscription.name} removed for user {self.username}")

    def generate_invoices(self):
        for subscription in self.subscriptions:
            if subscription.is_active:
                start_date = datetime.now()
                end_date = start_date + timedelta(minutes=10)
                invoice = Invoice(self.user_id, subscription.name,
                                  subscription.price, start_date, end_date)
                subscription.add_invoice(invoice)
                self.credit -= subscription.price
                print(
                    f"Invoice generated for user {self.username} for subscription {subscription.name} with amount {subscription.price} units")

    def get_invoices(self):
        for subscription in self.subscriptions:
            for invoice in subscription.invoices:
                print(
                    f"Invoice for subscription {subscription.name} from {invoice.start_date} to {invoice.end_date} with amount {invoice.amount} units")

    def get_statistics(self):
        total_invoiced = 0
        for subscription in self.subscriptions:
            for invoice in subscription.invoices:
                total_invoiced += invoice.amount
        total_spent = sum([s.price for s in self.subscriptions])
        print(
            f"User {self.username} has been invoiced {total_invoiced} units and spent {total_spent} units in the system")


class Subscription:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.is_active = False
        self.invoices = []

    def activate(self):
        self.is_active = True
        print(f"Subscription {self.name} activated")

    def deactivate(self):
        self.is_active = False
        print(f"Subscription {self.name} activated")

    def add_invoice(self, invoice):
        self.invoices.append(invoice)


class Invoice:
    def __init__(self, user_id, subscription_name, amount, start_date, end_date):
        self.user_id = user_id
        self.subscription_name = subscription_name
        self.amount = amount
        self.start_date = start_date
        self.end_date = end_date


# Test:

user = User(1, "Mehrad")
user.credit = 1000

subscription = Subscription("VM", 250)
user.add_subscription(subscription)
subscription.activate()

user.generate_invoices()
user.generate_invoices()

user.get_invoices()
user.get_statistics()

# Output:
#       Subscription VM added for user Mehrad
#       Subscription VM activated
#       Invoice generated for user Mehrad for subscription VM with amount 250 units
#       Invoice generated for user Mehrad for subscription VM with amount 250 units
#       Invoice for subscription VM from 2023-02-16 12:15:10.121954 to 2023-02-16 12:25:10.121954 with amount 250 units
#       Invoice for subscription VM from 2023-02-16 12:15:10.121954 to 2023-02-16 12:25:10.121954 with amount 250 units
#       User Mehrad has been invoiced 500 units and spent 250 units in the system
