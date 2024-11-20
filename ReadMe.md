### README.md

---

## **XML to MongoDB Product Data Transfer Script**

This Python project facilitates the extraction of product data from an XML file and its insertion into a MongoDB database. It uses object-oriented programming (OOP) principles and robust data validation, handling various attributes such as product details, images, and descriptions, while cleaning and organizing the data.

---

### **Features**

1. **XML Parsing**  
   - Reads and extracts product data from a structured XML file.

2. **Data Cleaning**  
   - Removes HTML tags and unescapes entities from product descriptions.

3. **MongoDB Integration**  
   - Inserts or updates product data into the specified MongoDB collection.

4. **Error Handling**  
   - Captures errors related to file parsing, database connection, or invalid data.

---

### **Requirements**

1. **Python Version:**  
   Python 3.7 or higher.

2. **Python Libraries:**  
   - `pymongo`  
   - `xml.etree.ElementTree` (built-in)  
   - `datetime` (built-in)  
   - `html.parser` (built-in)  

3. **MongoDB Instance:**  
   - A MongoDB Atlas account or a local MongoDB installation is required.

---

### **Installation**

Install the required library using `pip`:

```bash
pip install pymongo
```

---

### **Project Structure**

- **`script.py`**: The main Python script.  
- **`xml_file.xml`**: The XML file containing product data (to be provided).  
- **`README.md`**: Project documentation (this file).  

---

### **How It Works**

1. **`HTMLCleaner` Class**  
   - A custom HTML parser for cleaning text by removing HTML tags and handling HTML entities.

2. **`Product` Class**  
   - Represents a single product with attributes like name, color, price, and description.  
   - Extracts specific details such as fabric, model measurements, and product measurements using keys from the product's description.

3. **`ProductManager` Class**  
   - Parses the XML file and converts the data into `Product` objects.  
   - Inserts or updates product data in MongoDB.

4. **MongoDB Operations**  
   - Uses the `_id` field (ProductId) to ensure unique identification of products.  
   - Updates existing records or inserts new ones, depending on the data.

---

### **Running the Script**

1. **Configure MongoDB Connection**  
   Set the MongoDB connection details in the script:

   ```python
   connection_string = "mongodb+srv://<username>:<password>@<cluster-name>.mongodb.net/<database>?retryWrites=true&w=majority&appName=Cluster0"
   db_name = "ProductDB"
   collection_name = "Products"
   ```

   Replace `<username>`, `<password>`, `<cluster-name>`, and `<database>` with your MongoDB credentials.

2. **Specify the XML File**  
   Set the path to the XML file in the script:

   ```python
   xml_file = 'xml_file.xml'
   ```

3. **Run the Script**  
   Execute the script with the following command:

   ```bash
   python script.py
   ```

4. **Expected Output**  
   If the script executes successfully, it will output:

   ```plaintext
   [X] products were successfully processed and transferred to MongoDB.
   ```

---

### **XML File Format**

The script processes XML files in the following format:

```xml
<Products>
    <Product ProductId="123" Name="Product Name">
        <Images>
            <Image Path="image1.jpg" />
            <Image Path="image2.jpg" />
        </Images>
        <ProductDetails>
            <ProductDetail Name="Color" Value="Red" />
            <ProductDetail Name="Price" Value="50.00" />
            <ProductDetail Name="DiscountedPrice" Value="40.00" />
            <ProductDetail Name="Quantity" Value="100" />
            <ProductDetail Name="ProductType" Value="Clothing" />
        </ProductDetails>
        <Description>
            <![CDATA[
                <ul>
                    <li><strong>Kumaş Bilgisi:</strong> %100 Pamuk</li>
                    <li><strong>Model Ölçüleri:</strong> 180 cm, 75 kg</li>
                    <li><strong>Ürün Ölçüleri:</strong> L Beden</li>
                </ul>
            ]]>
        </Description>
    </Product>
</Products>
```

---

### **Important Notes**

- **Data Validation**: The script ensures all necessary fields are present and formats numeric values correctly.  
- **Data Uniqueness**: Products are identified by their `ProductId`, ensuring no duplicate records in the database.  
- **Error Logs**: Any errors encountered during execution will be displayed in the console.

---

### **Contact**

If you have any questions or suggestions, feel free to contact:

- **Yavuz Görkem Deniz**  
  Email: [gorkeemdeniz@outlook.com]  
  LinkedIn: [https://www.linkedin.com/in/yavuz-g%C3%B6rkem-deniz-a0a222240/]  

Thank you for using this script!