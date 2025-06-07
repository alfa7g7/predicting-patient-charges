FROM python:3.10

WORKDIR /app

# Copy requirements and install dependencies first (for better caching)
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy all application files
COPY . /app/

# Train the model first
RUN python train_model.py

# Expose port
EXPOSE 5000

# Run application
CMD ["python", "app.py"] 