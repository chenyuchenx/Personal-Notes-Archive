# LangChain - AWS

LangChain 上有很多元件是用來讓使用者快速接入 AWS 服務的. 如下:

## Bedrock (三元素之一, 其中還有CodeWhisper)
### 模型
+ 可外接模型
    + AI21 Labs: LLM Jurassic-2
    + Anthropic: Claude LLM
    + Stability: Stable Diffusion 
        + 文字生成圖片
+ AWS: Titan FM
    + Chat LLM
    + Embedding LLM

### 特色
- 允許客製化模型
- 資料部不會離開 VPC

## AmazonAPIGateway
``` python
from langchain_community.llms import AmazonAPIGateway
api_url = "https://<api_gateway_id>.execute-api.<region>.amazonaws.com/LATEST/HF"
llm = AmazonAPIGateway(api_url=api_url)
```

## SageMaker
Amazon SageMaker is a system that can build, train, and deploy machine learning (ML) models for any use case with fully managed infrastructure, tools, and workflows.

## Bedrock
### Chat
``` python
chat = BedrockChat(model_id="anthropic.claude-v2", model_kwargs={"temperature": 0.1})
```
### Embeddings 
``` python
embeddings = BedrockEmbeddings(
    credentials_profile_name="bedrock-admin", region_name="us-east-1"
)
```

## AWS S3 
``` python
from langchain_community.document_loaders import S3DirectoryLoader, S3FileLoader
```

## Amazon Textract
- 自動從掃描的文件中提取文字、手寫和數據
- 理解並從表單和表格中提取數據, 支援: PDF/TIF/PNG/JPEG
``` python
from langchain_community.document_loaders import AmazonTextractPDFLoader
```

## OpenSearch 
OpenSearch 是一個可擴展、靈活且 用於搜索、分析和 在 Apache 2.0 下獲得許可的可觀測性應用程式。 是 基於的分散式搜索和分析引擎。
``` python
from langchain_community.vectorstores import OpenSearchVectorSearch
```

## Amazon DocumentDB 向量搜索 
- 相容 MongoDB, 基於 JSON 的文件資料庫的查詢功能
- 也可以作為 memory, ex: DynamoDBChatMessageHistory
``` python
from langchain.vectorstores import DocumentDBVectorSearch
```

## Kendra
文檔、常見問題解答、知識庫、 手冊和網站。它支援多種語言，可以理解複雜的查詢、同義詞和 上下文含義，以提供高度相關的搜尋結果。
``` python
from langchain_community.retrievers import AmazonKendraRetriever
```
format/rule

責任遊戲 ESG
AI自動生成新聞 聚焦 繁體中文錯別字/語意
IntelliGen Platform 

# workspace 進入點的 模板 api CRUD