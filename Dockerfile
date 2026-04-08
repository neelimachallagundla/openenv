FROM python:3.10

WORKDIR /app

# Copy all project files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port for Gradio (important)
EXPOSE 7860

# Run your app
CMD ["python", "app.py"]
