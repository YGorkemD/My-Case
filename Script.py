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


class Product:
    """Class representing product information."""

    def __init__(self, product_id, name, details, images, description):
        self.product_id = product_id
        self.name = name.strip().capitalize()
        self.color = [details.get('Color', '').capitalize()]
        self.discounted_price = float(details.get('DiscountedPrice', '0').replace(',', '.'))
        self.is_discounted = self.discounted_price > 0
        self.price = float(details.get('Price', '0').replace(',', '.'))
        self.price_unit = 'USD'
        self.product_type = details.get('ProductType', '')
        self.quantity = int(details.get('Quantity', '0'))
        self.series = details.get('Series', '')
        self.season = details.get('Season', '')  
        self.status = 'Active' if self.quantity > 0 else 'Inactive'
        self.fabric = self.extract_detail(description, 'Kumaş Bilgisi:')
        self.model_measurements = self.extract_detail(description, 'Model Ölçüleri:')
        self.product_measurements = (
            self.extract_detail(description, 'Ürün Ölçüleri:') or 
            self.extract_detail(description, 'Ürün Ölçüleri1:')
        )
        self.product_info = self.extract_detail(description, 'Ürün Bilgisi:')
        self.model_product_info = self.extract_model_product_info(description)
        self.images = images
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    @staticmethod
    def extract_detail(description, key):
        """
        Extracts and cleans information from the description using a given key.
        
        Args:
            description (str): The HTML description string.
            key (str): The key to search for in the description.
        
        Returns:
            str: The cleaned extracted detail or an empty string if not found.
        """
        if key in description:
            try:
                # Split the description to extract the value after the key
                raw_detail = description.split(f'{key}</strong>')[-1].split('</li>')[0].strip()
                return clean_html(raw_detail)
            except IndexError:
                return ""
        return ""
    
    @staticmethod
    def extract_model_product_info(description):
        """
        Extracts and cleans the model product information from the description.
        
        Args:
            description (str): The HTML description string.
        
        Returns:
            str: The cleaned model product information or an empty string if not found.
        """
        key = 'Modelin üzerindeki ürün'
        if key in description:
            try:
                raw_info = description.split(f'{key}')[1].split('</li>')[0].strip()
                return clean_html(raw_info)
            except IndexError:
                return ""
        return ""

    def to_dict(self):
        """Converts the object into a dictionary for MongoDB."""
        return {
            '_id': self.product_id,
            'stock_code': self.product_id,
            'color': self.color,
            'discounted_price': self.discounted_price,
            'is_discounted': self.is_discounted,
            'price': self.price,
            'price_unit': self.price_unit,
            'product_type': self.product_type,
            'quantity': self.quantity,
            'series': self.series,
            'season': self.season,  
            'status': self.status,
            'fabric': self.fabric,
            'model_measurements': self.model_measurements,
            'product_measurements': self.product_measurements,
            'product_info': self.product_info,
            'model_product_info': self.model_product_info,
            'name': self.name,
            'images': self.images,
            'createdAt': self.created_at,
            'updatedAt': self.updated_at,
        }

