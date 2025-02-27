# Data Pipeline Orchestration 🚀🔧📊
Project done as a part of the MS Data Science Program Semester 1 | Infrastructure for Big Data | SETU Carlow Ireland
This repository contains a **Streamlit** application for orchestrating a machine learning data pipeline using **Docker** containers. The app enables users to: 🎯🔍💡

- **Ingest data** into a database.
- **Launch a Jupyter environment** for data cleaning.
- **Trigger model training** once the data is cleaned.

## Features 🚀📌⚙️

1. **Data Ingestion**: Downloads data and stores it in a database.
2. **Jupyter Notebook**: Provides an interactive environment for data cleaning.
3. **Model Training**: Trains the model using cleaned data and saves the trained model.

## Technologies Used 🛠️📦📡

- **Streamlit**: For the user interface.
- **Docker & Docker Compose**: For containerized workflow execution.
- **Jupyter Notebook**: For data cleaning and preprocessing.
- **Python**: For data processing and model training.

## Getting Started 🚀🔧⚡

### Prerequisites ✅💻📌

Ensure you have the following installed on your system:

- **Docker**: [Install Docker](https://docs.docker.com/get-docker/)
- **Docker Compose**: [Install Docker Compose](https://docs.docker.com/compose/install/)
- **Python 3.x**: [Install Python](https://www.python.org/downloads/)
- **Streamlit**: Install using `pip install streamlit`

### Installation 📂⚙️📥

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/your-repository.git
   cd your-repository
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Start the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## Usage 📊🎯🚀

### Step 1: Ingest Data into Database 🗄️📥🔄

- Click the **Run Ingest Step** button to fetch and store data in the database.
- This process runs the following command:
  ```bash
  docker-compose up --build ingest
  ```

### Step 2: Launch Jupyter Notebook for Data Cleaning 📚📝🔍

- Click the **Start Jupyter Service** button.
- Jupyter Notebook will be accessible at `http://localhost:8888`.
- Use Jupyter to clean the data and save it to `shared_data/cleaned_data.csv`.
- Ensure the shared volume is properly set up so the cleaned data is accessible.

### Step 3: Train the Model 📊🧠🎯

- Click the **Run Trainer** button to start training.
- This process runs the following command:
  ```bash
  docker-compose up --build trainer
  ```
- After completion, the trained model will be saved in the container.

## Project Structure 📂🛠️📝

```
|-- app.py                  # Streamlit application
|-- docker-compose.yml      # Docker Compose configuration
|-- shared_data/            # Shared directory for processed data
|-- requirements.txt        # Python dependencies
|-- README.md               # Project documentation
```

## Notes 📝⚠️💡

- Ensure the `shared_data` directory exists before running the workflow.
- If using a bind mount, check that the paths in `docker-compose.yml` are correctly set.
- Monitor logs for errors using:
  ```bash
  docker-compose logs
  ```

## License 📜🔓✅

This project is licensed under the MIT License.

---

### Contributions 💡🤝🚀

Pull requests are welcome! If you find any issues, feel free to open an issue in this repository. 🚀💻📌

