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
    url = 'https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart'
    driver.get(url)

    driver.implicitly_wait(5)

    book_items = driver.find_elements(
        By.CSS_SELECTOR, 'li.cp-search-result-item'
    )

    results = []

    for item in book_items:
        try:
            title_element = item.find_element(
                By.CSS_SELECTOR, '.title-content'
            )
            title_text = title_element.text.strip()
        except Exception:
            title_text = 'N/A'

        try:

            author_elements = item.find_elements(
                By.CSS_SELECTOR, 'author-link'
            )
            authors = [author.text.strip() for author in author_elements]

            author_text = '; '.join(authors) if authors else 'N/A'
        except Exception:
            author_text = 'N/A'

        try:
            format_div = item.find_element(By.CSS_SELECTOR, 'cp-format-info')
            format_span = format_div.find_element(
                By.CSS_SELECTOR, 'cp-screen-reader-message')
            format_year_text = format_span.text.strip()
        except Exception:
            format_year_text = 'N/A'

        book_dict = {
            "Title": title_text,
            "Author": author_text,
            "Format-Year": format_year_text,
        }
        results.append(book_dict)

    df = pd.DataFrame(results)
    print(df)
    df.to_csv('get_books.csv', index=False)
    print("Successfully saved data to get_books.csv")

    with open('get_books.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=4, ensure_ascii=False)
    print('Successfully saved data to get_books.json')
finally:
    driver.quit()