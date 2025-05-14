from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd


options = webdriver.ChromeOptions()
options.add_argument("--headless")

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

try:
    # Navigate to the page with top 10 vulnerabilities
    driver.get("https://owasp.org/www-project-top-ten/")

    # Wait for the section with id="sec-main" to be present
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.ID, "sec-main"))
        )
    except Exception as e:
        print(f"An error occurred while waiting for the page to load: {e}")
        exit()

    vulnerabilities = []

    for i in range(1, 11):
        try:
            # Construct XPath for each vulnerability
            xpath = f'//*[@id="sec-main"]/ul[2]/li[{i}]/a'

            # Find the element
            element = driver.find_element(By.XPATH, xpath)

            # Get the title (from the strong tag inside the link)
            title = element.find_element(By.TAG_NAME, "strong").text

            # Get the href link
            href = element.get_attribute("href")

            # Create dictionary for this vulnerability
            vuln_dict = {
                "title": title,
                "link": href
            }

            # Add to vulnerabilities list
            vulnerabilities.append(vuln_dict)

        except Exception as e:
            print(f"Error extracting vulnerability {i}: {e}")
            continue

    # Print the extracted data
    print("Extracted Vulnerabilities:")
    for vuln in vulnerabilities:
        print(vuln)

    # Export to CSV file
    df = pd.DataFrame(vulnerabilities)
    df.to_csv('owasp_top_10.csv', index=False, encoding='utf-8')
    print(f"Data successfully written to owasp_top_10.csv")

finally:
    driver.quit()
