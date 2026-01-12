"""
llm_client.py
--------------
Wrapper để gọi LLM (Google Gemini thông qua OpenAI-compatible API).
Tools chỉ tập trung vào logic, không lo config/thought.
"""

import os
from dotenv import load_dotenv
from openai import OpenAI
# Load biến môi trường từ file .env
load_dotenv()

# 1. Đọc config từ environment
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", None)
if not GEMINI_API_KEY:
    raise RuntimeError("Missing GEMINI_API_KEY in environment variables")

# 2. Khởi tạo client để gọi Gemini
client = OpenAI(
    api_key=GEMINI_API_KEY,
    # Đây là endpoint OpenAI-compatible của Gemini
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

def call_llm(prompt: str, model: str = "gemini-2.5-flash") -> str:
    """
    Gửi một prompt đến Gemini và trả về text output.
    
    - prompt: nội dung cần LLM phân tích/sinh output
    - model: tên model Gemini; có thể thay thành gemini-2.5-pro, gemini-3, ...
    """
    # Xây payload để gọi ChatCompletion
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful, precise test design assistant."},
            {"role": "user", "content": prompt}
        ],
        # Có thể cấu hình reasoning/extra_body nếu cần
        # extra_body={"google": {"thinking_config": {"thinking_budget": "high"}}}
    )

    print("LLM response:", response)

    # Trả kết quả text
    # choices[0].message.content là định dạng chuẩn khi gọi OpenAI-compatible API
    return response.choices[0].message.content


