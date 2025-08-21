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
