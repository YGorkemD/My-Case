import xml.etree.ElementTree as ET
from pymongo import MongoClient
from datetime import datetime
from html.parser import HTMLParser
import re


class HTMLCleaner(HTMLParser):
    """Custom HTML parser to extract text without HTML tags."""
    
    def __init__(self):
        super().__init__()
        self.text = ""

    def handle_data(self, data):
        self.text += data

    def get_clean_text(self):
        return self.text.strip()