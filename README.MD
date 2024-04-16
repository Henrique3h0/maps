# Google Maps Scraper 🗺️

This is a project consisting of two Python scripts to extract information from commercial establishments on Google Maps and create HTML files with this data.

## Features 🚀

### Script 1: scraper.py 📜

The `scraper.py` script contains a `GoogleMapsScraper` class that performs the following tasks:

- Initializes a headless Chrome browser using Selenium.
- Performs a search on Google Maps with a term provided by the user.
- Extracts information from search results, such as name, address, website, and contact.
- Creates threads to handle multiple results efficiently.
- Closes the browser after scraping is completed.

### Script 2: maps.py 🔄

The `maps.py` script interacts with the Google Maps scraper and performs the following tasks:

- Prompts the user to enter a location and type of establishment.
- Uses the scraper to search for and extract information from establishments.
- Creates HTML files with the obtained data.
- Opens the HTML files in the browser for visualization.
- Displays messages to the user informing about the search results.

## Prerequisites 🛠️

- Python 3.x installed on the system.
- Required libraries can be installed using the `requirements.txt` file.

## How to Use 📋

1. Clone the repository to your local environment:

```bash
git clone https://github.com/Henrique3h0/maps
```

2. Navigate to the project directory:

```bash
cd maps
```

3. Install the dependencies:

```bash
pip install -r requirements.txt
```

4. Run the `maps.py` script:

```bash
python maps.py
```

5. Follow the instructions presented in the terminal to perform the search.

## Additional Notes ℹ️

- Ensure you have an active internet connection for the scraper to access Google Maps.
- The generated HTML files will be saved in the `captações/{actual_data}` directory within the project directory.

## Perfect for Google Maps Client Acquisition 🎯

This tool is ideal for professionals who perform client acquisition using Google Maps, facilitating the extraction and organization of information from commercial establishments.

## Contributions 🤝

Contributions are welcome! Feel free to open an issue if you encounter any problems or to propose improvements.

## Author ✍️

Developed by [LIMA](https://github.com/Henrique3h0).
