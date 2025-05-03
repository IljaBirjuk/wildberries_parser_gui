import requests
import csv
import time

headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json",
    "Referer": "https://www.wildberries.ru/"
}

query = input("Введите поисковый запрос (например, платье, куртка, кроссовки): ").strip()
total_pages = 15  # можешь увеличить до 10–20

data = []
start_time = time.time()

for page in range(1, total_pages + 1):
    url = (
        f"https://search.wb.ru/exactmatch/ru/common/v4/search?"
        f"appType=1&curr=rub&dest=-1257786&query={query}&page={page}&limit=30&resultset=catalog"
    )

    try:
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            with open("errors.log", "a", encoding="utf-8") as log:
                log.write(f"[Ошибка {response.status_code}] Страница {page}\n")
            print(f"Пропуск страницы {page} из-за ошибки: {response.status_code}")
            continue

        products = response.json().get("data", {}).get("products", [])

        for product in products:
            title = product.get("name", "").replace("\n", " ").replace("\r", " ")
            price = product.get("priceU", 0) // 100
            stars = product.get("reviewRating", 0)
            reviews = product.get("feedbacks", 0)
            link = f"https://www.wildberries.ru/catalog/{product.get('id')}/detail.aspx"
            data.append([title, price, reviews, stars, link])
            print(f"Сохранено: {title}")

    except Exception as e:
        with open("errors.log", "a", encoding="utf-8") as log:
            log.write(f"[Исключение] Страница {page}: {e}\n")
        print(f"Ошибка на странице {page}: {e}")
        continue

# Сохраняем в CSV
with open("wb_api_products.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file, delimiter=";")
    writer.writerow(["Title", "Price", "Reviews", "Stars", "Link"])
    writer.writerows(data)

elapsed = round(time.time() - start_time, 2)
print(f"\nПарсинг завершён: {len(data)} товаров сохранено.")
print(f"Время выполнения: {elapsed} секунд.")
print("Результат в файле wb_api_products.csv")