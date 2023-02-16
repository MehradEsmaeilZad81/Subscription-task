# Subscription-task

This Python code is an implementation of a simple user subscription management system. It contains three classes: User, Subscription, and Invoice, which work together to manage user subscriptions, generate invoices and keep track of statistics for each user.

The User class contains information about the user, including their user ID, username, available credit, and a list of subscriptions they have. It has methods to add and remove subscriptions, generate invoices, and get statistics about the user's subscription history.

The Subscription class contains information about a particular subscription, including its name, price, activation status, and a list of invoices. It has methods to activate and deactivate the subscription, and to add an invoice to the list of invoices.

The Invoice class contains information about a specific invoice, including the user ID, subscription name, amount, and start and end dates.

The Python script provides a simple example of how these classes can manage user subscriptions and generate invoices. It creates a User object and a Subscription object, adds the subscription to the User object, activates it, generates two invoices for the User object, and gets the invoices and statistics for the User object.
