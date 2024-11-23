FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    gfortran \
    libatlas-base-dev \
    libblas-dev \
    liblapack-dev \
    python3-distutils \
    && rm -rf /var/lib/apt/lists/*

COPY . /app

RUN pip install --upgrade pip
RUN pip install numpy
RUN pip install pandas
RUN pip install statsmodels
RUN pip install matplotlib
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

ENV FLASK_APP=app.py

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]
