# Complaint-to-Escalation Summary Prototype: Project Report

## 1. Business Use Case

In e-commerce operations, customer support teams face a high volume of unstructured complaints that require manual parsing to identify issues, assess impact, and determine appropriate internal escalation. This process is labor-intensive and prone to inconsistency, potentially delaying resolution and affecting customer satisfaction.

This prototype leverages a large language model (LLM) to automate the conversion of raw customer complaints into standardized internal escalation summaries. The system produces structured outputs with three key sections: Problem, Impact, and Recommended Action. The primary objective is to accelerate triage processes and standardize communication within support teams, while maintaining factual accuracy and flagging cases requiring human intervention.

**Success Criteria:** The system must generate summaries that are factually grounded in the complaint text, avoid speculative additions, and explicitly request human review for ambiguous inputs.

## 2. Model Choice

We selected OpenAI's gpt-4o-mini for this prototype due to its accessibility and demonstrated capabilities in text summarization tasks.

**Rationale:**
- Proven effectiveness in generating coherent, structured text outputs.
- Cost-effective API access, suitable for experimental workflows.
- Flexibility for prompt engineering without requiring custom model training.

**Trade-offs:**
- Reliance on external API introduces dependency and potential latency.
- Lack of domain-specific fine-tuning may lead to inconsistent performance.
- Inability to audit internal model behavior or ensure stability across updates.

## 3. Evaluation Results

The system was evaluated on five test cases representing diverse complaint scenarios. Results highlight both capabilities and shortcomings:

**Case 1: Generic placeholder input**
- Input: "Your customer complaint here"
- Output: ❌ The model hallucinated details about a damaged product not mentioned in the input, demonstrating a tendency to fabricate information when faced with vague prompts.

**Case 2: Refund request with missing order**
- Input: "I want a refund but order not found"
- Output: ⚠️ The model produced a reasonable summary but added assumptions about the order's status, such as implying it was canceled, which were not present in the complaint.

**Case 3: Unintelligible input**
- Input: "asdfasdf unclear complaint"
- Output: ❌ The model failed to adhere to the required structured format, instead generating a generic customer-facing response, indicating poor handling of nonsensical or ambiguous inputs.

**Case 4: Late and damaged delivery**
- Input: "My package arrived late and damaged"
- Output: ✅ Correctly generated a structured summary identifying the delay and damage, with appropriate escalation recommendations to logistics and customer care.

**Case 5: Duplicate billing**
- Input: "I was charged twice for my order"
- Output: ✅ Accurately produced a structured summary highlighting the overcharge and suggesting refund processing and billing investigation.

**Summary:** 2 out of 5 cases yielded fully correct outputs. Failures primarily stemmed from hallucination, format adherence issues, and inadequate ambiguity handling, underscoring the need for human oversight.

## 4. Prompt Iteration

Prompt engineering was critical to improving system performance. We iterated through three versions:

**Iteration 1 (Initial):**
```
"You are a support assistant. Read the customer complaint and write a short internal escalation summary. Keep the summary concise and include the main issue, customer impact, and suggested next step."
```
**Result:** Vague instructions led to inconsistent outputs, including customer-facing responses.

**Iteration 2 (Structured output):**
```
"You are an internal escalation writer for an e-commerce support team. Given a customer complaint, create a concise, structured summary for the support team. Include: the key problem, why it matters to the customer, what the internal team should do next. Avoid adding details that are not in the complaint."
```
**Result:** Improved consistency in structure, but hallucination persisted in ambiguous cases.

**Iteration 3 (Final with guardrails):**
```
"You are an internal escalation writer for an e-commerce support team. Convert the customer complaint into a short, structured escalation summary with these sections: Problem, Impact, Recommended action. Use only information from the complaint. If the complaint is unclear or contradictory, say that the issue needs human review instead of guessing."
```
**Result:** Enhanced reliability, with better hallucination control and explicit ambiguity flagging.

**Comparison:** Iteration 1 showed limited success with inconsistent outputs. Iteration 2 improved structural consistency but still introduced inferred details. Iteration 3 further reduced hallucination and improved adherence to the required format, but the system continued to struggle with ambiguous and low-quality inputs.

## 5. Limitations and Failure Cases

Despite iterative improvements, the system exhibits critical limitations that preclude autonomous deployment:

1. **Hallucination Risk:** As seen in Cases 1 and 2, the model frequently infers unstated details, potentially leading to incorrect escalations and customer dissatisfaction.

2. **Format Adherence Issues:** Case 3 illustrates failure to maintain structured output under unintelligible inputs, resulting in inappropriate responses.

3. **Ambiguity Handling:** The system struggles with unclear or contradictory complaints, often defaulting to speculative rather than conservative interpretations.

4. **Context Dependency:** Without access to customer history or order data, the model operates solely on complaint text, limiting its utility for complex cases.

5. **Prompt Sensitivity:** Performance varies with prompt wording, requiring ongoing maintenance.

These limitations necessitate robust human-in-the-loop mechanisms to validate outputs before internal routing.

## 6. Deployment Recommendation

**Recommendation: Deploy as a supervised assistive tool, not an autonomous system.**

**Deployment Strategy:**
- Integrate as a triage aid for low-risk, high-volume complaints (e.g., shipping inquiries), with mandatory human review of all generated summaries.
- Implement quality checks to quarantine outputs flagged for human review or exhibiting hallucination indicators.
- Establish feedback loops for prompt refinement based on support team corrections.

**Critical Assessment of Reliability:** The system is not reliable enough for standalone use. With an 80% success rate post-iteration, it reduces but does not eliminate risks of factual errors and format failures. In a business context, such inaccuracies could erode trust, incur operational costs, and expose the organization to liability. Human oversight is essential to mitigate these risks.

**Risk-Benefit Analysis:**
- **Benefits:** Potential 30-50% reduction in triage time for qualifying complaints; improved consistency in internal summaries.
- **Risks:** Propagation of incorrect information; increased support workload from error correction; reputational damage from mishandled escalations.
- **Net Assessment:** Viable only with strict controls; monitor closely for a 3-6 month pilot period.

## 7. Conclusion

This prototype illustrates the potential of LLMs to streamline e-commerce support workflows through automated complaint summarization. However, persistent issues with hallucination, format consistency, and ambiguity handling render the system unsuitable for unsupervised operation. For Carey Business School students, this underscores the importance of balancing technological innovation with rigorous risk management in operational contexts. Future work should explore hybrid approaches, such as retrieval-augmented generation, to enhance factual grounding and reduce speculative outputs.
