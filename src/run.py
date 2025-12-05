import subprocess
import os
import sys

# Path to virtual environment
VENV_PYTHON = r"nenv\Scripts\python.exe"

# paths to each step of the pipeline
STEPS = [
    "src/get_data.py",
    "src/clean_data.py",
    "src/analyze.py",
    "src/visualize.py",
    "src/report.py",
]

def run_pipeline():
    print("YOUTUBE TRENDS PIPELINE RUN")

    for step in STEPS:
        print(f"> Running: {step}")

        # Run each step as a separate python process
        result = subprocess.run([VENV_PYTHON, step], capture_output=True, text=True)

        # Forward stdout/stderr to user
        if result.stdout:
            print(result.stdout)
        if result.stderr:
            print(result.stderr)
        
        print(f"Completed: {step}\n")

if __name__ == "__main__":
    run_pipeline()