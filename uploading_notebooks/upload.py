import os
import boto3
from dotenv import load_dotenv


load_dotenv()
SPACES_KEY = os.getenv("SPACES_KEY")
SPACES_SECRET = os.getenv("SPACES_SECRET")


session = boto3.session.Session()
client = session.client('s3',
                        region_name='nyc3',
                        endpoint_url='https://nyc3.digitaloceanspaces.com',
                        aws_access_key_id=SPACES_KEY,
                        aws_secret_access_key=SPACES_SECRET)


# files_list = []
for city in ["rj","sp","df","cwb"]:
    path = f"/home/felipe/coleta2/{city}"
    for number,filename in enumerate(os.listdir(path)):
        # files_list.append(filename)
        client.upload_file(f"/home/felipe/coleta2/{city}/{filename}",'brbus-dataset',f'bronze/{city}/{filename}')
        print(number)

    