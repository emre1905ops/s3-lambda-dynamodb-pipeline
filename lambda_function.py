import boto3
import csv
import json
import io
import uuid

# AWS servisleri için client/resource oluştur
s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')

# DynamoDB tablosu adı
table = dynamodb.Table('UploadedFiles')

def lambda_handler(event, context):
    # S3 eventindeki tüm dosyaları işle
    for record in event.get('Records', []):
        try:
            bucket = record['s3']['bucket']['name']
            key = record['s3']['object']['key']
            print(f"Processing file: {key} from bucket: {bucket}")

            # Dosyayı S3'ten indir
            obj = s3.get_object(Bucket=bucket, Key=key)
            content = obj['Body'].read().decode('utf-8')

            # CSV dosyası işle
            if key.lower().endswith('.csv'):
                f = io.StringIO(content)
                reader = csv.DictReader(f)
                for row in reader:
                    # Her satır için benzersiz ID ekle
                    row['id'] = str(uuid.uuid4())
                    table.put_item(Item=row)
                print(f"CSV dosyası başarıyla işlendi: {key}")

            # JSON dosyası işle
            elif key.lower().endswith('.json'):
                data = json.loads(content)
                if isinstance(data, list):
                    for obj_item in data:
                        obj_item['id'] = str(uuid.uuid4())
                        table.put_item(Item=obj_item)
                elif isinstance(data, dict):
                    data['id'] = str(uuid.uuid4())
                    table.put_item(Item=data)
                print(f"JSON dosyası başarıyla işlendi: {key}")

            else:
                print(f"Desteklenmeyen dosya formatı: {key}")

        except Exception as e:
            print(f"Hata oluştu: {e}")

    return {
        'statusCode': 200,
        'body': json.dumps("Dosya işleme tamamlandı.")
    }
