# 🔐 Apply Filters to SQL Queries (Security Analysis)

## 📌 Project Description
This project focuses on using SQL filtering techniques to investigate potential security issues and retrieve specific employee and login data. The analysis simulates real-world tasks such as detecting suspicious login activity and identifying employees requiring system updates.

---

## 🔍 Retrieve after hours failed login attempts

A potential security incident occurred after business hours (after 18:00), so failed login attempts during this period needed to be investigated.

```sql
SELECT * 
FROM log_in_attempts 
WHERE login_time > '18:00' AND success = FALSE;
```



