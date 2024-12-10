import streamlit as st
import subprocess
import os

st.title("Data Pipeline Orchestration")

st.markdown("""
This Streamlit app allows you to control the workflow steps:

1. **Ingest**: Download data and store it in the DB.
2. **Jupyter**: Launch a Jupyter environment to clean data. After cleaning, save the cleaned CSV to `/shared/cleaned_data.csv`.
3. **Trainer**: Once cleaned_data.csv is ready, trigger training.
""")

# Paths and commands
compose_file = "docker-compose.yml"  # Adjust if needed
shared_data_path = "shared_data"     # The volume mount point on host if you bind it, or just a named volume
cleaned_data_file = os.path.join(shared_data_path, "cleaned_data.csv")

# Ensure shared_data directory exists if you're using a bind mount
if not os.path.exists(shared_data_path):
    os.makedirs(shared_data_path, exist_ok=True)

st.subheader("Step 1: Ingest Data into Database")
if st.button("Run Ingest Step"):
    st.write("Running `docker-compose up --build ingest`...")
    try:
        # Run the ingest step. The `--exit-code-from ingest` ensures it stops after ingestion completes.
        subprocess.run(["docker-compose", "-f", compose_file, "up", "--build", "--exit-code-from", "ingest", "ingest"], check=True)
        st.success("Ingestion completed successfully.")
    except subprocess.CalledProcessError as e:
        st.error(f"Ingest step failed: {e}")

st.subheader("Step 2: Launch Jupyter Notebook for Data Cleaning")
if st.button("Start Jupyter Service"):
    st.write("Launching Jupyter service in background...")
    # Start jupyter in detached mode
    subprocess.run(["docker-compose", "-f", compose_file, "up", "--build", "-d", "jupyter"], check=False)
    st.write("Jupyter should be accessible at http://localhost:8888. Use the logs to find the token.")
    st.info(f"Go to the Jupyter notebook, clean the data, and save it as {cleaned_data_file}. Once done, come back and run the next step.")




st.subheader("Step 3: Check Cleaned Data and Trigger Trainer")


if st.button("Run Trainer"):

        st.write("Running training step...")
        # Run trainer in foreground to see logs in streamlit:
        try:
            subprocess.run(["docker-compose", "-f", compose_file, "up", "--build", "--exit-code-from", "trainer", "trainer"], check=True)
            st.success("Training completed, model saved!")
        except subprocess.CalledProcessError as e:
            st.error(f"Training step failed: {e}")