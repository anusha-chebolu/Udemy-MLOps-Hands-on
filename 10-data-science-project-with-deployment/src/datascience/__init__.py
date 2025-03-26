import os
import sys
import logging

# Define a standardized logging string format
# This format includes:
# - Timestamp (asctime)
# - Log Level
# - Module name
# - Custom message
logging_str = "[%(asctime)s %(levelname)s: %(module)s - %(message)s]"

# Define the directory for storing log files
# Helps in maintaining organized log management
log_dir = "logs"

# Create the full path for the log file
# Joins the log directory with the specific log filename
log_filepath = os.path.join(log_dir, "logging.log")

# Create the log directory if it doesn't exist
# exist_ok=True prevents raising an error if directory already exists
os.makedirs(log_dir, exist_ok=True)

# Configure the basic logging settings
logging.basicConfig(
    # Set the minimum logging level to INFO
    # This means it will capture INFO, WARNING, ERROR, and CRITICAL levels
    level=logging.INFO,
    
    # Use the predefined logging string format
    # Provides consistent and informative log entries
    format=logging_str,

    # Configure log handlers
    handlers=[
        # File Handler: Writes log messages to a file
        # Useful for persistent logging and later analysis
        logging.FileHandler(log_filepath),
        
        # Stream Handler: Outputs log messages to the console (stdout)
        # Provides real-time visibility during script execution
        logging.StreamHandler(sys.stdout)
    ]
)

# Create a custom logger with a specific name
# Allows for more granular logging control
# Can be used across different modules of the project
logger = logging.getLogger("datasciencelogger")