## 解釋同步和非同步的差異
|      | 同步   | 非同步   |
| ---- | ------ | -------- |
| 定義 | 請求發送後，必須等待伺服器的回應後才能繼續下一個操作 | 請求發送後，不需要等待伺服器的回應即可繼續下一個操作 |
| 阻塞/非阻塞 | 阻塞 | 非阻塞 |
| 返回值 | 即時返回 | 不即時返回 |
| 速度 | 較慢 | 較快 |
| 應用 | 簡單明瞭，適用於數據量較小的操作 | 適用於數據量較大或需要長時間執行的操作 |
| 錯誤處理 | 錯誤處理複雜，容易導致系統崩潰 | 錯誤處理相對簡單，容錯性較高 |

## 如何檢查 SQL 緩慢之問題，你是如何進行檢查並優化？
### 如何檢查 SQL 緩慢之問題
1. 使用 EXPLAIN 指令分析 SQL 語句，確認查詢包括索引的使用情況、行數、排序等。
2. 檢查是否存在索引失效或缺失，例如 WHERE 條件中欄位沒有索引或錯誤的索引。
3. 檢查是否存在子查詢或 JOIN 過多的情況，這會導致系統負載過大或運行時間過長。
4. 檢查是否存在數據結構設計不合理，例如表之間的關聯性設計不當或冗余欄位過多。
5. 檢查數據庫的緩存，是否存在大量的緩存失效或過期的情況。
### 如何進行檢查並優化:
```sql
EXPLAIN SELECT * FROM orders WHERE status = 'pending' AND amount > 100;
```
| id | select_type | table  | partitions | type | possible_keys | key    | key_len | ref   | rows | filtered | Extra       |
|----|-------------|--------|------------|------|---------------|--------|---------|-------|------|----------|-------------|
| 1  | SIMPLE      | orders | NULL       | ref  | status        | status | 66      | const | 500  | 50.00    | Using where |

使用EXPLAIN 檢查，上列使用了 status 索引，查詢了 500 行，其中有 50% 符合 WHERE 條件。如果需要進一步優化，可以考慮在 status 和 amount 上都建立索引，或者使用多表 JOIN 操作，避免在單表上進行大量的查詢操作。同時，也可以考慮增加緩存來減少數據庫的負載。

## 資料庫索引的優缺點?
### 優點：
- 改善資料庫的可搜尋性
- 支持唯一性約束
- 減少資料讀取時間
- 提高資料庫效能
- 加速查詢速度
### 缺點：
- 當索引的層級增加時，查詢的效能會下降
- 索引需要維護，會增加寫入操作的時間
- 索引需要定期維護，以確保它們保持最新
- 適當的索引設計需要較高的技能水平
- 增加資料庫的空間和複雜性

## 什麼是 Deadlock？  (用程式碼表示)。
    
```python
from datetime import datetime
import threading, time

def worker_1(resource_a, resource_b, lock_a, lock_b):
    acquired_lock_a = lock_a.acquire(timeout=5)
    print(f"Worker 1 {'acquired' if acquired_lock_a else 'failed to acquire'} lock_a at {datetime.utcnow()}")
    acquired_lock_b = lock_b.acquire(timeout=5)
    print(f"Worker 1 {'acquired' if acquired_lock_b else 'failed to acquire'} lock_b at {datetime.utcnow()}")

    if acquired_lock_a and acquired_lock_b:
        resource_a += 1
        resource_b += 1
        print(f"Worker 1 updated resource_a to {resource_a}, resource_b to {resource_b}")
        lock_b.release()
        lock_a.release()

def worker_2(resource_a, resource_b, lock_a, lock_b):
    acquired_lock_b = lock_b.acquire(timeout=5)
    print(f"Worker 2 {'acquired' if acquired_lock_b else 'failed to acquire'} lock_b at {datetime.utcnow()}")
    acquired_lock_a = lock_a.acquire(timeout=5)
    print(f"Worker 2 {'acquired' if acquired_lock_a else 'failed to acquire'} lock_a at {datetime.utcnow()}")

    if acquired_lock_b and acquired_lock_a:
        resource_a += 2
        resource_b += 2
        print(f"Worker 2 updated resource_a to {resource_a}, resource_b to {resource_b}")
        lock_a.release()
        lock_b.release()

if __name__ == "__main__":

    resource_a = 0
    resource_b = 0
    lock_a = threading.Lock()
    lock_b = threading.Lock()

    t1 = threading.Thread(target=worker_1, args=(resource_a, resource_b, lock_a, lock_b))
    t2 = threading.Thread(target=worker_2, args=(resource_a, resource_b, lock_a, lock_b))
    t1.start()
    t2.start()

    t1.join()
    t2.join()
```
    
## 寫一段有 memory leak 的示例程式  (用程式碼表示)。
    
```python
import tracemalloc, numpy as np, gc

def memory_leak():
    tracemalloc.start()
    gc.disable()
    size = 1000
    arr = []

    while True:
        for i in range(10):
            a = np.zeros((size, size), dtype=np.int)
            a += 1
            arr.append(a)

        current, peak = tracemalloc.get_traced_memory()
        print(f"Current memory usage: {current} bytes")
        print(f"Tracing memory usage: {peak} bytes")

if __name__ == "__main__":
    memory_leak()
```
    
## 查詢列表中的第一個非重複整數 (用程式表示) 列表：[3, 6,6, 3,2,1]
    
```python
def find_first_unique_integer(lst):
    return next((num for num in lst if lst.count(num) == 1), None)

if __name__ == "__main__":
    lst = [3, 6, 6, 3, 2, 1]
    result = find_first_unique_integer(lst)
    print(result)
```
    
## string = "hgijjigihdgjggeddeihjdji"，如何將字串去重複並排序？並顯示結果
    
```python
from collections import Counter

def unique_chars_with_counts(string):
    char_counts = Counter(string)
    unique_chars = sorted(char_counts.keys())
    return unique_chars, char_counts

if __name__ == "__main__":
    string = "hgijjigihdgjggeddeihjdji"
    unique_chars, char_counts = unique_chars_with_counts(string)
    print("Unique and sorted characters:", "".join(unique_chars))
    print("Character counts:", char_counts)
```
    
## 麻煩寫一段程式將[1,4,7,9] 和 [2,3,6,8] 合併為 [1,2,3,4,6,7,8,9]
    
```python
def merge_sorted_lists(lst1, lst2):
    if not (isinstance(lst1, list) and isinstance(lst2, list)):
        raise TypeError("Both inputs must be lists")
    if not all(isinstance(x, (int, float)) for x in lst1 + lst2):
        raise TypeError("All list elements must be numbers")
    return sorted(lst1 + lst2)

if __name__ == "__main__":
    lst1 = [1,4,7,9]
    lst2 = [2,3,1,8]
    merged_list = merge_sorted_lists(lst1, lst2)
    print(f"Merged and sorted list: {merged_list}")
```
    
## 如何設計 REST API ？
1. 定義資源：需要確定系統中有哪些資源需要提供給使用者。確定後需要設計 URI，使其易於識別和訪問。URI 應該清晰、簡潔且符合常規。
2. 選擇 HTTP 方法：RESTful API 使用 HTTP 方法來操作資源。根據不同的操作，選擇適當的 HTTP 方法。例如，使用 GET 方法獲取資源，使用 POST 方法創建新資源，使用 PUT 方法更新現有資源，使用 DELETE 方法刪除資源。
3. 定義資源表徵：RESTful API 通常使用 JSON 或 XML 等格式來表示資源。需要定義資源表徵格式，包括資源的欄位、數據類型等。
4. 設計輸出格式：確定您的 API 將以哪種格式（如 JSON 或 XML）返回資源。在選擇輸出格式時，需要考慮使用者對輸出格式的偏好和需求。
5. 實現安全性：API 安全性是設計 RESTful API 時必須考慮的重要因素之一。需要確保 API 服務端和使用者之間的通訊是安全的，可以使用 HTTPS 等協議實現。
6. 考慮緩存：對於需要頻繁訪問的資源，可考慮使用緩存技術提高性能和減少伺服器負載。
7. Swagger：在設計 API 時，需要提供清晰明確的文檔，以幫助使用者了解 API 的功能和使用方式。FastAPI 是自動生成文檔的好幫手。

## 解釋 GET 和 POST 的差異
|        | GET                      | POST                                    |
| ------ | ------------------------ | --------------------------------------- |
| 使用時機 | 從服務端獲取資源           | 將資源提交到服務端進行處理                |
| 安全性   | 安全、只讀、不改變資源狀態 | 可能改變資源狀態                        |
| 幂等性   | 幂等                      | 非幂等                                  |
| 資源表示方式 | URI                      | HTTP消息實體                           |
| 緩存和共享 | 可以進行緩存和共享          | 不可緩存和共享                           |
| 使用限制 | 只用於獲取資源，不提交資源或執行操作 | 用於提交資源、執行操作或觸發事件          |
  
## 解釋 POST / PUT / PATCH 在 Restful 定義下的差異與使用時機
|        | POST                 | PUT                 | PATCH               |
| ------ | -------------------- | ------------------- | ------------------- |
| 使用時機 | 創建新資源或提交子資源 | 完全替換現有資源       | 部分更新現有資源     |
| 資源狀態 | 資源不存在，創建新資源 | 資源存在，完全替換    | 資源存在，部分更新   |
| 幂等性   | 非幂等               | 幂等                | 幂等                |
| 資源表示方式 | HTTP消息實體         | URI                 | URI                 |
| 使用限制 | 可以創建新資源         | 可以完全替換現有資源 | 可以部分更新現有資源 |


## 請描述如何使用 Exception  (用程式表示)，並說明為何要使用？
    
```python
def read_file(filename):
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
            return lines
    except FileNotFoundError as e:
        print(f"Error: {e}. Please make sure the file exists and try again.")
    finally:
        if f:
            f.close()
            print(f"File {filename} is closed.")
```

1. 穩定性：程式遭遇例外狀況時，捕捉例外狀況並採取適當的措施，而不是崩潰或顯示錯誤。
2. 可讀性：例外狀況可以將錯誤處理代碼與主要邏輯分開，使程式碼更易於閱讀維護。
3. 可重用性：將錯誤處理代碼包裝在函式或類別中，則可以在多個程式中重複使用。
4. 減少複雜性：例外狀況可以減少需要處理各種錯誤情況的 if/else 語句的數量。
5. 用戶體驗：捕捉例外狀況向用戶顯示有用的錯誤訊息，可以提高用戶體驗。

## 網站需要有多個前後台角色且各自有不同權限，請說明該如何設計？
### 實現步驟：
1. 定義角色：定義系統中需要的角色，例如系統管理員、普通用戶、VIP用戶等。
2. 分配權限：為每個角色分配相應的權限，例如管理員可以編輯刪除用戶資料，普通用戶只能查看自己的資料等。
3. 指派角色：將不同的角色指派給相應的使用者。
4. 驗證權限：當用戶發出請求時，系統會根據用戶的角色進行權限驗證，判斷是否擁有相應的權限進行該操作。
### 在 Python 中實現此類權限管理的方法有很多種，以下列舉幾種：
1. Flask-Security 庫：這是一個針對 Flask 框架的安全擴展庫，提供了身份驗證、角色管理和權限控制等功能。
2. Django 框架自帶的權限系統：Django 框架中內置了權限系統，可以方便地實現權限控制。
3. Flask-Principal 库：這是一個為 Flask 應用提供權限管理支持的庫，使用它可以輕鬆實現權限控制。
4. 自己編寫權限管理代碼：開發者可以根據自己的需求編寫權限管理代碼，這需要開發者自己設計數據庫結構和編寫權限管理代碼。

## 請設計電商交易平台的資料庫，並將所有資料表透過 PK 將其關聯
資料表有 : 交易紀錄表、商品資料、賣家資料、會員資料....等

    - 交易紀錄表 (transactions)
        - id (primary key)
        - productId (foreign key to products table)
        - sellerId (foreign key to sellers table)
        - buyerId (foreign key to members table)
        - createdAt
        - amount
    - 商品資料 (products)
        - id (primary key)
        - name
        - desc
        - price
        - sellerId (foreign key to sellers table)
    - 賣家資料 (sellers)
        - id (primary key)
        - name
        - email
        - phone
    - 會員資料 (members)
        - id (primary key)
        - name
        - mail
        - phone