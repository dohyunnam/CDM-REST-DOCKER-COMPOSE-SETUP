FROM python:3.9-slim

WORKDIR /restapi

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose port
EXPOSE 1241

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "1241"]