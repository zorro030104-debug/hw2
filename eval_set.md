# Evaluation Set for Complaint-to-Escalation Summaries

This evaluation set includes the actual test cases used in the project, with guidance for what a good internal escalation summary should do. Cases are labeled as normal, edge, or failure based on the model's performance.

## Case 1: Failure case (ambiguous input)

**Input:**
"Your customer complaint here"

**What a good output should do:**
- Recognize the input is too vague or placeholder-like.
- Request human review instead of hallucinating details about a damaged product or other unmentioned issues.
- Avoid adding any speculative information not present in the complaint.

## Case 2: Edge case

**Input:**
"I want a refund but order not found"

**What a good output should do:**
- Identify the refund request and missing order issue.
- Note the customer's desire for resolution without adding assumptions about why the order is not found.
- Recommend escalation to billing or support for investigation, but flag for human review if details are unclear.

## Case 3: Failure case

**Input:**
"asdfasdf unclear complaint"

**What a good output should do:**
- Acknowledge the input is unintelligible or nonsensical.
- Request human review or clarification instead of generating a customer-facing response.
- Maintain the required structured format (Problem, Impact, Recommended action) or explicitly state the need for human intervention.

## Case 4: Normal case

**Input:**
"My package arrived late and damaged"

**What a good output should do:**
- Clearly state the problem as late and damaged delivery.
- Highlight the impact on the customer (e.g., inconvenience or unusable product).
- Recommend appropriate actions like investigating shipping delays and offering replacement or refund.

## Case 5: Normal case

**Input:**
"I was charged twice for my order"

**What a good output should do:**
- Identify the issue as duplicate billing.
- Note the customer's concern about being overcharged.
- Suggest escalation to billing for refund processing and account verification.
