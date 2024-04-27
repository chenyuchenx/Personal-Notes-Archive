# AI Expo Notes

展場有許多打造基本平台的其實就是基礎的Assist不帶tools僅含基礎embedding （例如：Fairy）
雖沒有特色 也無法隨意擴充 但產品基本功能全面 容易產品化
還是要把 實驗性想法 與 產品開發 拆分 無限想要創新的想法不容易變成標準產品

- 應用
    - 創新 
    - 
    - 
- 產品
    - 不可以無限想要新增擴充功能
    - 歸一到單行業 勝過打造平台 （因資源）
    - 

IDEA
打造 crewAI Deployment
- 第三方 提供 工具 （像是人類視覺 聽覺 取用某服務的能力 某專業能力）
- 分成創建 部門 角色 任務 
使用者登入平台後 可以等於創建了一家小公司
公司裡面有哪些人可做人了事情 可由使用者創建角色 或選擇平台模版角色
角色 又可以定義 目標 背景 及其專業能力（工具）

之後可以創建部門 部門底下 建立要完成的任務後 掛載角色
自動化執行完成所有任務


## 企業導入AI所面臨的～～

### 企業高管 2022～2024AI採用態度調査
・AI 應用已從「評估期」加速推進至「導入期」且逐步證實 AI 成熟度與財務表現呈直接相關
|  | 2022 | 2023 | 2024 |
|-------|-------|-------|-------|
| 考慮評估 | 62% | 54% | 37% |
| 已導入 | 23% | 42% | 62% |
| 未考慮 | 15% | 4% | 1% |
- 導入 AI的企業比例，2022至2024年預計將提升約3倍（23%提升至62％）
- 僅1%的企業不考慮導入AI
- 企業投資AI後平均帯來該業務6.3％的營牧增長
- AI 成熱度較高的企業，營收增長的比的較高

### 企業從 +AI 到 AI+
- 由認知到行動 0~1
    - 營試使用 AI 遍地閱花但缺乏騆鐽場景 未與企業策路結合 員工自主學習，無整體培訓計畫
    - 可用場景
- 由單點進行到系統化建置 1~10
    - 有一定程度的成功案例 期待創造跨呬隊綜效 著手規割 AI 治理機制
    - 可重複部署的AI 並建立關鍵場景

### 考驗
1. 缺乏關鍵場景 (以單點式使用 AI 進行流程優化，難以創造綜效)
2. 對產出結果心存疑慮 (80％企業主管對於 AI結果可信任程度感到疑慮，擔疆 AI 導致偏見與歧視，阻礙企業優化決策)
3. 難以兼顧效益、隱私與資安(全然立基於開源資料的 AI横型，無法與競爭對手產生差異化價值)
4. 人オ與組織重塑面臨考驗(我的企業需要怎樣的AI團隊 成為一個未解之題)
### 建議
1. 符合策略的關鍵場景
2. 負責任的全流程 (從訓練、驗證、調校到部署，實現透明可解釋的AI工作流程)
3. 安全有效的取用數據（安全且有效率取用多源資料，在更短的時間用更少的数據建構AI應用）
4. 人オ與組織轉型

### 成熟的AI分析：後見之明到先見之明
- 資料收集
- 探索
- 一次性查詢
- 報告（級生情況跩厦因：級遊性貝⅔断性分析） 
- 預測性建模（可能發生情況為何？
- 規範性分析（我們該如何回應？
- 自動化決策（資料、機器與演箅法可使用於各種脈絡決策）

## 資料“整合”成為燃料是關鍵
- ”整合”以破除資料/儲存孤島
- 日益複雜的資料
    - 資料散落在各個不同的系統裡面，缺乏整體的•端到端的可視性
    - 計畫和決策都是通過 Excel 、PPT、電子郵件等工具 x:手工進行
    - 部門之間的資料傳遞以批次處理方式進行
    - 各部門的計畫不同步；在傳達有關變化的信息方面存在延誤
    - 決策是局部優化，因為它們對整個組織的影響尚末完全瞭解
- 過去個AI訓練pipeline
    - kafka資料涉入 -> spark (clean/tarnsform) -> explore -> train batch -> deploy/stream/real-time
    - 從資料管道到資料理解與轉型 大多數時間花在資料上
- Pure Storage
    - AIRIS (AI Ready Infrastructure)
    - 業界首創簡化、規模化 AI 架構
    - 符合 NVIDIA 規範
    - DGX BasePoD 參考架構
    - 支援 GPU Direct Storage
- o9
    - 基於企業知識圖譜和人工智慧的資料分析、計畫與決策支援平臺
    - 圖資料庫的優勢
        - 能夠連接不同類型數據並透濄高速運算獲得商業洞察
        - 深度3時國譜資料庫的速度比關聯式資料庫快 1000倍

## 金融業生成式AI

### 可行性應用
- Synthetic Credit Data
- Frontline Al-Copilot
- Code Conversion & Generation
- Personalized Marketing Content
    - 荷蘭安智銀行推出 Future 活動
        - 應用生成式A與消費者進行互動，使年輕人可以體驗自己退休後的場景，並考慮進行退休規畫
- Banking Fraud Prevention
- Banking Product Recommendation Assistant
- Banking Contact Center Assitant
    - Wells Fargo推tt Virtuai Assistant
        - 透過Al 助理互動使客戶掌握財務狀況
        - 幫助客戶自主財務管理，提供衡量支出、儲蓄或預算的方法
    - Lemonade 24 小時 Al理賠客服
        - Al 機器人蒐集與客戶聊天互動数據，進行智能銷售引導
        - 收集的資料可優化演算法，使公司有更高的定價和風險承擔能力，以提供更妤的理賠流程和精準的行銷策略
- Banking Customer Authentication
- AML Compliance & Reporting
- Debt Collection & Recovery Assistant
- Bank Workflow Copilot
    - 蘇黎世保險 ChatGPT 智能理賠應用
        - 進行理賠和数據挖掘，輸入近6年的理賠数據，以加速理賠效率改善承保體驗
- Al Financial Coach
    - JPMorgan 自主開發 IndexGFT
        - 透過對話了解市場上投資商品
        - 指導客戶如何申購，包含證券、慕金等金融蔏品
- Operations Redesion
    - 美國 MetLife客服語音情感分析
        - 運用 Al分析客戶語氣與情緒，改善對語品質，建議交談語氣
        - 提高客戶滿意度及減少17%客速率
> 應用資料來源：Gartner Al Use-Case Prism
### 台灣金融業運用 Al 指引"近期即將發布（2024 H1）"
- 針對 Al 治理各項原則．建立完善監管機制
- 金管會 風控
    - 保護隱私及客戶權益
    - 公平性以人為本
    - 促進永續發展
    - 建立治理與問責機制
    - 確保系統穩健與安全性
    - 落實原則
###  AI Technical Framework
- 專用服務
    - 客服行銷話術 GPTS
    - 理專行銷話術 GPTS
    - 網銀分析助手 GPTS
- 通用服務
    - 語音質檢 GPTS
    - 行銷話術 GPTS
    - 風險捕捉 GPTS
    - 分析助手 GPTS
- 潜在應用
    - 集團法規知識庫
        - 以集國遊法業務痛點出發，建酱內外規 Reg Tech.知識庫，發展智能比對、摘要等 Al 應用服務
    - 保險業務員 AI 助理
        - AI Coach 提供業務員教育訓練
            - 整理最新產品資訊及市場际劲提供業務員參考；扮演智能陪練角色擬真客戶畫像與情緒，提升業務員對話敊能，
        - 智能分析此較產品
        - 智能生成關鍵對話策略
        - 智能語音文書 CRM
        - AI 生成社群素材

## 電商與行銷行業生成式AI

### 個人化商城 (購物人格/即時動機)
- 細緻設計品貼標(強化物品開聯性)
    - Al的設計品貼標更細緻，讓商品更容易被搜尋
    - 運用 Al模型擴充標籤 由60%提升至約98%覆蓋率物品關聯性達到更高的準確度
- 深度描燴使用者軌跡（了解使用者風格德好）
    - 行為描繪，逐漸透過消費者的走逛行為收斂需求與偏好
- 強化社群關聯性

### SEO
- 困難
    - No user id 消費前不註冊
    - Cookieless 第三方cookie退場
    - 客戶數據是最常見的第一方數據
        - 導致常常再次推薦已經搜尋過的東西與網站
- Cookieless
    - Google 第三次延後
- 隱私權 （行使資料主體近用權）
    - 體驗至上的時代 （重視隱私權又同時期待個人化體驗）
        - 71% 期待品牌提供壹定程度的個人化服務 
        - 76% 不喜歡品牌展示或推數他們不想要的商品
    - Seo 近百億資料庫
    - 體驗 個人化 又要隱私
    - 客戶為中心 歷史數據（Customer data platform）
- ### 打造無需第三方 Cookte 及會員登入的嶄新 Al 應用
- 即時意圖預測
    - AI萃取產品資訊
    - Awoo BI AI行銷工具
 
## 機器人與預設性維護生成式AI
- 現代設備故障率很低不好利用歷史數據訓練ML/DL Model
- 99.9% Diagnosis accuracy
- 0 Additional sensor required
- 1-3 months Early alarm ahead of actual failure
- 0 Production line interruption

### Optimization Automatic Path Planning (ABB)
Multiple robot paths generated automatically !!!
- Transfer time: 25.32 seconds for 12 paths in total
- Time saving: (36.36-25.324)/12 = 0.92 seconds in av
- 機器人語言 repic 自然語言 對應 機器人指令

### 生成式AI
- 良率很高 瑕疵檢測很難
- 物件檢測
    - 過去AI很容易受工廠跟光影影響
- 用LLM不用重訓練
    - AMR
    - ALIF
    - Milvus (embedding DB)
- GEN AI NG Photo to Natural Language
    - Leaming of NG photos to categorize the photo according to guides and generate to-do action
- GEN AI Process Generator
    - Learing of process SOPs to make production recipes and generate action sequence file
- GEN AI Process Skill Upgrade
    - Continuously optimizing process skills and generating skill upgrades that adjust to different skills
- Adaptive system solution through RS & Opti
    - Robot hardware equipped with absolute accuracy through robot auto calibration to enable for system code upgrade to adapt to the latest program that is best fit.

## 居家健康照護市場
- US$ 303,6059 MN (2020) 預估成長 US$ 525,833.3 MN (2027)
- 在地安老
    - 以科技為核心、跨域整合、鏈結社區
    - 影響結合生成式AI分析情率 動作 行為 去執行 決策 行動
