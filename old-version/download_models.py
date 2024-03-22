from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from google import auth
import os

# Credenciais do Google
credentials, _ = auth.default()

# Serviço Google Drive
drive = build('drive', 'v3', credentials=credentials)

# se o link da pasta for https://drive.google.com/drive/folders/1ErR1g2qvmwwxiQFzwQiu_erXmgfjY0Xm?  o ID será 1ErR1g2qvmwwxiQFzwQiu_erXmgfjY0Xm
# ID da pasta
folder_id = '1ErR1g2qvmwwxiQFzwQiu_erXmgfjY0Xm'

# Listar os arquivos na pasta
request = drive.files().list(q=f"'{folder_id}' in parents and trashed=false",
                             fields='nextPageToken, files(id, name)')
response = request.execute()

# Baixar os arquivos
for file in response['files']:
    file_id = file['id']
    file_name = file['name']
    file_path = f'{os.path.join(os.getcwd,file_name)}'

    request = drive.files().get_media(fileId=file_id)

    with open(file_path, 'wb') as f:
        downloader = MediaIoBaseDownload(f, request)
        done = False
        while not done:
            status, done = downloader.next_chunk()

    print(f'Arquivo {file_name} baixado com sucesso!')
