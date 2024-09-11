
drive_link = "< drive folder link >"
def create_folder_download_link(drive_link):
    # Extract the folder ID from the provided Google Drive link
    folder_id = drive_link.split('/folders/')[1].split('?')[0]

    # Construct the download link using the extracted folder ID
    download_link = f"https://drive.google.com/drive/folders/{folder_id}?usp=sharing"

    return download_link
download_link = create_folder_download_link(drive_link)
print(f"Download link: {download_link}")