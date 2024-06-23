# Creating a virtual environment
python -m venv .venv

# Activating the virtual environment
source .venv/bin/activate

# Installing the required packages
pip install -r requirements.txt

# Installing tesseract and tesseract-lang
brew install tesseract
brew install tesseract-lang

# Creating a config file
cp config.example.py config.py
open -a TextEdit config.py
