import tableauserverclient as TSC
import dotenv
import os
from tableau.tableau_tsc import get_tableau_server_and_auth

dotenv.load_dotenv()


def list_webhooks_on_site():
    """
    Lists all webhooks on the Tableau site.
    """

    server, tableau_auth = get_tableau_server_and_auth()

    with server.auth.sign_in(tableau_auth):
        all_webhooks = list(TSC.Pager(server.webhooks))

        return all_webhooks


def get_webhook_by_id(webhook_id):
    """
    Retrieves a specific webhook by its ID."""

    server, tableau_auth = get_tableau_server_and_auth()

    with server.auth.sign_in(tableau_auth):
        webhook = server.webhooks.get_by_id(webhook_id)

        return webhook


def create_webhook(name, url, event_type):
    """
    Creates a new webhook on the Tableau site.
    """

    server, tableau_auth = get_tableau_server_and_auth()

    with server.auth.sign_in(tableau_auth):
        new_webhook = TSC.WebhookItem()
        new_webhook.name = name
        new_webhook.url = url
        new_webhook.event = event_type

        created_webhook = server.webhooks.create(new_webhook)

        return created_webhook


def delete_webhook(webhook_id):
    """
    Deletes a webhook by its ID.
    """

    server, tableau_auth = get_tableau_server_and_auth()

    with server.auth.sign_in(tableau_auth):
        server.webhooks.delete(webhook_id)

        return f"Webhook with ID {webhook_id} has been deleted."
