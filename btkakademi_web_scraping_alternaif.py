from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

driver = webdriver.Chrome()
driver.get("https://www.btkakademi.gov.tr/portal/catalog")

wait = WebDriverWait(driver, 10)

# "Daha Fazla Göster" butonuna tıklayarak tüm kursları yükleme
while True:
    try:
        # Butonu bekle, bul ve tıkla
        more_button = wait.until(EC.element_to_be_clickable((By.ID, "gbt_catalog-main-right-course-more-btn")))
        more_button.click()
        time.sleep(2)  # İçerik yüklenene kadar bekle
    except (TimeoutException, NoSuchElementException):
        print("Daha Fazla Göster butonu bulunamadı veya tıklanacak buton kalmadı.")
        break
    except ElementClickInterceptedException:
        print("Butona tıklanamadı, sayfa kaydırılıyor ve tekrar deneniyor.")
        driver.execute_script("window.scrollBy(0, 300);")
        time.sleep(1)

# Tüm kurslar yüklendikten sonra kurs kartlarını çek
course_cards = driver.find_elements(By.CSS_SELECTOR, "div.m-auto.w-full.sm\\:max-w-\\[262px\\].bcg-primary.relative.rounded-xl")

data = []

for card in course_cards:
    try:
        title_elem = card.find_element(By.CSS_SELECTOR, "div.font-medium.text-base")
        title = title_elem.get_attribute("title") or title_elem.text

        link_elem = card.find_element(By.TAG_NAME, "a")
        href = link_elem.get_attribute("href")
        if not href.startswith("http"):
            href = "https://www.btkakademi.gov.tr" + href

        level_elem = card.find_element(By.CSS_SELECTOR, "span.ant-tag > span.txt-secondary")
        level = level_elem.text.strip()

        user_count_elem = card.find_element(By.CSS_SELECTOR, "div.flex.flex-row.items-center > span.mr-2")
        user_count = user_count_elem.text.strip()

        data.append({
            "Kurs Adı": title,
            "Seviye": level,
            "Kullanıcı Sayısı": user_count,
            "Bağlantı": href
        })
    except Exception as e:
        print(f"⚠️ Hata: {e}")
        continue

driver.quit()

# Kursları çekme tamamlandıktan sonra
data.reverse()  # listeyi ters çevirir

df = pd.DataFrame(data)
df.drop_duplicates(subset=["Kurs Adı"], inplace=True)
df.to_excel("btkakademi_courses_all.xlsx", index=False)


print("✅ Tüm kurslar başarıyla kaydedildi.")
