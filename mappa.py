import requests
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
from PIL import Image
#LOCO

st.set_page_config(page_title="Mappa To Watch", page_icon=':smiley:', layout="wide")

#Function For GIF
def loader(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#LOAD ASSET
lotte_felix = loader("https://lottie.host/8a46c615-f671-4c99-9fa6-60e1335947f7/7TUlAYQPib.json")
lott_news = loader("https://lottie.host/e128a3da-a1fb-4162-9f47-508223f805c7/wU1bBHPHZs.json")


#SIDE BAR
selected = option_menu(
    menu_title=None,
    options=["Home", "Popular"],
    icons=["house", "book"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
)

if selected == "Home":
#HEADER SECTION
    with st.container():
        left_column, right_column = st.columns(2)
        st.subheader("Welcome Mappa's Fan")
        st.title("This Website will help you find your favorite Mappa's anime")
        st.write("Hope you guys enjoy")
        st.write("Thanks you :D")

#ANOTHER SECTION
    with st.container():
        st.write("---")
        left_column , right_column = st.columns(2)
        with left_column:
            st.title("Get Start")
            st.write("LET\'S GOOOOO!!!!!")
            genre_input = st.multiselect("Genre", ["Drama", "Action", "Adventure", "Fantasy", "Sci-fi", "Horror", "Shounen", "Shoujo"])
            if genre_input:
                st.success('We have acknowledged your preference!!', icon="✅")
                st.write("Your Preference are :", genre_input)

        with right_column:
            st_lottie(lotte_felix, height=550, key="Felix")

if selected == "Popular":
        st.subheader("Here's Mappa's Top Anime")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.header("HOT!!")
            st.image("https://images.cinemaexpress.com/uploads/user/ckeditor_images/article/2022/9/20/jujutsu_kaisen.jpg", width=550)

        with col2:
            st.header("Recommended!!")
            st.image("https://m.media-amazon.com/images/M/MV5BMTMwNmQyM2EtMDQ2My00Y2FhLWJlYTYtMDMwYWU4MzAwYmI3XkEyXkFqcGdeQXVyMTQ3MjMyMTYz._V1_.jpg", width=550)

        with col3:
            st.header("Masterpiece!!!")
            st.image("https://flxt.tmsimg.com/assets/p10701949_b_v9_ah.jpg", width=550)

        st.subheader("Can now watch in Netflix or Billibilli")
