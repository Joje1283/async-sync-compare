# Step 1: 기본 이미지 선택
FROM python:3.11.7

# Step 2: 작업 디렉토리 설정
WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Step 4: 애플리케이션 코드 추가
COPY . .

# Step 5: 실행 명령 설정
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]


# build: docker build -t fastapi .
# run: docker run -d --name fastapi -p 8000:8000 fastapi