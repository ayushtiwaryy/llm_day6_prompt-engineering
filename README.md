# Day 6 - Prompt Engineering: Building a Prompt for Complaint Classification

## 📌 Overview

Today, I learned how to design a structured prompt to classify customer complaints into predefined categories using Prompt Engineering.

The prompt follows the **Anatomy of a Prompt** by clearly defining the AI's **Role**, **Task**, **Constraints**, **Output Format**, **Example**, and **Fallback** behavior. This structure helps the model generate accurate and consistent responses.

---

## 🎯 Objective

Build an AI prompt that classifies customer complaints into one of the following categories:

* **BILLING**
* **TECHNICAL**
* **RETURN**
* **OTHER** (fallback for unrelated issues)

---

# 🧠 Prompt Components

## 1️⃣ Role

Defines the identity of the AI.

```text
You are a support assistant at a mobile/laptop service center.
```

The AI behaves like a customer support representative.

---

## 2️⃣ Task

Defines what the AI should accomplish.

```text
You have to classify the issue into a category.
```

The AI reads the user's complaint and determines the most appropriate category.

---

## 3️⃣ Constraints

Restricts the possible outputs.

```text
BILLING
TECHNICAL
RETURN
```

The AI must choose only one of these categories whenever applicable.

---

## 4️⃣ Output Format

Defines how the response should look.

```text
Give output in one word only.
```

Example outputs:

```text
TECHNICAL
```

```text
RETURN
```

```text
BILLING
```

This ensures consistent responses that are easy to process programmatically.

---

## 5️⃣ Example

Provides the model with an example to establish the expected behavior.

```text
Complaint:
I want a refund.

Output:
RETURN
```

Examples improve consistency and help the model understand the desired mapping.

---

## 6️⃣ Fallback

Handles cases outside the predefined categories.

```text
If the issue does not belong to any category,
return:

OTHER
```

This prevents incorrect classifications for unrelated complaints.

---

# 📝 Sample Prompt

```python
prompt = """
# ROLE
You are a support assistant at a mobile/laptop service center.

# TASK
Classify the user's complaint into a category.

# CONSTRAINT
Allowed categories:
- BILLING
- TECHNICAL
- RETURN

# OUTPUT FORMAT
Return only one word from the allowed categories.

# EXAMPLE
Complaint:
I want a refund.

Output:
RETURN

# FALLBACK
If the complaint does not match any category,
return:
OTHER

Complaint:
My phone is not working. I want a refund.
"""
```

---

# 📌 Example Inputs & Outputs

| User Complaint                                      | Category  |
| --------------------------------------------------- | --------- |
| My phone is not turning on.                         | TECHNICAL |
| I was charged twice for my order.                   | BILLING   |
| I received a damaged laptop and want my money back. | RETURN    |
| How can I change my account password?               | OTHER     |

---

# 💡 Key Learnings

* Learned how to assign a **Role** to the AI.
* Defined a clear **Task** for complaint classification.
* Used **Constraints** to restrict valid outputs.
* Specified a fixed **Output Format** for consistency.
* Added an **Example** to guide the model.
* Implemented a **Fallback** response for unsupported cases.
* Understood how structured prompts improve accuracy and reliability.

---

# 🚀 Applications

This prompt design can be used for:

* Customer Support Automation
* Help Desk Ticket Routing
* AI Chatbots
* Complaint Classification Systems
* Email Categorization
* Customer Service Workflows

---

# 🛠️ Technologies Used

* Python
* Prompt Engineering
* Large Language Models (LLMs)

---

# 📖 What I Learned Today

* Designing structured prompts using the Anatomy of a Prompt.
* Using Role, Task, Constraints, Output Format, Examples, and Fallback effectively.
* Creating prompts that produce predictable and machine-friendly outputs.
* Building a simple AI-powered complaint classification system.

---

## 🎯 Outcome

By creating this prompt, I learned how to build a structured classification workflow for customer support. The prompt ensures that responses are accurate, consistent, and limited to predefined categories, making it suitable for automation and integration into AI-powered service desk applications.


