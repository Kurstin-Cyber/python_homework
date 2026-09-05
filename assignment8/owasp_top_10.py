import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), options=options
)

try:
 
    url = "https://owasp.org/Top10/2025/"
    driver.get(url)
    driver.implicitly_wait(5)
   
   
    vulnerability_elements = driver.find_elements(
        By.XPATH, "//ol//li//a[contains(text(), 'A0')]"
    )

    results = []
    seen_titles = set()

    for element in vulnerability_elements:
        try:
            title = element.text.strip()
            link = element.get_attribute("href")

            if title and link and title not in seen_titles:
                seen_titles.add(title)
                results.append({
                    "Vulnerability": title,
                    "Link": link
                })
        except Exception:
            continue
   
   
    results = results[:10]

    print(f"Extracted {len(results)} items successfully.")
    for item in results:
        print(item)

    df = pd.DataFrame(results)
    if not df.empty:
        df.to_csv("owasp_top_10.csv", index=False)
        print("Successfully saved data to owasp_top_10.csv")
    else:
        print("Warning: DataFrame is empty. No CSV file was written.")

finally:
    driver.quit()