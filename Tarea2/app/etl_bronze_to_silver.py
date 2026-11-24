def get_s3_client():
    return (boto3.client(
        "s3",
        endpoint_url=os.getenv('MINIO_ENDPOINT'),
        aws_access_key=os.getenv('MINIO_ACCESS_KEY'),
        aws_secret_access=os.getenv('MINIO_SECRET_KEY'),
        region_name="eu-west-1"
        )
)

def extract_from_bronce():
def transform():
def load_parquet():

if __name__ == "__main__":
    s3_client = get_s3_client()
    df_raw = extract_from_bronce(s3_client)
    df_clean = transform(df_raw)
    load_parquet(s3_client,df_clean)
