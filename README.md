# Order Management System with Google OAuth2 and DRF

## 🚀 Overview

This is a Django Rest Framework-based backend template for an Order Management System.

### ✅ Features:
- Google OAuth 2.0 Integration (manual via Postman)
- Add and Retrieve Sample Entries
- API endpoints secured via DRF permissions
- Supports filtering entries by title

---

## 🔐 Google OAuth 2.0 Setup (Manual via Postman)

1. Visit Google Cloud Console: https://console.cloud.google.com/
2. Create a new project & OAuth 2.0 client credentials.
3. Add redirect URI like: `http://localhost:8000/oauth/callback/`
4. Exchange code for:
   - `access_token`
   - `refresh_token`
5. Use access token in Postman to access protected APIs.

---

## 📦 Endpoints

### Add Entry
- **POST** `/api/add/`
- **Headers:** `Authorization: Bearer <access_token>`
- **Body:**
```json
{
  "title": "Sample Order",
  "description": "Details about the sample"
}
```

### Fetch Entries
- **GET** `/api/fetch/?title=Sample`
- Returns only entries for the authenticated user.

---

## 🛠️ How to Run

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser  # optional
python manage.py runserver
```

---

## 🔒 Security Notes
- DO NOT expose your Google client secrets.
- Use HTTPS in production.

---

Developed as a backend template for Ywork.ai intern assignment.
