import pymongo
import pprint
import params as p
import pandas as pd


class MongoDBConncetor :
    def __init__(self, database_name : str , host :str , port : str ) -> None:
        self.client = pymongo.MongoClient(f"mongodb://{host}:{port}/")
        self.db_name = self.client[database_name]
        
    def view_collections(self):
        return self.db_name.list_collection_names()
      
    def get_collection_elements(self,cllection_name : str):
      self.collection = self.db_name.cllection_name
      game_list = self.collection.find({},{}).sort("name")
      
      return game_list
    
    def search_in_collection_for(self,cllection_name : str, element = None, search_input = None, sort_by= None):
      self.collection = self.db_name[cllection_name]
      if search_input == "*" :
        search_input= None
        element= None
      liste = []
      
      if element is None and search_input is None and sort_by is None:
        game_list = self.collection.find({},{}).sort("Titre")
        
      elif element is not None and search_input is not None and sort_by is not None:
        game_list = self.collection.find({element: search_input}).sort(sort_by)
        
      elif element is not None and search_input is not None and sort_by is None:
        game_list = game_list = self.collection.find({element: search_input})
      elif element is None and search_input is None and sort_by is not None:
        game_list = self.collection.find({},{}).sort(sort_by)
        
      #print(game_list)
      for i in game_list:
        liste.append(i)
      return liste
if __name__ == "__main__":
    connector = MongoDBConncetor(database_name = "Games" , host = p.MEHDI_IP , port= p.MEHDI_P)
    pprint.pprint(connector.view_collections())
    pprint.pprint(connector.search_in_collection_for(cllection_name = "Magasin", search_input='Noita', element='Titre'))