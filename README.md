# 🎓 Online Examination System (OES)

An **Online Examination System** designed to conduct secure, real-time exams with dedicated **Teacher** and **Student** interfaces.  
The platform ensures **exam integrity** through a controlled kiosk environment and structured exam rooms.

---

## ✨ Features

### 👩‍🏫 Teacher Panel
- Dashboard to manage **question papers**
- Create and edit **exams**
- Create **exam rooms**
- Monitor submissions and scores

### 👨‍🎓 Student Panel
- Join exams via **exam room**
- Attempt questions within a **scheduled time**
- Auto-submit answers when time expires

### 🔒 Secure Examination Environment
- Runs in **kiosk mode**
- Keyboard shortcuts disabled
- Tab switching and opening new browsers restricted
- Prevents cheating and external navigation

---

## 🖥️ Teacher Dashboard

The teacher dashboard provides a centralized view of all created question papers and exams.

![Teacher Dashboard](https://private-user-images.githubusercontent.com/83212553/531342973-67853d88-8a1c-4e21-912d-842cecb88381.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NjcyODE4NDMsIm5iZiI6MTc2NzI4MTU0MywicGF0aCI6Ii84MzIxMjU1My81MzEzNDI5NzMtNjc4NTNkODgtOGExYy00ZTIxLTkxMmQtODQyY2VjYjg4MzgxLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNjAxMDElMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjYwMTAxVDE1MzIyM1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWM0ZDI4YmQ2ZjBjYTVhMDA3YTYyN2Y5YTZkZGZiM2YzOTljZTc2MWQ2NzFjMDQ0M2Y4M2E1YzBkZTRmYzc3MDUmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.UYs7ndH5Vt6OR-0YV8HZgNM56lAlXbNxxQNcNOiBImY)

---

## 📝 Question Paper Creation

Teachers can create question papers with multiple question types such as:
- Multiple Choice
- Short Answer
- Subjective Questions

![Question Form UI]([./form_ui.png](https://private-user-images.githubusercontent.com/83212553/531342975-3c406f45-5fc6-485e-9396-b6de4c3f6776.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NjcyODIzMjcsIm5iZiI6MTc2NzI4MjAyNywicGF0aCI6Ii84MzIxMjU1My81MzEzNDI5NzUtM2M0MDZmNDUtNWZjNi00ODVlLTkzOTYtYjZkZTRjM2Y2Nzc2LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNjAxMDElMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjYwMTAxVDE1NDAyN1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTYzYzY4NTBmYjcxMDdiYzEwYTg4NmUyZGIzYzRhZDkwYjQ0YmMwMGM4ZDIxNWY1ZWE2ZjM0ZTc4OGIyMGUwYTMmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.AZvCrXc6TY5zXzSDg2L6hfWfXvs6sd-33BNtPn4deus))

---

## 🏫 Exam Room

Students join a dedicated **exam hall** where:
- Cameras can be monitored
- Exams are conducted in a controlled environment
- Submissions are tracked in real time

![Exam Hall]([./hall.png](https://private-user-images.githubusercontent.com/83212553/531342974-77fdca1d-badd-4bae-bd71-65ca5d5f69f7.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NjcyODIzMjcsIm5iZiI6MTc2NzI4MjAyNywicGF0aCI6Ii84MzIxMjU1My81MzEzNDI5NzQtNzdmZGNhMWQtYmFkZC00YmFlLWJkNzEtNjVjYTVkNWY2OWY3LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNjAxMDElMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjYwMTAxVDE1NDAyN1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWM3ZDFlMjBkZmVkYjk1MTM3NzZhNTVmODdhYzkwY2M2NTQ2MWEwOGVjN2RiMTJhYzhmMTdhZGY5YjNlNjEzMTUmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.52ml73hrgafTA5LLRuo9xoRl1o4lRE13mAoSAkAWZfM))

---

## 🧠 How It Works

1. **Teacher**
   - Logs in
   - Creates a question paper
   - Schedules an exam room

2. **Student**
   - Joins the exam room
   - Attempts the exam within the allotted time
   - Answers are auto-submitted

3. **System**
   - Enforces kiosk restrictions
   - Prevents tab switching or browser exit
   - Ensures exam integrity

---

## 🛠️ Tech Stack

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** (Add your backend here – e.g., Node.js, Django, etc.)
- **Database:** (Add DB – e.g., MySQL, PostgreSQL)
- **Real-Time / Proctoring:** WebRTC / Media APIs
- **Security:** Kiosk Mode, Keyboard & Tab Restrictions

---

## 🚀 Future Enhancements

- AI-based cheating detection
- Detailed analytics for teachers
- Question bank with difficulty levels
- Auto-grading for subjective answers
- Mobile-friendly student view

---

## 📌 Project Status

🟢 Actively Developed / Academic Project

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!  
Feel free to fork the repository and submit a pull request.

---

## 📄 License

This project is licensed under the **MIT License**.

---

### ⭐ If you like this project, don’t forget to give it a star!
