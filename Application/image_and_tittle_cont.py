import streamlit as st


h = st.container(height= 200)

with h:
    img_col , info_col = st.columns(spec = [1, 2])
    img_col.markdown(body=""" 
                     <img src="https://cdn.cdkeys.com/700x700/media/catalog/product/f/i/fifa-22-pc-game-origin-cover_92_.jpg" alt="Dinosaur" 
                     style="width:100;height:200px;"
                     />" 
                     """ , unsafe_allow_html=True)
    info_col.title("Noita")
    info_col.text("Gnere : Aventure")
    info_col.text("Annee : 2019")