# LLM

+ GPT-4 Turbo的上下文長度可達300頁，128K TOKEN。
+ 更新增加了對.Json文件的呼叫和控制。
+ 可以利用.Json文件來隨機產生提示詞和描述。
+ 更新包含了Assistants API Function Calling的精確呼叫。
+ 可根據Seed產生可重複的輸出。


> RAG接近給模型基於特定問題的上下文知識。 引入新的訊息，這些訊息可能不在LLM中。
使用RAG控制內容來減少幻覺（模型產生與現實不符的輸出），這是RAG的常見用途。
通常的用例是提供內容給模型，並指示它僅使用該內容來回答問題，不使用LLM自有的知識，
以此限制回答來自特定的知識庫，減少幻覺。

Fine-tuning / RAG / FaultGuardian