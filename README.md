# Customer Complaint to Escalation Summary Prototype

## 1. Project overview

This small Python project turns customer complaints into short internal escalation summaries. It is a homework prototype to show how raw customer feedback can be rewritten for internal teams.

This project uses an LLM API (OpenAI GPT model) to generate escalation summaries.

---

## 2. Business workflow

1. A customer complaint is received.
2. The complaint text is analyzed for the main issue, urgency, and customer impact.
3. The system creates a clear summary for the internal escalation team.
4. The summary is shared with support, operations, or engineering so they can act faster.

---

## 3. User, input, and output

- User: a student or developer testing the prototype.
- Input: a customer complaint written in plain language.
- Output: a concise escalation summary that highlights the problem, impact, and next steps.

---

## 4. Why this task is valuable

This task is valuable because it helps teams respond faster to customer issues. It also makes communication more consistent and saves time by turning messy complaints into action-ready messages.

---

## 5. File structure

- `app.py` — main program that converts complaints into summaries  
- `prompts.md` — prompt development and iteration  
- `eval_set.md` — evaluation cases and expected behavior  
- `report.md` — analysis and findings  
- `README.md` — project overview and usage guide  

---

## 6. How to run the app

1. Make sure you have Python installed and the required package:

```bash
pip install openai
```

2. Set your API key:

```bash
export OPENAI_API_KEY="your_api_key"
```

3. Run the app:

```bash
python app.py
```

4. Enter a customer complaint and review the generated summary.

Note: This is a prototype for learning and experimentation, not a production system.

Video Link：https://vimeo.com/1180276244?share=copy&fl=sv&fe=ci