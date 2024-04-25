import json
import urllib.parse
import urllib.request

import click


@click.command()
@click.option('--client_id', help='Client ID of the application', required=True)
@click.option('--client_secret', help='Client Secret of the application', required=True)
@click.option('--tenant_id', help='Tenant ID of the application', required=True)
def generate_aad_token(client_id, client_secret, tenant_id):

    url = "https://login.microsoftonline.com/%s/oauth2/token" % (tenant_id)
    resource_app_id_uri = 'https://api.securitycenter.windows.com'
    body = {
        'resource' : resource_app_id_uri,
        'client_id' : client_id,
        'client_secret' : client_secret,
        'grant_type' : 'client_credentials'
    }

    data = urllib.parse.urlencode(body).encode("utf-8")
    request = urllib.request.Request(url, data)
    response = urllib.request.urlopen(request)
    json_response = json.loads(response.read())
    aad_token = json_response["access_token"]

    with open('aad_token.txt', 'w') as f:
        f.write(aad_token)

    print("API key generated successfully")



if __name__ == '__main__':
    generate_aad_token()