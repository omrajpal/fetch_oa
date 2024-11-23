# Fetch - ML Engineering Internship Coding Exercise

## Prerequisites

Before running the Flask Prediction App, make sure you have the following installed on your system:

- **Python 3.12+**
- **Docker** (if you plan to run the app in a container)

### Python Dependencies

If you're not using Docker, the following Python packages are required:

- `Flask`
- `pandas`
- `numpy`
- `matplotlib`
- `statsmodels`

You can install these dependencies using `pip` from the `requirements.txt` file provided in the project.

### Data Requirements

Ensure that you have a CSV file named `data_daily.csv` in the project directory. This file should contain at least two columns:

- `# Date`: The date column in `YYYY-MM-DD` format.
- `Receipt_Count`: The numerical data to be predicted (e.g., daily receipt counts).

## Project Setup and Execution

You can run this project in two different ways: 
1. **Using a Python virtual environment**
2. **Using Docker**

### 1. Running the Application in a Python Virtual Environment

#### Step 1: Clone the Repository
First, clone the repository to your local machine:

git clone https://github.com/ankitamin8/Fetch_ML_OA

#### Step 2: Set Up Virtual Environment

##### Create virtual environment
python -m venv myenv

##### Activate the virtual environment
##### On macOS/Linux:
source myenv/bin/activate
##### On Windows:
myenv\Scripts\activate

#### Step 3: Install Dependencies

Install the necessary Python dependencies:
pip install --upgrade pip
pip install -r requirements.txt

#### Step 4: Run the Flask Application

python app.py

### 2. Running the Application Using Docker

#### Step 1: Build the Docker Image
Navigate to the project directory and build the Docker image:

docker build -t my-flask-app .

#### Step 2: Run the Docker Container
Run the Docker container:

docker run -p 5000:5000 my-flask-app

This will expose the Flask app at http://localhost:5000 in your web browser.
