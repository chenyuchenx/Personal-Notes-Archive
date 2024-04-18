# FastAPI

## 特性
- 快速：可与 NodeJS 和 Go 比肩的极高性能（归功于 Starlette 和 Pydantic）。最快的 Python web 框架之一。
- 高效编码：提高功能开发速度约 200％ 至 300％。*
- 更少 bug：减少约 40％ 的人为（开发者）导致错误。*
- 智能：极佳的编辑器支持。处处皆可自动补全，减少调试时间。
- 简单：设计的易于使用和学习，阅读文档的时间更短。
- 简短：使代码重复最小化。通过不同的参数声明实现丰富功能。bug 更少。
- 健壮：生产可用级别的代码。还有自动生成的交互式文档。
- 标准化：基于（并完全兼容）API 的相关开放标准：OpenAPI (以前被称为 Swagger) 和 JSON Schema。

```
uvicorn main:app --host 0.0.0.0 --port 5000 --reload
```

### 關於 Field 字段參數說明 
**[Field documents](https://www.cnblogs.com/yoyoketang/p/15923431.html)**
- Field(None) 是可選字段，不傳的時候值默認為None
- Field(...) 是設置必填項字段
- title 自定義標題，如果沒有默認就是字段屬性的值
- description 定義字段描述內容

### **pydantic 設定管理**
- [doc setting](https://fastapi.tiangolo.com/zh/tutorial/metadata/)
- pydantic 的設定管理可以透過繼承 BaseSettings 類別進行實作
- 該類別與 BaseModel 類別最大差別在於 BaseSettings 提供環境變數(environment variables)與 dotenv 的整合。

### 你可以配置兩個文檔用戶界面，包括：
- Swagger UI：服務於 /docs。
    - 可以使用參數 docs_url 設置它的 URL。
    - 可以通過設置 docs_url=None 禁用它。
- ReDoc：服務於 /redoc。
    - 可以使用參數 redoc_url 設置它的 URL。
    - 可以通過設置 redoc_url=None 禁用它。