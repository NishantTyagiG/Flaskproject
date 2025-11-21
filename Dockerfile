FROM python:3.10-slim
WORKDIR /app
COPY requriments.txt /app/
RUN pip install --no-cache-dir -r requriments.txt
COPY . /app/
EXPOSE 8000
CMD ["python","test.py"]
