import streamlit as st
import requests
import os

# Get the base URL from environment variable
API_BASE_URL = os.getenv("API_BASE_URL", "http://localhost:8000")


# Streamlit frontend
def main():
    st.title("Ghost Blogger")

    menu_options = ["Add Post", "Read Post", "Read All Posts", "Update Post", "Delete Post", "Search Post"]
    selected_option = st.sidebar.selectbox("Menu", menu_options)

    if selected_option == "Add Post":
        st.subheader("Add Post")
        title = st.text_input("Title")
        content = st.text_area("Content")
        author = st.text_input("Author")
        if st.button("Submit"):
            post = {"title": title, "content": content, "author": author}
            response = requests.post(f"{API_BASE_URL}/add_post", json=post)
            if response.status_code == 200:
                st.success(response.json()["message"])
            else:
                st.error("Failed to add post")

    elif selected_option == "Read Post":
        st.subheader("Read Post")
        title = st.text_input("Title")
        if st.button("Read"):
            response = requests.get(f"{API_BASE_URL}/read_post/{title}")
            if response.status_code == 200:
                post = response.json()
                if "message" in post:
                    st.error(post["message"])
                else:
                    st.write(post)
            else:
                st.error("Failed to read post")

    elif selected_option == "Read All Posts":
        st.subheader("Read All Posts")
        response = requests.get(f"{API_BASE_URL}/read_all_posts")
        if response.status_code == 200:
            posts = response.json()
            for post in posts:
                st.write(post)
        else:
            st.error("Failed to read all posts")

    elif selected_option == "Update Post":
        st.subheader("Update Post")
        title = st.text_input("Title")
        content = st.text_area("Content")
        author = st.text_input("Author")
        if st.button("Update"):
            post = {"title": title, "content": content, "author": author}
            response = requests.put(f"{API_BASE_URL}/update_post/{title}", json=post)
            if response.status_code == 200:
                st.success(response.json()["message"])
            else:
                st.error("Failed to update post")

    elif selected_option == "Delete Post":
        st.subheader("Delete Post")
        title = st.text_input("Title")
        if st.button("Delete"):
            response = requests.delete(f"{API_BASE_URL}/delete_post/{title}")
            if response.status_code == 200:
                st.success(response.json()["message"])
            else:
                st.error("Failed to delete post")

    elif selected_option == "Search Post":
        st.subheader("Search Post")
        query = st.text_input("Search Query")
        if st.button("Search"):
            response = requests.get(f"{API_BASE_URL}/search_post?query={query}")
            if response.status_code == 200:
                posts = response.json()
                for post in posts:
                    st.write(post)
            else:
                st.error("Failed to search posts")

if __name__ == "__main__":
    main()
