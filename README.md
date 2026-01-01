# Online Examination System (OES)

The **Online Examination System (OES)** is a web-based platform designed to conduct secure, real-time examinations with separate interfaces for **Teachers** and **Students**.  
The system focuses on maintaining exam integrity through a controlled kiosk environment and structured exam rooms.

---

## Features

### Teacher Panel
- Dashboard to manage question papers
- Create and edit examinations
- Create and manage exam rooms
- Monitor student submissions and scores

### Student Panel
- Join examinations via an exam room
- Attempt questions within a scheduled time window
- Automatic submission when the exam time expires

### Secure Examination Environment
- Runs in kiosk mode
- Keyboard shortcuts are disabled
- Switching tabs or opening new browser windows is restricted
- Prevents unauthorized navigation during examinations

---

## Teacher Dashboard

The teacher dashboard provides a centralized view of all created question papers and examinations, allowing efficient exam management.

![Teacher Dashboard](https://private-user-images.githubusercontent.com/83212553/531342973-67853d88-8a1c-4e21-912d-842cecb88381.png)

---

## Question Paper Creation

Teachers can create question papers consisting of multiple question types, including:
- Multiple Choice Questions
- Short Answer Questions
- Subjective Questions

![Question Form UI](https://private-user-images.githubusercontent.com/83212553/531342975-3c406f45-5fc6-485e-9396-b6de4c3f6776.png)

---

## Exam Room

Students participate in examinations through a dedicated exam hall where:
- Cameras can be monitored
- Exams are conducted in a controlled environment
- Submissions are tracked in real time

![Exam Hall](https://private-user-images.githubusercontent.com/83212553/531342974-77fdca1d-badd-4bae-bd71-65ca5d5f69f7.png)

---

## System Workflow

1. **Teacher**
   - Logs into the system
   - Creates a question paper
   - Schedules an exam room

2. **Student**
   - Joins the assigned exam room
   - Attempts the examination within the allotted time
   - Responses are automatically submitted upon completion or timeout

3. **System**
   - Enforces kiosk restrictions
   - Prevents tab switching or browser exit
   - Ensures examination integrity

---

## Technology Stack

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** (Specify backend technology, e.g., Node.js, Django)
- **Database:** (Specify database, e.g., MySQL, PostgreSQL)
- **Real-Time / Proctoring:** WebRTC / Media APIs
- **Security:** Kiosk mode, keyboard and browser restrictions

---

## Future Enhancements

- AI-based cheating detection
- Advanced analytics for teachers
- Question bank with difficulty classification
- Automated grading for subjective answers
- Mobile-compatible student interface

---

## Project Status

This project was developed as an **academic project** and is currently under active development.

---

## Contributing

Contributions, issues, and feature requests are welcome.  
Please fork the repository and submit a pull request for any improvements.

---

## License

This project is licensed under the **MIT License**.
