import streamlit as st
from mongoconnection import MongoDBConncetor as mng
import params as p

host = p.MEHDI_IP
port =p.MEHDI_P
db = "Games"
search_cats = ["Titre","Langues","Date de parution","Mode","Prix €","Studio", "Plate-formes", "Genre","DLC","Avis general"]
page_logo = "https://cdn.game.net/image/upload/dpr_auto,f_auto,q_auto/v1/game_img/GAME-logo-230"


if "search_input" not in st.session_state:
    st.session_state['search_input'] = "*"

if "search_cat" not in st.session_state:
    st.session_state['search_cat'] = "*"

if "sort_by" not in st.session_state:
    st.session_state['sort_by'] = "*"

st.markdown(body=f""" <div style = "display: flex;
        justify-content: center;">
            <img src={page_logo} alt="Gmaing store" class="center">
            </div>""", unsafe_allow_html=True)

st.markdown("---")

class GUI:
    def __init__(self) -> None:
        self.search_cats = search_cats
        self.select_cat = st.empty()
        self.sort_by = st.empty()
        self.search_bar = st.empty()
        self.result_container = st.empty()
        self.db_connector = mng(database_name = db , host = host , port= port)
    
    def search(self,store : str, category = None, search_input = None, sort_by = None):
        result = self.db_connector.search_in_collection_for(cllection_name = store , element = category , search_input= search_input, sort_by= sort_by)
        return result
    
    def update_searchbar(self):
        st.session_state['search_input'] = self.search_bar
        
    def update_searchcat(self):
        st.session_state['search_cat'] = self.select_cat
        
    def update_sortby(self):
        st.session_state['sort_by'] = self.sort_by
        
    def display(self):
        self.cat_col , self.sort_col = st.columns(spec=[1,1])
        self.select_cat = self.cat_col.selectbox(label='Select search categories', options=search_cats, on_change=self.update_searchcat())
        self.sort_by = self.sort_col.selectbox(label='Sort by', options=search_cats, on_change=self.update_sortby())
        self.search_bar = st.text_input(label =" Search " , on_change=self.update_searchbar())
    def number_or_not(self,num):
        try:
            float(num)
            return True
        except ValueError:
            return False
    
    def print_infos(self, title : str, image_url :str, studio : str, year : str , genre :str, rating: float, prix :str):
        with st.container(height=400):
            img_col , info_col = st.columns(spec = [1, 2])
            h = title
            h = h.replace(":", "_")
            
            gen = ", ".join(genre)
            img_col.markdown(body=f""" 
                            <img src="{image_url}" alt="{h}" 
                            style="width:100;height:200px;"
                            /> 
                            """ , unsafe_allow_html=True)
            info_col.title(title)
            info_col.markdown(f"**Studio** : {studio}")
            info_col.markdown(f"**Genre**: {gen}")

            info_col.markdown(f"**Date de parution**: {year}")
            info_col.markdown(f"**Avis géneral**: {rating} ⭐")
            info_col.markdown(f"""**Prix** : <span style="color:#2E8B57">{prix}€</span> """, unsafe_allow_html=True)
            info_col.button(label = "Plus de détails", key=title , on_click=self.get_details(search_input=title, element="Titre"))
            
    def print_moreinfos(self, title : str, image_url :str, studio : str, year : str , genre :str, rating: float, prix :str, plat : str, mode : str, lang: str, dlc : str):
        try:
            if st.session_state[f'{title}'] == True:
                h = mode
                mode = ", ".join(mode)
                lang = ", ".join(lang)
                dlc = ", ".join(dlc)
                plat= ", ".join(plat)
                st.markdown(f"""**Mode** : {mode}""", unsafe_allow_html=True)
                st.markdown(f"""**Langues** : {lang}""", unsafe_allow_html=True)
                st.markdown(f"""**DLC** : {dlc}""", unsafe_allow_html=True)
                st.markdown(f"""**Plates-formes** : {plat}""", unsafe_allow_html=True)
        except:
            pass
            
    def get_details(self,search_input : str , store = "Magasin", element = None , sort_by = None):
        result = self.db_connector.search_in_collection_for(cllection_name = store , element = element , search_input= search_input, sort_by= sort_by)
        for i in result:
            self.print_moreinfos(prix=i["Prix €"],title=i["Titre"], image_url= i["Image"], genre=i["Genre"], studio=i["Studio"], 
                                 year = i["Date de parution"], rating= i["Avis general"], mode = i["Mode"], lang=i["Langues"], plat = i["Plates-formes"], dlc = i["DLC"])
    
    def default_results(self):
        default_res = self.search(store = "Magasin", category = None, search_input = None, sort_by = None)
        for i in default_res:
                self.print_infos(title=i["Titre"], image_url= i["Image"], genre=i["Genre"], studio=i["Studio"], year = i["Date de parution"], rating= i["Avis general"])

    def launch(self):
        f = st.session_state['search_input']
        self.display()
        if f == "*":
            self.default_results()

        if self.search_bar != "" and st.session_state['search_cat'] is not None and st.session_state['search_input'] is not None and st.session_state['sort_by'] is not None:
            send = self.search_bar
            if self.number_or_not(send):
                send = float(send)
            result = self.search(store = "Magasin", category = self.select_cat, search_input = send, sort_by= self.sort_by) 
            for i in result:
                self.print_infos(prix=i["Prix €"],title=i["Titre"], image_url= i["Image"], genre=i["Genre"], studio=i["Studio"], year = i["Date de parution"], rating= i["Avis general"])
    
if __name__ == "__main__":
    g = GUI()
    g.launch()