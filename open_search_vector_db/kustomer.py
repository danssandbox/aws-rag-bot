import requests
from langchain_core.documents import Document
import boto3


def get_all_shortcuts_as_documents(kustomer_function):
    # Get additional configuration
    aws_region = 'us-east-2'
    ssm = boto3.client('ssm', region_name=aws_region)
    kustomer_api_key_param_path = f"/prod/reporting/dw/kustomer_api_key"
    kustomer_api_key_param_obj = ssm.get_parameter(Name=kustomer_api_key_param_path, WithDecryption=True)
    kustomer_api_key = kustomer_api_key_param_obj['Parameter']['Value']

    base_url = "https://api.kustomerapp.com"
    initial_url = f"{base_url}/{kustomer_function}"
    headers = {
        "Authorization": f"Bearer {kustomer_api_key}",
        "Content-Type": "application/json"
    }

    documents = []
    url = initial_url
    while url:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            for item in data.get('data', []):
                # Check if appDisabled or deleted are False
                if item['attributes'].get('appDisabled', True) or item['attributes'].get('deleted', True):
                    continue  # Skip this item

                name = item['attributes'].get('name', '')
                text = item['attributes']['draft'].get('text', '')
                page_content = f"{name}: {text}"
                metadata = {
                    "source": "Kustomer Shortcut",
                    "title": name,
                    "created_at": item['attributes'].get('updatedAt', '')
                }
                doc = Document(page_content=page_content, metadata=metadata)
                documents.append(doc)

            # Check if there's a next page
            next_link = data.get('links', {}).get('next')
            url = f"{base_url}{next_link}" if next_link else None
        else:
            raise Exception(f"Failed to fetch shortcuts. Status code: {response.status_code}")

    return documents
