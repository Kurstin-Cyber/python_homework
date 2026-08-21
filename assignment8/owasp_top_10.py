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
    driver.implicitly_wait(6)

    
    risk_elements = driver.find_elements(
        By.XPATH, "//main//a[contains(@href, 'A0') or contains(@href, '2021')]"
    )

   
    if not risk_elements:
        risk_elements = driver.find_elements(By.XPATH, "//main//a")

    results = []
    seen_titles = set()

    for element in risk_elements:
        title = element.text.strip()
        link = element.get_attribute("href")

        
        if title and link and title not in seen_titles and len(results) < 10:
           
            if any(char.isdigit() for char in title) or "A0" in link:
                seen_titles.add(title)
                results.append({"Vulnerability": title, "Link": link})

   
    results = results[:10]

    df = pd.DataFrame(results)
    print(df)

    df.to_csv("owasp_top_10.csv", index=False)
    print("Successfully saved data to owasp_top_10.csv")

finally:
    driver.quit()