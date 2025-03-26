import os
from pathlib import Path
import logging

# Project name - used as the main package name
project_name = "datascience"

# List of files and directories to be created in the project
# Organized to represent a typical machine learning or data science project structure
list_of_files = [
    # GitHub Actions workflow directory (for CI/CD)
    ".github/workflows/.gitkeep",  # Placeholder for continuous integration workflows

    # Main source code package
    f"src/{project_name}/__init__.py",  # Marks the directory as a Python package

    # Components subdirectory (for reusable code components)
    f"src/{project_name}/components/__init__.py",  # Package for machine learning components

    # Utilities subdirectory (for helper functions and common utilities)
    f"src/{project_name}/utils/__init__.py",  # Package for utility functions
    f"src/{project_name}/utils/common.py",  # Common utility functions used across the project

    # Configuration management
    f"src/{project_name}/config/__init__.py",  # Package for configuration-related code
    f"src/{project_name}/config/configuration.py",  # Configuration management and settings

    # Pipeline subdirectory (for data processing and ML workflow steps)
    f"src/{project_name}/pipeline/__init__.py",  # Package for ML pipeline components

    # Entity subdirectory (for data models and configuration entities)
    f"src/{project_name}/entity/__init__.py",  # Package for data models
    f"src/{project_name}/entity/config_entity.py",  # Defines configuration and data entities

    # Constants subdirectory (for project-wide constant values)
    f"src/{project_name}/constants/__init__.py",  # Package for constant definitions

    # Configuration files
    "config/config.yaml",  # Main configuration file (YAML format)
    "params.yaml",  # Hyperparameters or model parameters
    "schema.yaml",  # Data schema definition

    # Entry point and deployment
    "main.py",  # Main script to run the entire data science project
    "Dockerfile",  # Docker configuration for containerization
    "README.md",  # Project documentation and instructions

    # Project setup and requirements
    "requirements.txt",  # List of Python package dependencies
    "setup.py",  # Python package installation and setup script

    # Research and experimentation
    "research/research.ipynb",  # Jupyter notebook for initial research and exploration

    # Web interface (if applicable)
    "templates/index.html"  # HTML template for potential web interface
]

# Iterate through the list of files and create directories and empty files
for filepath in list_of_files:
    # Convert to Path object for cross-platform compatibility
    filepath = Path(filepath)
    
    # Split the filepath into directory and filename
    filedir, filename = os.path.split(filepath)

    # Create directory if it doesn't exist
    if filedir!="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Directory created: {filedir} for the file: {filename}")
    
    # Create empty file if it doesn't exist or is empty
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as file:
            pass
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"File already exists: {filepath}")