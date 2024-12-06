# Setup Environment

0. **Install Prerequisites**:
   - Ensure that Python and Jupyter Notebook are installed on your system. You can refer to the following links for installation guidance:
     - [Install Python](https://realpython.com/installing-python/)
     - [Install Jupyter Notebook](https://jupyter.org/install)

1. **Install Required Packages**:
   - Run the following script to set up your environment by installing the required packages:
     ```bash
     python3 -m pip install -r requirements.txt
     ```
# Practice1

## Repository Contents
Folder path `practice_1`

- **`practice_1.ipynb`**: Jupyter notebook for data preprocessing and model training.
- **`models_practice_1/spam_email_model.pkl`**: The trained model checkpoint.
- **`models_practice_1/spam_email_transform.pkl`**: The preprocessing scaler checkpoint.
- **`serving_practice_1.py`**: Python script to serve the model as an API.
- **`practice_1_client_sample.sh`**: Shell script to demonstrate a sample API call.

## Steps to Train the Model

1. **Open the Jupyter Notebook**:
   - Launch Jupyter Notebook and open `practice_1.ipynb`.

2. **Preprocess Data and Train the Model**:
   - Follow the steps in the notebook to preprocess the data and train the model.
   - Ensure each cell is executed in sequence to complete the training process.
   - The trained model will be saved as `models_practice_1/spam_email_model.pkl`.
   - The preprocessing scaler will be saved as `models_practice_1/spam_email_transform.pkl`.

## Steps to Serve the Model

1. **Set Environment Variables**:
   - Update environment variables `MODEL_PATH` and `SCALER_PATH` to point to the correct model and scaler checkpoints.
     ```bash
     export MODEL_PATH=models_practice_1/spam_email_model.pkl # this is default value
     export TRANSFORM_PATH=models_practice_1/spam_email_transform.pkl # this also is default value
     ```

2. **Run the API Server**:
   - Execute the following command to start the server:
     ```bash
     python3 serving_practice_1.py
     ```

## Steps to Run the Sample Client

1. **Execute the Sample Client Script**:
   - Run the `practice_2_client_sample.sh` script to make a sample API call.
     ```bash
     sh practice_1_client_sample.sh
     ```

2. **Expected Output**:
   - The script should output a JSON response similar to:
     ```json
     {"spam": true}
     ```