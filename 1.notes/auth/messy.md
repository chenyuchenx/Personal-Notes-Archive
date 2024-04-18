### Imbue
### https://zhuanlan.zhihu.com/p/661851923

---
AI Agent 是從 Context(Perception/State/Experience/World Knwoledge) 制定 Plan 走到 Policy後 執行 Action 調用 Tool Use, 通過 Feedback/Observation, 並調用 Memory 的短/長期記憶來制定找到總和結果.

---
 ChatGPT 的使用者來說，工具的應用概念應該已經相當熟悉。如果你是ChatGPT的付費用戶，你可能已經使用過插件（plugins），或者是最近推出的GPTs系列中包含的設定檔中的動作（action）——這些都是動作執行單元的實例。此外，OpenAI API版本中的 function calling，或者LangChain的 Tools，同樣也就是這個概念。

---
 ChatGPT 的使用者來說，工具的應用概念應該已經相當熟悉。如果你是ChatGPT的付費用戶，你可能已經使用過插件（plugins），或者是最近推出的GPTs系列中包含的設定檔中的動作（action）——這些都是動作執行單元的實例。此外，OpenAI API版本中的 function calling，或者LangChain的 Tools，同樣也就是這個概念。

---
從這個流程圖，我們可以如此理解 AI Agent 的整體運作機制。在處理任務之前，AI代理首先要感知(Perception) 當前環境。這包括了解系統的現狀 (State)、回顧過往經驗 (Experience)，並利用賦予的世界知識 (World Knwoledge)。這些信息形成了全面的背景知識 (Context)，使AI代理能夠為我們制定合適的計劃和做出決策 (Plan)。然後，我們設定的策略保證模組 (Policy ) 將確保代理的行動不會脫離控制或逾越許可的行為範圍。一旦通過這一模組，AI Agent 就會採取適當的行動，如果需要與外界互動 (Action)，則會透過工具 (Tool Use) 來執行。最終，AI代理與環境的互動將引來新的反饋 (Feedback)，這些反饋通過代理的觀察 (Observation )被感知，並且將需要記住的信息選擇性地儲存於適當的記憶模組中。

---
IC 製造業代工廠 ( 比較保守)
- 保守原因是因為 IC 製造業擔心機密外洩
 - 這邊可以強調我們此用地端
 - 或者有疑慮也可以使用 llm 決定參數工具但不將結果回傳LLM 但這點會怕變成有點沒有延伸擴展性, 可能在上下文或feedback上沒有發展
- OEE 設備+文檔問答 + 也可以另外製作通用的調參工具(也可能調參工具是比較適用於IC上游設計業我不確定)
- 另外這些廠商都很重視數據的穩定性, 比起問A答B, 更擔心回答A之後裡面的某一點或一個數字錯了, 差小數點也差很多, 但在我們這個工具下只要接入的數據沒有問題, 回答的答案數字也一定會正確, 不會隨意生成.
**** 良率在代工中非常重要, 可以用OEE這套去打良率檢測, 瓶頸站, 重測率, 集中性異常等
**** 代工產線的維運成品也很高, 串接異常 通知 逾時 預檢 降低維運成品

OEE Tools 優勢:
1. 數據準 錯誤率極低
2. 可根據使用者需求 決定取樣頻率 近乎及時
3. 數據面若足夠細 可分析至細節
4. 參數可以根據全線詢問出來可視化

IC 下游封裝測試廠商
- 可以用萃取工具搭配文檔案問答
- 困難點在於: 可能有些機台拿不到 log file

## MediHelper 的AI醫療助手
- 一個集成了最新醫療知識庫和數據分析功能的AI助手，能夠透過語音或文字與使用者互動，提供個性化的醫療建議和監測。
### 情境設定: 
- User：一位患有糖尿病的中年男性，正在家中管理自己的健康狀況。
### 問答示例
- User：MediHelper，今天感覺有點頭暈。
- MediHelper：
    + 思考: 基於User的背景因此從血糖著手
    + 行動: 調用了血糖檢測APP紀錄
    + 觀察: 根據紀錄的早上的血糖是180 mg/dL, 頭暈可能是高血糖的一個症狀。
    + 思考: 造成高血糖的原因
    + 行動: 調用了飲食/健康/藥物紀錄等APP
    + 觀察: User 沒有食用早餐的紀錄
    + 思考: 跳過早餐可能會影響糖尿病病患血糖控制
    + 行動: 調用網路搜尋/醫療知識庫
    + 觀察: 建議User現在可以吃一些低GI（升糖指數）的食物，如全麥麩麵包、燕麥片或者蔬菜水果，以穩定您的血糖水平。同時，請確保您按時服用您的糖尿病藥物，
    + 思考: 尋找最近可以買到GI食物的地方, 全麥麩麵包、燕麥片判段超市就有
    + 行動: 調用User GPS與地圖工具
    + 觀察: User 直走200m 有一家7-11.
+ MediHelper：根據紀錄您今早的血糖為180 mg/dL, 且查無您有使用早餐之紀錄, 因此判斷跳過早餐可能影響您的血糖控制，尤其是對於糖尿病患者來說。建議您可以食用一些麥麩麵包、燕麥片以穩定您的血糖水平。同時，請確保您按時服用您的糖尿病藥物。如果您打算購入一些建議食品, 直走200m 直行於民生東路四段上, 您會看到一家7-11便利店, 可購買相關物品, 如您的頭暈情況持續或惡化，建議您立即就醫，以確保您的安全。
- User：好的，謝謝！
+ MediHelper：不用客氣，隨時為您服務。如果您有任何其他問題或需要進一步協助，請隨時告訴我。祝您健康！


## MediHelper 的AI醫療助手
- 一個集成了最新醫療知識庫和數據分析功能的AI助手，能夠透過語音或文字與使用者互動，提供個性化的醫療建議和監測。
### 情境設定: 
病人在診間與醫生進行了一次詳細的健康檢查和諮詢。在整個過程中，AI助理作為一個觀察者和記錄者，全程記錄了對話和診療細節。診療結束後，病人希望透過AI助理來更好地理解醫生的診斷和建議。
### 問答示例
- User：AI，你能幫我總結一下醫生剛才談到的主要診斷和建議嗎？
+ MediHelper：當然可以。根據剛才的對話，醫生提到您目前的主要問題是高血壓和膽固醇偏高。醫生建議您應該調整飲食，減少鹽分和油脂的攝入，並且建議您每週至少進行三次中等強度的運動，如快走或游泳。
- User：他有提到需要服用藥物嗎？
+ MediHelper：是的，醫生為您開了兩種藥物，一種是用來控制血壓的，另一種則是用來調節膽固醇的。醫生強調，定期回診檢查是非常重要的，以便根據您的身體狀況調整治療計劃。
- User：那些藥物有什麼副作用嗎？
+ MediHelper：根據醫生的說明，血壓藥物可能會導致一些輕微的副作用，如頭暈或疲勞感，而調節膽固醇的藥物則可能會引起消化不良或肌肉痠痛。如果您感受到這些副作用，應及時與醫生聯繫。
- User：醫生有沒有提到下次回診的時間？
+ MediHelper：是的，醫生建議您在六週後回診，以檢查藥物的效果和您的健康狀況。此外，如果在這段時間內您感覺身體有任何不適，應立即預約提前看診。
- User：謝謝你，AI。這對我很有幫助。我能把這次對話的摘要發送到我的郵箱裡嗎？
+ MediHelper：當然可以，我將把今天的診療摘要和重要建議發送到您的郵箱。如果您有任何疑問或需要進一步的幫助，隨時可以聯繫我。
- User：太好了，謝謝






















