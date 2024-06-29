import pymongo

myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
mydb = myclient["Games"]
magasin = mydb["Magasin"]
magasin.drop()
magasin = mydb["Magasin"]
catalogue = mydb["catalogue"]

mydict = [
        {
            "_id": "1",
            'Titre':'Mario Party Superstars',
            'Image':'https://cdkeyprices.fr/images/games/5638642/mario-party-superstars-desktop-logo-all.jpg',
            'Studio':'Nintendo',
            'Plates-formes':['Nintendo Switch'],
            'Genre':['Party Game','Famille','Multijoueur'],
            'Mode':['Multijoueur'],
            'Avis general':4.7,
            'Prix €':34.99,
            'DLC':[""],
            'Date de parution':'05/10/2021',
            'Langues':['Allemand', 'Néerlandais', 'Anglais', 'Espagnol', 'Français', 'Italien', 'Japonais', 'Coréen', 'Russe']
        },
        {
            "_id": "2",
            'Titre':'Hollow Knight',
            'Image':'https://cdn-products.eneba.com/resized-products/q7i-msiKJw8A73IeLKtYuwpr0ilw62NWSVQIFD0GbB0_350x200_3x-0.jpeg',
            'Studio':'Team Cherry',
            'Plates-formes':['PC', 'Nintendo Switch', 'PlayStation', 'Xbox'],
            'Genre':['Metroidvania', 'Aventure','Solo'],
            'Mode':['Solo'],
            'Avis general':5,
            'Prix €':14.99,
            'DLC':["Rêves Cachés",'La Troupe Grimm','Sang-de-vie','Chercheur de Dieux'],
            'Date de parution':'24/02/2017',
            'Langues':['Anglais', 'Français', 'Allemand', 'Espagnol', 'Coréen', 'Chinois simplifié', 'Italien', 'Portugais', 'Russe', 'Japonais']
        },
        {
            "_id": "3",
            'Titre':'It Takes Two',
            'Image':'https://cdn1.epicgames.com/offer/8ae7b3c0f490471b967ce26cc2f6e0e6/EGS_ItTakesTwo_Hazelight_S2_1200x1600-5c82de2d2e21a841dd06ec27e082777e_1200x1600-5c82de2d2e21a841dd06ec27e082777e',
            'Studio':'Hazelight Studios',
            'Plates-formes':['PC', 'Nintendo Switch', 'PlayStation', 'Xbox'],
            'Genre':['Plates-formes', 'Réflexion', 'Action','Aventure'],
            'Mode':['Coopération'],
            'Avis general':5,
            'Prix €':39.99,
            'DLC':[""],
            'Date de parution':'25/03/2021',
            'Langues':['Anglais', 'Français', 'Allemand', 'Espagnol', 'Coréen', 'Chinois simplifié', 'Italien', 'Portugais', 'Russe', 'Japonais'] 
        },
        {
            "_id": "4",
            'Titre':'Noita',
            'Image':'https://cdn.cdkeys.com/700x700/media/catalog/product/f/i/fifa-22-pc-game-origin-cover_92_.jpg',
            'Studio':'Nolla Games',
            'Plates-formes':['PC'],
            'Genre':['Action','Aventure','Roguelite','Solo'],
            'Mode':['Solo'],
            'Avis general':5,
            'Prix €':19.99,
            'DLC':[""],
            'Date de parution':'24/09/2019',
            'Langues':['Anglais', 'Français', 'Allemand', 'Espagnol', 'Coréen', 'Chinois simplifié', 'Italien', 'Portugais', 'Russe', 'Japonais']
        },
        {
            "_id": "5",
            'Titre':'Brawl Stars',
            'Image':'https://www.shutterstock.com/image-vector/stars-brawl-wing-vector-600nw-1358889212.jpg',
            'Studio':'Supercell',
            'Plates-formes':['iOS','Android'],
            'Genre':['Arène de bataille','Action'],
            'Mode':['Multijoueur'],
            'Avis general':4.6,
            'Prix €':0.0,
            'DLC':[""],
            'Date de parution':'15/06/2017',
            'Langues':['Anglais', 'Français', 'Allemand', 'Espagnol', 'Coréen', 'Chinois simplifié', 'Italien', 'Portugais', 'Russe', 'Japonais']
        },
        {
            "_id": "6",
            'Titre':"Cyberpunk 2077",
            'Image':'https://upload.wikimedia.org/wikipedia/en/thumb/9/9f/Cyberpunk_2077_box_art.jpg/220px-Cyberpunk_2077_box_art.jpg',
            'Studio':'CD Projekt RED',
            'Plates-formes':['PC', 'PlayStation', 'Xbox'],
            'Genre':['FPS','Action','Aventure'],
            'Mode':['Solo'],
            'Avis general':4.5,
            'Prix €':29.99,
            'DLC':["Phantom liberty"],
            'Date de parution':'10/12/2020',
            'Langues':['Anglais', 'Français', 'Allemand', 'Espagnol', 'Coréen', 'Chinois simplifié', 'Italien', 'Portugais', 'Russe', 'Japonais']
        },
        {
            "_id": "7",
            'Titre':'The Binding of Isaac: Rebirth',
            'Image':'https://upload.wikimedia.org/wikipedia/en/thumb/e/e1/The_Binding_of_Issac_Rebirth_cover.jpg/220px-The_Binding_of_Issac_Rebirth_cover.jpg',
            'Studio':'Edmund McMillen',
            'Plates-formes':['PC'],
            'Genre':['Roguelike'],
            'Mode':['Solo'],
            'Avis general':4.9,
            'Prix €':14.99,
            'DLC':["Afterbirth",'Afterbirth+','Repentance'],
            'Date de parution':'04/11/2014',
            'Langues':['Anglais']
        },
        {
            "_id": "8",
            'Titre':'Elden ring',
            'Image':'https://www.fredzone.org/wp-content/uploads/2022/03/Elden-Ring-jaquette-1000x1000.jpg',
            'Studio':'FromSoftware',
            'Plates-formes':['PC','PlayStation','Xbox'],
            'Genre':['Action-RPG'],
            'Mode':['Solo','Multijoueur'],
            'Avis general':4.9,
            'Prix €':59.99,
            'DLC':[""],
            'Date de parution':'25/02/2022',
            'Langues':['Anglais', 'Français', 'Allemand', 'Espagnol', 'Coréen', 'Chinois simplifié', 'Italien', 'Portugais', 'Russe', 'Japonais']
        },
        {
            "_id": "9",
            'Titre':'Hades',
            'Image':'https://cdn1.epicgames.com/min/offer/1200x1600-1200x1600-e92fa6b99bb20c9edee19c361b8853b9.jpg',
            'Studio':'Supergiant Games',
            'Plates-formes':['PC','PlayStation','Xbox','Nintendo Switch'],
            'Genre':['Roguelike'],
            'Mode':['Solo'],
            'Avis general':4.9,
            'Prix €':24.99,
            'DLC':[""],
            'Date de parution':'06/12/2018',
            'Langues':['Anglais', 'Français', 'Allemand', 'Espagnol', 'Coréen', 'Chinois simplifié', 'Italien', 'Portugais', 'Russe', 'Japonais']
        },
        {
            "_id": "10",
            'Titre':'Sekiro: Shadows Die Twice',
            'Image':'https://upload.wikimedia.org/wikipedia/en/thumb/6/6e/Sekiro_art.jpg/220px-Sekiro_art.jpg',
            'Studio':'FromSoftware',
            'Plates-formes':['PC','PlayStation','Xbox'],
            'Genre':['Action-RPG'],
            'Mode':['Solo'],
            'Avis general':4.9,
            'Prix €':59.99,
            'DLC':[""],
            'Date de parution':'22/03/2019',
            'Langues':['Anglais', 'Français', 'Allemand', 'Espagnol', 'Coréen', 'Chinois simplifié', 'Italien', 'Portugais', 'Russe', 'Japonais']
        },
        {
            "_id": "11",
            'Titre':'Lethal Company',
            'Image':'https://www.goclecd.fr/wp-content/uploads/lethal-company.jpg',
            'Studio':'Zeekerss',
            'Plates-formes':['PC','PlayStation','Xbox'],
            'Genre':['Horreur','Aventure'],
            'Mode':['Solo', 'Multijoueur'],
            'Avis general':5,
            'Prix €':9.75,
            'DLC':[""],
            'Date de parution':'09/10/2023',
            'Langues':['Anglais']
        },
        {
            "_id": "12",
            'Titre':'Overcooked',
            'Image':'https://cdn.cdkeys.com/700x700/media/catalog/product/o/v/overcooked-pc-get-cheap-cd-key_7_.jpg',
            'Studio':'Ghost Town Games',
            'Plates-formes':['PC','PlayStation','Xbox','Nintendo Switch'],
            'Genre':['Simulation'],
            'Mode':['Multijoueur'],
            'Avis general':4.5,
            'Prix €':16.99,
            'DLC':[""],
            'Date de parution':'02/08/2016',
            'Langues':['Anglais', 'Français', 'Allemand', 'Espagnol', 'Coréen', 'Chinois simplifié', 'Italien', 'Portugais', 'Russe', 'Japonais']
        },
        {
            "_id": "13",
            'Titre':'We Were Here',
            'Image':'https://image.api.playstation.com/vulcan/ap/rnd/202008/3107/Yq4l4Iahas3v9ESc6m1nzZ4U.png',
            'Studio':'Total Mayhem Games',
            'Plates-formes':['PC','PlayStation','Xbox','Nintendo Switch'],
            'Genre':['Adventure','Réflexion'],
            'Mode':['Coopération'],
            'Avis general':4.8,
            'Prix €':0.0,
            'DLC':[""],
            'Date de parution':'03/02/2017',
            'Langues':['Anglais']
        },
        {
            "_id": "14",
            'Titre':'The Witcher 3: Wild Hunt',
            'Image':'https://calimacil.com/cdn/shop/files/Geralt-calimacil-larp-replica-banner-mobile.jpg?v=1695734545&width=1500',
            'Studio':'CD Projekt RED',
            'Plates-formes':['PC','PlayStation','Xbox','Nintendo Switch'],
            'Genre':['Adventure','Action-RPG'],
            'Mode':['Solo'],
            'Avis general':4.8,
            'Prix €':19.99,
            'DLC':["Blood and Wine","Hearts of Stone"],
            'Date de parution':'18/05/2015',
            'Langues':['Anglais', 'Français', 'Allemand', 'Espagnol', 'Coréen', 'Chinois simplifié', 'Italien', 'Portugais', 'Russe', 'Japonais']
        },
        {
            "_id": "15",
            'Titre':'Dark and Darker',
            'Image':'https://sm.ign.com/ign_fr/cover/d/dark-and-d/dark-and-darker_zfjz.jpg',
            'Studio':'IRONMACE',
            'Plates-formes':['PC'],
            'Genre':['Adventure','Action-RPG','Dungeon crawler','FPS'],
            'Mode':['Multijoueur'],
            'Avis general':4.4,
            'Prix €':34.99,
            'DLC':[""],
            'Date de parution':'07/08/2023',
            'Langues':['Anglais']
        }
]

magasin.insert_many(mydict)
x = magasin.find()
for doc in x:
    print(doc)
