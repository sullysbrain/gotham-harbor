import os
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient


def get_blob_service_client() -> BlobServiceClient:
    """Authenticate to Azure Blob Storage using Azure AD (service principal)."""
    account_name = os.environ["STORAGE_ACCOUNT_NAME"]
    account_url = f"https://{account_name}.blob.core.windows.net"
    credential = DefaultAzureCredential()
    return BlobServiceClient(account_url, credential=credential)


def download_blob(container: str, blob_name: str, dest_path: str) -> str:
    """Download a blob to a local file path."""
    client = get_blob_service_client()
    blob_client = client.get_blob_client(container=container, blob=blob_name)
    with open(dest_path, "wb") as f:
        stream = blob_client.download_blob()
        stream.readinto(f)
    return dest_path


def upload_blob(container: str, blob_name: str, source_path: str) -> None:
    """Upload a local file to a blob."""
    client = get_blob_service_client()
    blob_client = client.get_blob_client(container=container, blob=blob_name)
    with open(source_path, "rb") as f:
        blob_client.upload_blob(f, overwrite=True)


def list_blobs(container: str, prefix: str | None = None) -> list[str]:
    """List blob names in a container, optionally filtered by prefix."""
    client = get_blob_service_client()
    container_client = client.get_container_client(container)
    return [blob.name for blob in container_client.list_blobs(name_starts_with=prefix)]
