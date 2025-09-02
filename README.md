# 實例化需求（用 Given / When / Then 格式）


案例 1：成功登入

Given 使用者帳號存在，帳號為 user01，密碼為 123456
When 使用者輸入帳號 user01，密碼 123456 並點擊登入
Then 系統顯示「登入成功」並導向首頁

案例 2：密碼錯誤登入失敗
Given 使用者帳號存在，帳號為 user01，正確密碼為 123456
When 使用者輸入帳號 user01，密碼 654321 並點擊登入
Then 系統顯示「帳號或密碼錯誤」

案例 3：不存在的帳號
Given 系統中沒有帳號 ghost99
When 使用者輸入帳號 ghost99，密碼 anypass 並點擊登入
Then 系統顯示「帳號不存在」

驗收時間: 8/22 17:00
驗收環境: VSCode or Cursor
請上傳GitHub並開放下載編輯
程式語言: 任意

# 作業主題: [重構]
1. 附檔名錯誤, python 程式副檔名請用 py
2. 請重構程式, 登入畫面建立類別 LoginWindow
3. 帳號與密碼, 建立類別 Account, 內含 username, password, 由建構式建立
4. 檢查密碼帳號, 請用 Account 的方法 verify_password


實例化需求（用 Given / When / Then 格式）[重構]


案例 1：成功登入

Given 使用者帳號存在，帳號為 user01，密碼為 123456
When 使用者輸入帳號 user01，密碼 123456 並點擊登入
Then 系統顯示「登入成功」並導向首頁

案例 2：密碼錯誤登入失敗
Given 使用者帳號存在，帳號為 user01，正確密碼為 123456
When 使用者輸入帳號 user01，密碼 654321 並點擊登入
Then 系統顯示「帳號或密碼錯誤」

案例 3：不存在的帳號
Given 系統中沒有帳號 ghost99
When 使用者輸入帳號 ghost99，密碼 anypass 並點擊登入
Then 系統顯示「帳號不存在」

驗收時間: 8/23 17:00
驗收環境: VSCode or Cursor
請上傳GitHub並開放下載編輯
程式語言: python

案例 3：不存在的帳號
Given 系統中沒有帳號 ghost99
When 使用者輸入帳號 ghost99，密碼 anypass 並點擊登入
Then 系統顯示「帳號不存在」

# 實例化需求（用 Given / When / Then 格式）


案例 1：成功創建帳號
Given Login畫面增加一個創建帳號按鈕
When 使用者點擊創建帳號按鈕，輸入帳號為 user02，密碼為 13579ab
Then 系統顯示「成功創建帳號」

案例 2：創建帳號未輸入帳號
Given Login畫面增加一個創建帳號按鈕
When 使用者點擊創建帳號按鈕，輸入帳號為 空白，密碼為 13579ab
Then 系統顯示「使用者名稱不得為空白」

案例 3：創建帳號但帳號已經存在
Given Login畫面增加一個創建帳號按鈕
When 使用者點擊創建帳號按鈕，輸入帳號為 user01，密碼為 24682468

# 實例化需求（用 Given / When / Then 格式）


案例 1：成功創建帳號 下次執行時 帳號還存在
Given Login畫面增加一個創建帳號按鈕
When 使用者點擊創建帳號按鈕，輸入帳號為 user02，密碼為 13579ab
Then 系統顯示「成功創建帳號」

案例 2：關閉再重啟 創建相同帳號 跳出 「使用者名稱已經存在」
Given 重啟APP, 點擊創建帳號按鈕
When 使用者點擊創建帳號按鈕，輸入帳號為 user02，密碼為 13579ab
Then 系統顯示「使用者名稱已經存在」

# * 重構function call, 消除 code smell - long parameter list
* Account 增加欄位: 性別, 生日, 電子郵件
* 建立帳號時 輸入上述欄位
* 登入後, 在首頁顯示: 帳號, 性別, 生日, 電子郵件

# VARCHAR
VARCHAR = Variable Character

文字長度可以變動，不像 CHAR(n) 固定長度。
255 → 最多可存 255 個字元。
如果存的字比 255 短，只會用到實際長度，不會浪費空間。

用途:
存使用者名稱、密碼、電子郵件等文字。
適合長度不固定的文字欄位。

# Code Smell
「Code Smell」是程式設計領域的一個術語，用來描述 程式碼中可能存在設計問題或潛在缺陷的跡象，但它不是明確的錯誤，也不一定會馬上導致程式錯誤。換句話說，它是一種「程式味道不好」的警告。

特點:
不是錯誤
程式碼仍然可以正常運行。
提示潛在問題
可能會導致後續維護困難、擴充性差或容易出錯。
通常需要重構（Refactoring）
透過改善程式結構來解決。

| 類型 | 說明 | 範例 | 改進方式 |
|------|------|------|----------|
| 重複程式碼 (Duplicated Code) | 相同或非常相似的程式碼出現多次 | `def add_user(): ...` `def add_admin(): ...` | 抽象成共用函式或類別 |
| 過長方法 (Long Method) | 一個函數做太多事情，難以維護 | ```def process(): do_a(); do_b(); do_c(); do_d()``` | 拆分成多個小函式 |
| 過長類別 (Large Class) | 類別承擔過多職責 | ```class Manager: def add(): ... def delete(): ... def report(): ...``` | 將職責分散到多個類別 |
| 神奇數字 (Magic Number) | 直接使用數字常數而非命名常數 | `if status == 3:` | 使用具名常數 `STATUS_APPROVED = 3` |
| 過多參數 (Long Parameter List) | 函式參數過多 | `def register_user(name, age, email, phone, address): ...` | 封裝成資料物件或字典 |
| 低內聚 (Low Cohesion) | 類別中方法之間關聯性低 | `class Util: def login(): ... def send_email(): ...` | 將方法分散到功能相關的類別 |
| 高耦合 (High Coupling) | 類別依賴過多，修改影響範圍大 | `class A: def __init__(self, b, c, d): ...` | 使用依賴注入或介面 |
| 不必要的註解 (Commented Out Code) | 註解掉的程式碼過多 | `# old_login()` | 移除，或放版本控制 |
| 過度使用全域變數 (Global Variable Overuse) | 多個函式共用全域變數 | `x = 10` 多處使用 | 封裝成類別屬性或傳入參數 |
| 過度複雜條件 (Complex Conditional) | if/else 過於複雜 | `if a and b or c and not d:` | 拆分條件，或用策略模式 |
