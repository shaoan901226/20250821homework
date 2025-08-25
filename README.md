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

＃實例化需求（用 Given / When / Then 格式）


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
