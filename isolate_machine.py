import click
import requests
import urllib3


@click.command()
@click.option('--access_token_fp', help='Path to Access token file to authenticate to the Microsoft Graph API', required=True)
@click.option('--machine_id_to_isolate', help='ID of the machine to isolate', required=True)
def isolate_machine(access_token_fp, machine_id_to_isolate):
    urllib3.disable_warnings()

    # The endpoint URL for isolating a machine
    url = f"https://api.security.microsoft.com/api/machines/{machine_id_to_isolate}/isolate"

    with open(access_token_fp, 'r') as f:
        access_token = f.read().strip()

    # The headers for the request
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    # The body of the request
    body = {
        "Comment": "Isolating machine for security investigation",
        "IsolationType": "Full"
    }

    # Make the POST request
    response = requests.post(url, headers=headers, json=body, verify=False)

    # Check the response
    if response.status_code == 200:
        print("Machine isolated successfully")
    else:
        print(f"Failed to isolate machine: {response.status_code} - {response.text}")


if __name__ == '__main__':
    isolate_machine()