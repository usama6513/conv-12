import streamlit as st  
import pandas as pd  
import json  
import os  
from datetime import datetime  
import time  
import requests  
import plotly.express as px  
import plotly.graph_objects as go  
from streamlit_lottie import st_lottie  
  
st.set_page_config(  
     page_title="📚Personal Library Management System📚",  
     page_icon="💖",  
     layout="wide",  
     initial_sidebar_state="expanded"  
)  
    
def save_library():  
    try:  
         with open("library.json", "w") as file:  
            json.dump(st.session_state.library, file, indent=4)  
    except Exception as e:  
         st.error(f"Error saving library: {e}")  
  
def load_library():  
    try:  
        if os.path.exists("library.json"):  
            with open("library.json", "r") as file:  
                  st.session_state.library = json.load(file)  
                  return True  
        else:  
            return False  
    except Exception as e:  
         st.error(f"Error Loading library: {e}")  
         return False  
  
if "library" not in st.session_state:  
    st.session_state.library = []  
   
if "current_view" not in st.session_state:  
    st.session_state.current_view = "Library"  
   
def add_book(title, author, publication_year, genre, read_status):  
    book = {  
         'title': title,  
                           'author': author,  
       'publication_year': publication_year,  
                         'genre': genre,  
        'read_status': read_status,  
        'added_date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")  
     }  
st.session_state.library.append("book")  
save_library()  
st.success("Book added successfully!")  
   
def remove_book(index):  
    if 0 <= index < len(st.session_state.library):  
        del st.session_state.library[index]  
        save_library()  
        st.success("Book removed successfully!")  
  
def search_books(search_term, search_by):  
    search_term = search_term.lower()  
    results = [book for book in st.session_state.library if search_term in book[search_by].lower()]  
    return results  
  
st.sidebar.markdown("<h1 style='text-align: center;'> Navigation</h1>", unsafe_allow_html=True)  
nav_option = st.sidebar.radio("Choose an option:", ["View Library", "Add Book", "Search Book"])  

if nav_option == "View Library":  
    st.session_state.current_view = "Library"  
elif nav_option == "Add Book":  
    st.session_state.current_view = "Add"  
elif nav_option == "Search Book":  
    st.session_state.current_view = "Search"  
   
st.markdown("<h1> Personal Library Manager - Maria </h1>", unsafe_allow_html=True)  
   
if st.session_state.current_view == "Add":  
     with st.form(key='add_book_form'):  
         title = st.text_input("Book Title")  
         author = st.text_input("Author")  
         publication_year = st.number_input("Publication Year", min_value=1000, max_value=datetime.now().year, step=1)  
         genre = st.text_input("Genre")  
         read_status = st.radio("Have you read this book?", ("Yes", "No"))  
         submit_button = st.form_submit_button("Submit")  
     if submit_button:  
         add_book(title, author, publication_year, genre, read_status == "Yes")  
   
elif st.session_state.current_view == "Library":  
     st.write("### Your Library")  
     for index, book in enumerate(st.session_state.library):  
         st.write(f"{book['title']} by {book['author']} ({book['publication_year']}) - {book['genre']} - {'Read' if book['read_status'] else 'Unread'}")  
         if st.button(f"Remove {book['title']}", key=index):  
             remove_book(index)  
   
elif st.session_state.current_view == "Search":  
     search_term = st.text_input("Enter search term")  
     search_by = st.radio("Search by", ["title", "author", "genre"])  
     if st.button("Search"):  
         results = search_books(search_term, search_by)  
         if results:  
             for book in results:  
                 st.write(f"{book['title']} by {book['author']} ({book['publication_year']})")  
         else:  
             st.warning("No matching books found.")  
   
st.markdown("Copyright @ 2025 Maria Personal Library Manager", unsafe_allow_html=True)
