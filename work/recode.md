# Dahboard
```
/d/06711e6159f3/online-spc-xbar-r-chart?${__cell_9}&orgId=11
/d/${__cell_10}/${__cell_11}?var-groupID=${__cell_12}&var-machineID=${__cell_13}&var-parameterID=${__cell_14}&from=${__cell_7}&to=${__cell_18}
```

# OEE

```
availability = sum(Status_1000) / (sum(Status_1000)+sum(Status_2000)+sum(Status_3000)+sum(Status_3100)+sum(Status_4000)
```

## M8 OEE 專案:
- 穩定的上下文感知能力 -> token limit 2000 BufferMemory
- 較敏感的時間感知能力 -> suffix add Date/Time
- LLM to Chat LLM -> 人性化的語意聊天
- ZERO_SHOT_REACT_DESCRIPTION -> OpenAIFunctionsAgent (BaseSingleActionAgent) -> OpenAIMultiFunctionsAgent (BaseMultiActionAgent)
- Yaml 形式的 Output -> AgentOutputParser