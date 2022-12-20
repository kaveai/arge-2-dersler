# FastAPI Notlar

### Docker'sız çalıştırma
```
uvicorn main:app --reload
```

### Container Build
```
docker build -t sentiment_api:v1 .
```

### Container Run
```
docker run --publish 8080:8080 sentiment_api:v1
```

# AWS Notlar

```
// Instance'ı güncelleme
sudo yum install

// Instance'a docker yüklemek
sudo yum install docker

// Instance'ta docker'ı çalıştırmak
sudo service docker start
```