## User Account
- li.yang@advantech.com.cn // Yh0123654.
- devanliang@iii.org.tw // Abcd1234#
- daniel.chiu@advantech.com.tw // a3787e83@Ss0
- daniel.chiu@advantech.com.tw // 472259c3@Ss0
- ifs@advantech.com // password
- sa.jing@advantech.com.cn // !QAZ2wsx
- lisa6222lisa@gmail.com // 3edc@WSX
- kenny.chen@iii.org.tw // !QAZ2wsx
- cj827iii@gmail.com // 1qaz@WSX

## 研華 AIFS-AutoML
 - https://www.youtube.com/watch?v=XJqjVuypyMA

## 研華 AIFS-DeployMent
- https://portal-afs-stage2-eks006.sa.wise-paas.com/v2/2174f980-0fc1-5b88-913b-2db9c1deccc5/dataset
- lisa6222lisa@gmail.com
- 3edc@WSX

## 推論平台測試網址:
- http://203.74.121.112:55682/　
- 測試帳號:advantech / advantech

## SSO 開通權限
- https://portal-sso-ensaas.sa.wise-paas.com/users
- IAPP
    - X-Ifp-Api-Key : ZJkJSPQzhQAH4qRQ.wSdy05bVoIvdf-pt-vbHVAXhdR3ndvYW
    - harbor.arfa.wise-paas.com/ifp/ifps-inference-api:1.0.1.7
- https://whimsical.com/software-structure-MKsTeArpdd5FcMyGgao1qi
- https://portal-sso-ensaas.bj.wise-paas.cn/
- https://portal-sso-ensaas.bj.wise-paas.com.cn/

- https://dev.azure.com/ADVIFACTORY/WISE-Factory_Public/_git/release-notes

## M 林口 B2  電頻冰水主機 
- 溫度 溼度 壓力 流量 電力消耗 負載
- 時間 保持開機
- 預測效能係數 COP 製冷量
- 目前做法先尋找並定義一個預測問題, 可能是HVAC配EHS或者稼動率配OEE, 並釐清資料與拓樸集合來源, 建立預訓練模型, 輕量開發IAI.Predict.Retrain微服務來串通上述路由, 用以驗證架構是否運作.

## IAI.Predict.Retrain && WISE-AIFS/DevelopmentService 優點:
1. 容器可以較輕量化百分之40-60% (依套件大小所做評估)
	- 這部分獨立後亦是可以優化的, 可以優化20-30%.
2. 可以跑較大型的訓練 可調GPU加速訓練過程

## 獨立 IAI.Predict.Retrain 優點:
1. 獲取資料集合到開始訓練速度較快
2. 使用自有環境Minio作為模型倉儲 達到遺失重獲取 未來下發使用
3. 可免除不同環境/版本之DS訂閱溝通問題
4. 模型打包與再訓練驗證測試較快

## 可預測設備
- Gearbox
- Oil-injection screw compressor
- Industry bearing
- Lithium-Ion Battery
- HVAC

---
- 3-dimensional Kalman filter - 三維卡爾曼濾波
- MLE Kalman filter - 最大似然估計卡爾曼濾波
---
- 離職率預測 : 降低中高階人才流動率
- 設備預防維修(設備異常預測): 降低異常損失成本
- 不良預測: 降低成本改善品質
- 連續型製程虛擬量測(製程失效因子分析): 有效提升產品品質，檢驗成本與時間降低
- 用電預測與節電優化: 提供預測性可讓生產能源有更多的預先處置時間
- 原物料採購價格趨勢預測: 有效調節採購與安全庫存數量
- 供應鏈需求預測: 
- 原材料價格預測: 
---
- 用於橋樑結構健康監測的高速分佈式數據採集系統
- 鋼鐵製造機器狀態監測系統
- 油氣管道洩漏檢測解決方案
---
+ 設備感測器 --> PCIE --> DaQNavi (MCM Catcher)
    + PCIE-1802 動態數據採集卡提供 8 組同步採集通道
    + 每秒可同時採樣多達 160 萬個振動信號
---
+ 機械手臂(砝碼, 負重)原始數據可分為 : 
    + 加速度 扭矩 電流 --> CV (不同特徵不同問題的CV閥值不同)
    + 4軸5秒不更新判斷行停機
    + 單機台異常紀錄一天一筆
---

## 製程管理
善用 AI 數據將是串連產線、廠務管理、物流、產品銷售供應鏈的關鍵。只要能掌握數據流，開始導入 AI 模型，就有機會輔助增進產線生產效率、提升產品良率、做到預防性維修與持續往高度自動化工廠做升級。

1. IQC進料檢驗  (Incoming Quality Control).
   主要是控制來料的品質管控
2. IPQCS製程品管  (In Process Quality Control) --針對生產線
    針對製程上的品質管控(某些公司的IPQC會握有稽核的權力), 品保會在產線上巡檢
3. PQC半成品檢驗  (Process Quality Control) --針對半成品
4. FQC產終檢驗  (Final Quality Control)
    在包裝的尾期進成品檢驗 , 同時也是產品出貨之前需做的最後檢驗
5. OQC出貨檢驗  (Out-going Quality Control)
    針對成品要出貨的物品品質管控,  尚未要立即出貨的成品則入庫管理
---
- 統計製程管制(Statistical Process Control, SPC)
- 工程製程管制(Engineering Process Control, EPC)
- 過程質量控制（製程質量控制），(Process Quality Control)PQC
---
+ 混合- 作業員調動頻繁
+ 層化- 管制界限計算錯誤
+ 趨勢- 設備逐漸老化 工人疲勞 進料品質漂移
+ 循環- 工具磨損 量測設備使用順序的不同
+ 流程水平改變- 新的供應商 新的操作員 檢驗儀器或方法的改變
---
+ 研發配方最佳化: 運用機器學習建立模型縮短實驗組數，大幅減少實驗組數以及成本
+ 設備參數最佳化: 有效提升產品品質，老師傅經驗傳承：內部專家系統建置
+ 鎳化金厚度預測: 貴金屬用料成本降低 ，提升產品品質，檢驗成本與時間降低 
---
+ EMS: 印刷機參數推薦提高直通率
+ PCB: 化鎳金厚度預測 降低原料成本
+ 光電面板: 虛擬量測 縮短NPI時間
+ 半導體封測: 焊線機參數推薦 提高生產效率
+ IC設計: IC庫存優化 提高 達交率
+ 石化橡膠: 煉油參數最佳化 增加利潤
+ 食品醫藥: 研發配方​ 研發配方最佳化 縮短研發時間
---