import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install(), options=options)
)

try:
    url = 'https://owasp.org/www-project-top-ten/'
    driver.get(url)

    driver.implicitly_wait(5)

    risk_elements = driver.find_elements(
        By.XPATH, "//div[contains(@class, 'container')]//ol//li//a" )
    if not risk_elements:
        risk_elements = driver.find_elements(
            By.XPATH, "//main//a[contains(@href, 'A0)]"
        )
    results = []

    for element in risk_elements:
        title = element.text.strip()
        link = element.get_attribut('href')

        if title and link:
            results.append({"Vulnerability": title, "Link": link})
    
    results = results[:10]

    print(pd.DataFrame(results))
    
    df = pd.DataFrame(results)
    df.to_csv('owasp_top_10.csv', index=False)
    print("Successfully saved data to owasp_top_10.csv")
finally:
    driver.quit()
