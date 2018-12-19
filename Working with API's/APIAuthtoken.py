# Example of authing to the microsoft graph API in a function that can be reused often

import adal
import requests

# Parameters can be passed into the function from the calling module/script - I prefer to bring this in from a database when using multiple sources
param_tenant_id = 'x'
param_application_id = 'y'
param_application_secret = 'z'

def authtoken(tenant_id, application_id, application_secret):
    authentication_endpoint = 'https://login.microsoftonline.com/'
    resource  = 'https://management.core.windows.net/'
    context = adal.AuthenticationContext(authentication_endpoint + tenant_id)
    token_response = context.acquire_token_with_client_credentials(resource, application_id, application_secret)
    access_token = token_response.get('accessToken')
    return access_token


access_token = authtoken(param_tenant_id, param_application_id, param_application_secret)

# Get's list of resource groups in subscription
endpoint = 'https://management.azure.com/subscriptions/d470d623-39f9-4dc6-865e-27fb601f140f/resourcegroups?api-version=2018-02-01'
headers = {"Authorization": 'Bearer ' + access_token}
output = requests.get(endpoint,headers=headers).json()