# Rasa IKT Bot 🤖

This is a **Rasa-based chatbot** developed as a final project for the **Department of Information and Communication Technologies** at the **University of Applied Sciences of Rijeka**.

---

##  About the Bot

The bot offers basic information about the study program, including:

- How the program is organized  
- Key benefits and challenges of the curriculum  
- Explanations of academic terms such as **ECTS**, **semester**, **course**, etc.

It also supports **custom actions** to provide:

- Descriptions of specific courses  
- Information about who teaches each course  
- Contact details and information about professors  

---

## 🛠 Technologies Used

- Built with the **Rasa framework**
- Developed using **PyCharm IDE**
- Integrated with a simple **HTML/JavaScript** frontend resembling a chat interface

---

##  How to Run the Project

Open **two terminal windows** in the project directory:

### 1. Start the Rasa server:

```bash
rasa run --enable-api --cors "*" --debug
```

### 2. Start the custom actions server:

```bash
rasa run actions
```

### 3. Launch the chatbot interface:

Open `index.html` in your browser to begin the conversation.

---

##  Features

- Clickable links in responses  
- Scrollable chat interface  
- Send messages via **Enter** key or mouse click  
- Simple and responsive local chatbot interface  

---

##  License

This project was created for **educational and demonstration purposes** as part of a final thesis.

--- 

##  Author

**Denis Subašić** – student  
Department of Information and Communication Technologies  
University of Applied Sciences of Rijeka  
[GitHub Profile](https://github.com/deniro1221)

##  Supervisor

**Ivan Šimac** – profesor  
Department of Information and Communication Technologies  
University of Applied Sciences of Rijeka