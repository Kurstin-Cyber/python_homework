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
   
    url = "https://owasp.org/www-project-top-ten/"
    driver.get(url)
    driver.implicitly_wait(5)

    vulnerability_elements = driver.find_elements(
        By.XPATH, "//main//ol//li//a | //main//ul//li//a"
    )

    results = []
    seen_titles = set()

    for element in vulnerability_elements:
        try:
            title = element.text.strip()
            link = element.get_attribute("href")

            
            if title and link and title not in seen_titles:
                if title.startswith("A0") or "A1" in title or "Injection" in title or "Broken" in title or "Control" in title:
                    seen_titles.add(title)
                    results.append({"Vulnerability": title, "Link": link})
        except Exception:
            continue

 
    if len(results) < 10:
        results = []
        seen_titles.clear()
        for element in vulnerability_elements:
            try:
                title = element.text.strip()
                link = element.get_attribute("href")
                
                if title and link and title not in seen_titles and ("A0" in title or "A10" in title or len(title) > 5):
                    seen_titles.add(title)
                    results.append({"Vulnerability": title, "Link": link})
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