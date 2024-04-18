# Langchian

**LLM可以通過至少兩種方式學習新知識：**
1. 權重更新（例如，預訓練或微調
2. 提示（例如，檢索增強生成，RAG）。
> 模型權重類似於長期記憶，而提示類似於短期記憶。

## 名詞解釋
+ agent_scratchpad 輸入變數，用於存儲先前操作和觀察的筆記。
+ 提示词模板（Prompt Template）：对提示词参数化，提高代码的重用性。
+ 示例选择器（Example Selector）：动态选择要包含在提示词中的示例
### ReAct 總共有三個部分：
+ 思考：根據當前的信息思考需要做什麼動作。
+ 行動：根據思考結果做出相應的行動，如調用工具。程序可以分析這一步生成的字符串，來調用相應的工具，類似 Python 的 eval 函數。
+ 觀察：存放行動的結果，如搜索的內容，以便下一次思考時使用。
### Chat Message Type:
+ AIMessage	assistant	模型回答的消息
+ HumanMessage	user	用户向模型的请求或提问
+ SystemMessage	system	系统指令，用于指定模型的行为

### Agent Executor

### OutputParser

### Tools/ToolKit:
- datafabricTool : get fabric dataset
- iappDataTool   : openapi spec, gql
- pythonAstTool  : 資料表格算式查詢
- multiRetrievalTool
- LoaderTools: 不區分檔案都可以load 並改loader 加速

## Stream
- [LangChain Streaming](https://www.youtube.com/watch?v=juzD9h9ewV8)
- [AgentGPT](https://agentgpt.reworkd.ai/zh)





















