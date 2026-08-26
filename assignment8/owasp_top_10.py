import pandas as pd
import os
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
        By.XPATH,
       "//li[contains(@class, 'md-nav__item')]//a[contains(@href, '2025')]"
    
    )
   

    results = []

    seen_titles = set()

    for element in vulnerability_elements:
        title = element.text.strip()
        link = element.get_attribute("href")

        
        if title and link and title not in seen_titles:
            seen_titles.add(title)

            results.append({
                "Vulnerability": title,
                "Link": link
            })
   
    results = results[:10]

    print(results)
    df = pd.DataFrame(results)


    df.to_csv("owasp_top_10.csv", index=False)

    print("Successfully saved data to owasp_top_10.csv")


finally:
    driver.quit()