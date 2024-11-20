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
    

def clean_html(raw_html):
    """
    Removes HTML tags and unescapes HTML entities from the given string.
    
    Args:
        raw_html (str): The raw HTML string to clean.
    
    Returns:
        str: The cleaned text.
    """
    if not raw_html:
        return ""
    
    # Replace common HTML entities with their corresponding characters
    html_entities = {
        '&nbsp;': ' ',
        '&amp;': '&',
        '&lt;': '<',
        '&gt;': '>',
        '&quot;': '"',
        '&#39;': "'",
    }
    
    for entity, char in html_entities.items():
        raw_html = raw_html.replace(entity, char)
    
    # Use HTMLCleaner to remove remaining HTML tags
    cleaner = HTMLCleaner()
    cleaner.feed(raw_html)
    return cleaner.get_clean_text()

