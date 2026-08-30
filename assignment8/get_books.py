from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import csv
import json



options = webdriver.ChromeOptions()
driver = webdriver.Chrome(
   service=Service(ChromeDriverManager().install()), options=options
)

try:
    # Task 3.2 Load web page
    url = 'https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart'
    driver.get(url)
    driver.implicitly_wait(5)

    # Task 3.3: Find all li elements for search results
    book_items = driver.find_elements(
        By.CSS_SELECTOR,
        "li.cp-search-result-item"
    )
    #Task 3.4: Create empty results list
    results = []

    #Task 3.5: Main loop to extract Title, Author, and Format-Year
    for item in book_items:
        try:
            title_element = item.find_element(
                By.CSS_SELECTOR, '.title-content'
            )
            title_text = title_element.text.strip()
        except Exception:
            title_text = 'N/A'
    # Authors
        try:

            author_elements = item.find_elements(
                By.CSS_SELECTOR, '.author-link'
            )

            authors = [a.text.strip() for a in author_elements if a.text.strip()]

            author_text = '; '.join(authors) if authors else 'N/A'
        except Exception:
            author_text = 'N/A'


        #Year
        try:
            format_element = item.find_element(By.CSS_SELECTOR, '.cp-format-info span')
           
            format_year_text = format_element.text.strip()
        except Exception:
            format_year_text = 'N/A'

        results.append (
         {
            "Title": title_text,
            "Author": author_text,
            "Format-Year": format_year_text,
        }
        )
    # Task 3.6: Create DataFrame and print
    df = pd.DataFrame(results)
    print(df)

    df.to_csv('get_books.csv', index=False)

    print("Successfully saved data to get_books.csv")

    with open('get_books.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=4, ensure_ascii=False)
    print('Successfully saved data to get_books.json')
finally:
    driver.quit()