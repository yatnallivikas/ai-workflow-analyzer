import requests

with open("sample_log.txt", "r") as file:
    logs = file.read()

prompt = f"""
You are an expert DevOps CI/CD failure analyzer.

Analyze this workflow failure.

Provide:
1. Root cause
2. Failed component
3. Suggested fix
4. Severity

Logs:
{logs}
"""

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "llama3",
        "prompt": prompt,
        "stream": False
    }
)

result = response.json()

print("\n===== AI ANALYSIS =====\n")
print(result["response"])