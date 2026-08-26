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

    
    vulnerbility_elements = driver.find_elements(
        By.XPATH, "//main//ol//li//a"
    )

   
    if not vulnerbility_elements:
        vulnerbility_elements = driver.find_elements(By.XPATH, "//main//a")

    results = []

    seen_titles = set()

    for element in vulnerbility_elements:
        title = element.text.strip()
        link = element.get_attribute("href")

        
        if title and link:
            results.append({
                "Vulnerability": title,
                "Link": link
            })
   
    results = results[:10]

    df = pd.DataFrame(results)
    print(df)

    df.to_csv("owasp_top_10.csv", index=False)
    print("Successfully saved data to owasp_top_10.csv")

finally:
    driver.quit()