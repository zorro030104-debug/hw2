# Prompt Development for Escalation Summary Prototype

## Initial prompt

You are a support assistant. Read the customer complaint and write a short internal escalation summary. Keep the summary concise and include the main issue, customer impact, and suggested next step.

---

## Revision 1

You are an internal escalation writer. Given a customer complaint, create a concise, structured summary for the support team. Include:
- the key problem,
- why it matters to the customer,
- what the internal team should do next.

Avoid adding details that are not in the complaint.

**What changed and why:**
Added clearer structure and defined expected outputs (problem, impact, next steps) to improve consistency and reduce vague responses.

**What improved or still failed:**
The output became more structured and easier to evaluate, but the model still introduced inferred details in ambiguous cases.

---

## Revision 2

You are an internal escalation writer. Convert the customer complaint into a short, structured escalation summary with these sections:
- Problem
- Impact
- Recommended action

Use only information from the complaint. If the complaint is unclear or contradictory, say that the issue needs human review instead of guessing.

**What changed and why:**
Added explicit section headings and stronger constraints to prevent hallucination and enforce human review for unclear inputs.

**What improved or still failed:**
The model showed improved format consistency and reduced hallucination. However, it still failed on unintelligible inputs and occasionally deviated from the required format.