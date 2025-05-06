import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/tasks/"

st.title("Task Manager")

title = st.text_input("Task Title")
description = st.text_area("Task Description")

if st.button("Create Task"):
    response = requests.post(API_URL, json={"title": title, "description": description})
    if response.status_code == 200:
        st.success("Task created successfully!")
    else:
        st.error("Error creating task!")

st.subheader("Task List")
response = requests.get(API_URL)
tasks = response.json()

if tasks:
    for task in tasks:
        st.write(f"Title: {task['title']} - Description: {task['description']}")
        if task.get('place'):
            st.write(f"Place: {task['place']}")
        if task.get('time'):
            st.write(f"Time: {task['time']}")
        delete_button = st.button(f"Delete {task['title']}", key=task['id'])
        if delete_button:
            del_response = requests.delete(f"{API_URL}{task['id']}")
            if del_response.status_code == 200:
                st.success(f"Task {task['title']} deleted successfully!")
            else:
                st.error("Error deleting task.")
else:
    st.write("No tasks available.")
