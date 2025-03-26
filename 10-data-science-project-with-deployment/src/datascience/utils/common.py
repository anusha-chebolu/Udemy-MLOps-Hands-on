import os
import yaml
from src.datascience import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
from box.exceptions import BoxValueError

# Function to read YAML configuration files
# YAML files are commonly used for storing configuration settings
@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Purpose: 
    - Reads configuration or settings from a YAML file
    - Converts the file contents into an easily accessible object
    
    Key Points:
    - Handles potential errors if the file is empty or can't be read
    - Uses safe loading to prevent security risks
    - Logs successful file loading
    - Returns data in a way that allows dot notation access (ConfigBox)
    
    Example Use Case:
    - Reading project configurations
    - Loading database connection settings
    - Storing any structured text-based configuration
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e

# Function to create multiple directories at once
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Purpose:
    - Automatically create multiple directories in one go
    - Prevents errors if directories already exist
    
    Key Points:
    - Can create nested directory structures
    - Optional logging for created directories
    
    Example Use Case:
    - Setting up project folder structure
    - Preparing directories for data storage
    - Creating output folders for different stages of a project
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")

# Function to save data as a JSON file
@ensure_annotations
def save_json(path: Path, data: dict):
    """
    Purpose:
    - Store data in a JSON file format
    - Human-readable and widely used data storage method
    
    Key Points:
    - Writes dictionary data to a file
    - Adds indentation for readability
    - Logs the location of saved file
    
    Example Use Case:
    - Saving configuration settings
    - Storing experiment results
    - Caching intermediate data
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"json file saved at: {path}")

# Function to load data from a JSON file
@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    Purpose:
    - Read data from a JSON file
    - Convert JSON data into an easily accessible object
    
    Key Points:
    - Loads JSON file contents
    - Converts to ConfigBox for easy attribute access
    - Logs successful file loading
    
    Example Use Case:
    - Reading stored configurations
    - Retrieving cached data
    - Loading previous experiment results
    """
    with open(path) as f:
        content = json.load(f)

    logger.info(f"json file loaded succesfully from: {path}")
    return ConfigBox(content)

# Function to save data in a binary format
@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    Purpose:
    - Store complex Python objects in a compressed binary file
    - Preserves exact data structure and types
    
    Key Points:
    - Can save almost any Python object
    - Uses joblib for efficient serialization
    - Logs the location of saved binary file
    
    Example Use Case:
    - Saving machine learning models
    - Storing complex data structures
    - Caching preprocessed data
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")

# Function to load data from a binary file
@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    Purpose:
    - Retrieve complex Python objects from a binary file
    - Restore exact data structure and types
    
    Key Points:
    - Loads previously saved binary files
    - Works with various types of Python objects
    - Logs successful file loading
    
    Example Use Case:
    - Loading saved machine learning models
    - Retrieving cached complex data structures
    - Restoring previous computational states
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data