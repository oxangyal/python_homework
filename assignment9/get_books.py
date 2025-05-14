from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import json

options = webdriver.ChromeOptions()
options.add_argument("--headless")

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

try:
    url = "https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart"
    driver.get(url)

    # Use WebDriverWait to wait for the search result items to be present
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "cp-search-result-item"))
        )
    except Exception as e:
        print(f"An error occurred while waiting for the page to load: {e}")
        exit()


    # Find all <li> elements with the class 'row cp-search-result-item'
    li_elements = driver.find_elements(By.CSS_SELECTOR, "li.row.cp-search-result-item")

    results = []

    for li in li_elements:
        # Extract title
        try:
            title_element = li.find_element(By.CSS_SELECTOR, "h2.cp-title span.title-content")
            title = title_element.text.strip()
        except:
            title = "N/A"

        # Extract author(s)
        try:
            author_elements = li.find_elements(By.CSS_SELECTOR, "span.cp-author-link a")
            authors = [author.text.strip() for author in author_elements]
            author = "; ".join(authors)
        except:
            author = ""

        # Extract format and year
        try:
            format_year_element = li.find_element(By.CSS_SELECTOR, "div.cp-format-info span.display-info-primary")
            format_year_text = format_year_element.text.strip()
        except:
            format_year_text = "N/A"

        results.append({
            "title": title,
            "authors": authors,
            "format_and_year": format_year_text
        })

     # Create a DataFrame from the results list
    df = pd.DataFrame(results)

     # Write the DataFrame to a CSV file
    df.to_csv('get_books.csv', index=False)

    # Write the results list to a JSON file
    with open('get_books.json', 'w') as json_file:
        json.dump(results, json_file, indent=4)

    # Print the DataFrame
    print(df)

# # Print the results
# for result in results:
#     print(f"Title: {result['title']}")
#     print(f"Authors: {', '.join(result['authors'])}")
#     print(f"Format/Year: {result['format_and_year']}")
#     print("---")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser
    driver.quit()
