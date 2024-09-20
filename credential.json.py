from google.oauth2 import service_account
from googleapiclient.discovery import build

def main():
    # Load the service account key JSON file
    creds = service_account.Credentials.from_service_account_file('triple-brook-421904-057b98429f82.json', scopes=['https://www.googleapis.com/auth/cloud-platform'])

    # Use credentials to create a service client
    service = build('compute', 'v1', credentials=creds)

    # Example: List Compute Engine instances (modify according to your needs)
    result = service.instances().list(project='triple-brook-421904', zone='asia-northeast1-b').execute()
    print(result)

if __name__ == '__main__':
    main()
