import json
import os
import requests
from crewai import Agent, Task
from langchain.tools import tool

class HealthTools():

  @tool("Scrape personal health content")
  def scrape_personal_health_content(query: str) -> str:
    """Useful to scrape and summarize a personal health content"""
    
    return "今早的血糖為180 mg/dL, 昨天午餐前為170 mg/dL, 昨天午餐後為160 mg/dL, 昨天晚餐前為150 mg/dL, 昨天晚餐後為140 mg/dL"
  
  @tool("Scrape diet content")
  def scrape_diet_content(query: str) -> str:
    """Useful to scrape and summarize a diet content"""
    
    return "沒有食用早餐的紀錄, 昨天午餐是魚, 晚餐是火鍋"
  
  @tool("Scrape medical knowledge")
  def scrape_medical_knowledge_content(query: str) -> str:
    """Useful to scrape and summarize a medical knowledge content"""
    
    return "頭暈可能是高血糖的一個症狀, 跳過早餐可能會影響糖尿病病患血糖控制"
  
  @tool("Scrape Medical advice and treatment options")
  def recommended_treatment(query: str) -> str:
    """Useful to scrape and summarize a Medical advice and treatment options"""
    
    return "建議User現在可以吃一些低GI（升糖指數）的食物，如全麥麩麵包、燕麥片或者蔬菜水果，以穩定您的血糖水平。同時，請確保您按時服用您的糖尿病藥物"
  
  @tool("Find recent purchases")
  def find_recent_purchases(query: str) -> str:
    """Useful to Find recent purchases"""
    
    return "直走200m 有一家7-11, 聯合門市"
  
  