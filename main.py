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
