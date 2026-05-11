# 📱 WhatsApp Chatbot (n8n Workflow)
An intelligent WhatsApp chatbot that combines a **Python/FastAPI ML backend** with an **n8n automation workflow** to handle customer queries automatically — powered by Google Gemini AI and backed by Google Sheets as a lightweight database.

## What the workflow looks like
<img width="1790" height="642" alt="image" src="https://github.com/user-attachments/assets/054be059-657a-4ce7-a641-e8b9609846c6" />

## 🛠️ Tech Stack
 
| Layer | Technology |
|---|---|
| Workflow automation | [n8n](https://n8n.io/) |
| Messaging API | WhatsApp Cloud API (Meta) |
| AI / NLP | Google Gemini |
| ML backend | Python · FastAPI · scikit-learn |
| Database | Google Sheets |

---

## 🚀 Features

* Receive WhatsApp messages via webhook
* AI-powered intent detection using Google Gemini
* View product catalog from Google Sheets
* Query product prices dynamically
* Provide support contact details
* Share business hours
* Maintain user state (menu navigation)
* Handles both menu-based and natural language input

---

## 🧠 How It Works

1. **Incoming Message**

   * Triggered via WhatsApp webhook
   * Extracts user number and message

2. **Duplicate Check**

   * Prevents processing the same message multiple times

3. **User State Management**

   * Retrieves user state from Google Sheets
   * Determines if user is new or returning

4. **Intent Detection (AI)**

   * Uses Google Gemini to classify:

     * `view_products`
     * `product_query`
     * `contact_request`
     * `business_hours`
     * `menu`

5. **Routing Logic**

   * Based on intent and state, routes to:

     * Product listing
     * Price lookup
     * Support info
     * Business hours
     * Menu

6. **Response Generation**

   * Builds an appropriate reply message

7. **Send Response**

   * Sends reply via WhatsApp Cloud API

8. **Update State**

   * Saves user state back to Google Sheets

---

## 🗂️ Google Sheets Structure

### 1. User State Sheet (`User_state`)

| User         | State |
| ------------ | ----- |
| XXXXXXXXXXXX | menu  |

---

### 2. Product Catalog Sheet (`Catalog`)

| A (Product Name) | B (Price) |
| ---------------- | --------- |
| Headphones       | 50        |
| Keyboard         | 80        |

---


## 🔁 State Flow

* `menu` → initial state
* `awaiting_option` → waiting for user choice
* `awaiting_product` → waiting for product query

---


