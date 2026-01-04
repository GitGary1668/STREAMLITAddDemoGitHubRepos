FROM python:3.11-slim

WORKDIR /app

# Install python deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app
COPY app.py .

# Hugging Face Spaces commonly exposes port 7860
EXPOSE 7860

# Run Streamlit on 7860 and bind to all interfaces
CMD ["streamlit", "run", "app.py", "--server.port=7860", "--server.address=0.0.0.0"]
