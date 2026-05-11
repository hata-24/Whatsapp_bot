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

## ✨ Features
 
- **Webhook-triggered** — responds to incoming WhatsApp messages in real time
- **AI intent detection** — uses Google Gemini to understand natural language queries
- **ML fallback** — a local scikit-learn model (`app.py`) classifies intent and product with confidence thresholds
- **Dynamic product catalog** — reads product names and prices live from Google Sheets
- **Stateful conversations** — tracks each user's position in the menu flow
- **Duplicate message guard** — prevents double-processing the same message
- **Supports both menu-based and free-text input**


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
<img width="463" height="360" alt="image" src="https://github.com/user-attachments/assets/bd0f559b-7438-4110-8d80-ffa22adc4c6b" />

---

### 2. Product Catalog Sheet (`Catalog`)
<img width="664" height="348" alt="image" src="https://github.com/user-attachments/assets/1b32ecde-02b8-4f39-a308-e72036654904" />

---


## 🔁 State Flow

* `menu` → initial state
* `awaiting_option` → waiting for user choice
* `awaiting_product` → waiting for product query

---

## 🚀 Getting Started
 
### Prerequisites
 
- [n8n](https://docs.n8n.io/hosting/) instance (self-hosted or cloud)
- Meta Developer account with a WhatsApp Business app
- Google Cloud project with Sheets API and Gemini API enabled
- Python 3.9+
### 1. Clone the repository
 
```bash
git clone https://github.com/hata-24/Whatsapp_bot.git
cd Whatsapp_bot
```
 
### 2. Set up the Python ML server
 
```bash
pip install fastapi uvicorn scikit-learn joblib
 
# (Optional) Retrain the models on your own data
python intent_model.py
 
# Start the API server
uvicorn app:app --host 0.0.0.0 --port 8000
```
 
The server exposes a single endpoint:
 
```
POST /predict
Body: { "text": "<user message>" }
Returns: { "intent": "...", "product": "..." }
```
 
Confidence threshold is set to `0.20` — anything below is classified as `"other"` / `"Default"`.
 
### 3. Set up Google Sheets
 
Create a spreadsheet with two tabs:
 
**`User_state`**
 <img width="463" height="360" alt="image" src="https://github.com/user-attachments/assets/bd0f559b-7438-4110-8d80-ffa22adc4c6b" />

 
**`Catalog`**
 <img width="664" height="348" alt="image" src="https://github.com/user-attachments/assets/1b32ecde-02b8-4f39-a308-e72036654904" />

 
### 4. Import the n8n workflow
 
1. Open your n8n instance.
2. Go to **Workflows → Import from file**.
3. Upload `whatsapp-chatbot-n8n-workflow.json`.
4. Add your credentials for:
   - WhatsApp Cloud API (Meta access token + phone number ID)
   - Google Sheets (OAuth2 or service account)
   - Google Gemini (API key)
5. Update the Google Sheets node to point to your spreadsheet ID.
6. Activate the workflow.
### 5. Configure the WhatsApp webhook
 
In your Meta Developer dashboard, set the webhook URL to your n8n webhook endpoint and subscribe to the `messages` field.
 
---



