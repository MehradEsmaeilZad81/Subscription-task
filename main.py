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


class Invoice:
    def __init__(self, user_id, subscription_name, amount, start_date, end_date):
        self.user_id = user_id
        self.subscription_name = subscription_name
        self.amount = amount
        self.start_date = start_date
        self.end_date = end_date
