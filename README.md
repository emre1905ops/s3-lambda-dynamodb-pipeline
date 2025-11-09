# s3-lambda-dynamodb-pipeline
Serverless AWS pipeline: S3 → Lambda → DynamoDB
# S3 → Lambda → DynamoDB Pipeline

## Proje Açıklaması
Bu proje, AWS Serverless mimari kullanılarak geliştirilmiş bir veri pipeline örneğidir.
- **AWS S3**: Dosya yükleme alanı
- **AWS Lambda**: Dosyaları tetikleme ve işleme
- **DynamoDB**: Verilerin kaydedildiği NoSQL tablo
- **CloudWatch Logs**: İşlem ve hata logları

## Kullanılan Teknolojiler
- Python 3.12
- Boto3 (AWS SDK for Python)
- AWS Serverless (Lambda, S3, DynamoDB, CloudWatch)

## Kurulum ve Test
1. AWS S3 bucket ve DynamoDB tablosu oluşturun
2. Lambda fonksiyonunu `lambda_function.py` ile oluşturun
3. S3 trigger ekleyin (All object create events)
4. Örnek CSV veya JSON dosyalarını `sample_files/` klasöründen yükleyin
5. CloudWatch üzerinden Lambda loglarını takip edin

## Örnek Dosyalar
- `sample_files/test.csv`
- `sample_files/test.json`

## Architecture Diagram
![Workflow](architecture_diagram.png)
