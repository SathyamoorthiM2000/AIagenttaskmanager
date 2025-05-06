AI-Based Task Management Agent

This project is an intelligent task management system that understands tasks written in natural language.  
It extracts time and place from user input and stores them in a PostgreSQL database.  
The system uses spaCy NLP for information extraction and FastAPI for backend APIs.  
A Streamlit frontend provides a user-friendly interface for task creation and viewing.  

Setup Instructions

1. Clone the repo and run  --- pip install -r requirements.txt
2. Agent activate --- venvagent\Scripts\activate
3. Start backend: --- uvicorn main:app --reload 
4. Run frontend: --- streamlit run streamlit_app.py 

Video link --- [ https://vimeo.com/1081729827/fcee4987c1?share=copy ]
