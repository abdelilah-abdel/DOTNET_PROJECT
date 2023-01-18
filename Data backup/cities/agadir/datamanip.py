import pandas as pd
import os
import glob

import re
import os
import  csv

'''
dir_path = '/home/abdel/Documents/DOTNET_Project/Data backup/DataRepo'
new_path = '/home/abdel/Documents/DOTNET_Project/Data backup/DataRepo/new'

csv_files= [ 'Iberostar_Founty_Beach-Agadir.csv', 'LABRANDA_Les_Dunes_d_Or-Agadir.csv', 'White_Beach_Resort_Taghazout-Tamraght_Agadir.csv', 'Atlantic_Hostel-Essaouira.csv', 'halassa_sea_spa_MGallery-Essaouira.csv', 'Hotel_Riad_Benatar-Essaouira.csv', 'L_Heure_Bleue_Palais-Essaouira.csv', 'Lodge-Essaouira.csv', 'Riad_Chbanate-Essaouira.csv', 'Riad_Le_Grand_Large-Essaouira.csv', 'Sofitel_Essaouira_Mogador_Golf_Spa-Essaouira.csv', 'Dar_7_Louyat-Fes_Fes_Meknes.csv', 'Dar_El_Mandar_Farm-Fes_Fes_Meknes.csv', 'Dar_Hafsa-Fes_Fes_Meknes.csv', 'Fes_Marriott_Hotel_Jnan_Palace-Fes_Fes_Meknes.csv', 'Hostel_Medina_Social_Club-Fes_Fes_Meknes.csv', 'Hotel_Spa_Riad_Dar_Bensouda-Fes_Fes_Meknes.csv', 'Ibis_budget_Fes-Fes_Fes_Meknes.csv', 'Palais_Faraj_Suites_Spa-Fes_Fes_Meknes.csv', 'Riad_Braya-Fes_Fes_Meknes.csv', 'Riad_Fes_Maya_Suite_Spa-Fes_Fes_Meknes.csv', 'Riad_Ibn_Khaldoun-Fes_Fes_Meknes.csv', 'Riad_Laaroussa_Hotel_and_Spa-Fes_Fes_Meknes.csv', 'Riad_Le_Calife-Fes_Fes_Meknes.csv', 'Riad_Verus-Fes_Fes_Meknes.csv', 'Riad_Zitouna-Fes_Fes_Meknes.csv', 'Iberostar_Club_Palmeraie-Marrakech.csv', 'La_Maison_Arabe-Marrakech.csv', 'Movenpick_Hotel_Mansour_Eddahbi-Marrakech.csv', 'Sol_Oasis-Marrakech.csv', 'Dar_Daif-Ouarzazate.csv', 'Dar_Panorama-Skoura_Ouarzazate.csv', 'Espace_Kasbah_Amridil-Skoura_Ouarzazate.csv', 'Hotel_marmar-Ouarzazate.csv', 'Le_Berbere_Palace-Ouarzazate.csv', 'L_Ma_Lodge-Skoura_Ouarzazate.csv', 'Maison_d_hotes_Dar_Farhana-Ouarzazate.csv', 'Riad_Ouarzazate-Ouarzazate.csv', 'arriott_Hotel-Rabat.csv', 'Dar_El_Kebira-Rabat.csv', 'Dar_Shaan-Rabat.csv', 'Dar_Zouhour-Rabat.csv', 'Ibis_Rabat-Rabat_Agdal.csv', 'Ibis_Rabat_Agdal-Rabat.csv', 'La_Tour_Hassan_Palace-Rabat.csv', 'Le_Diwan-Rabat_MGallery.csv', 'Le_Pietri_Urban_Hotel-Rabat.csv', 'ONOMO_Hotel-Rabat_Medina.csv', 'Reviews-The_View_Hotel-Rabat.csv', 'Riad_Dar_Soufa-Rabat.csv', 'Riad_Kalaa-Rabat.csv', 'Riad_Meftaha-Rabat.csv', 'Riad_Zyo-Rabat.csv', 'STORY_Rabat-Rabat.csv', 'Villa_Mandarine-Rabat.csv', 'Barcelo_Anfa_Casablanca-Casablanca_Casablanca_Settat.csv', 'Dar_Bargach-Tangier_Tanger_Tetouan_Al_Hoceima.csv', 'Dar_Jameel-Tangier_Tanger_Tetouan_Al_Hoceima.csv', 'El_Minzah_Hotel-Tangier_Tanger_Tetouan_Al_Hoceima.csv', 'Four_Seasons_Hotel_Casablanca-Casablanca_Casablanca_Settat.csv', 'Grand_Hotel_Villa_de_France-Tangier_Tanger_Tetouan_Al_Hoceima.csv', 'Hilton_Garden_Inn_Tanger_City_Center-Tangier_Tanger_Tetouan_Al_Hoceima.csv', 'Hilton_Tanger_City_Center_Hotel_Residences-Tangier_Tanger_Tetouan_Al_Hoceima.csv', 'Hilton_Tangier_Al_Houara_Resort_Spa-Tangier_Tanger_Tetouan_Al_Hoceima.csv', 'Hotel_Astrid-Casablanca_Casablanca_Settat.csv', 'Hotel_Boustane-Casablanca_Casablanca_Settat.csv', 'Hotel_Central-Casablanca_Casablanca_Settat.csv', 'Hotel_El_Djenina-Tangier_Tanger_Tetouan_Al_Hoceima.csv', 'Hotel_Le_Doge-Casablanca_Casablanca_Settat.csv', 'Hotel_Marco_Polo-Tangier_Tanger_Tetouan_Al_Hoceima.csv', 'Hotel_Premiere_Classe_Casablanca_Centre_Ville-Casablanca_Casablanca_Settat.csv', 'Hotel_Royal_Tulip_City_Center_Tanger-Tangier_Tanger_Tetouan_Al_Hoceima.csv', 'Hotel_Volubilis-Casablanca_Casablanca_Settat.csv', 'Hyatt_Regency_Casablanca-Casablanca_Casablanca_Settat.csv', 'Ibis_Budget_Tanger-Tangier_Tanger_Tetouan_Al_Hoceima.csv', 'Ibis_Tanger_City_Center_Hotel-Tangier_Tanger_Tetouan_Al_Hoceima.csv', 'Kenzi_Tower_Hotel-Casablanca_Casablanca_Settat.csv', 'Le_Casablanca_Hotel-Casablanca_Casablanca_Settat.csv', 'Lhostel_a_Casablanca-Casablanca_Casablanca_Settat.csv', 'Mamora_Bay-Tangier_Tanger_Tetouan_Al_Hoceima.csv', 'Manzil_Hotel-Casablanca_Casablanca_Settat.csv', 'MELLIBER_Appart_Hotel-Casablanca_Casablanca_Settat.csv', 'Movenpick_Hotel_Casablanca-Casablanca_Casablanca_Settat.csv', 'Palais_Zahia-Tangier_Tanger_Tetouan_Al_Hoceima.csv', 'Pestana_Tanger_City_Center-Tangier_Tanger_Tetouan_Al_Hoceima.csv', 'Point_du_Jour-Casablanca_Casablanca_Settat.csv', 'Radisson_Blu_Hotel_Casablanca_City_Center-Casablanca_Casablanca_Settat.csv', 'The_Medina_Hostel-Tangier_Tanger_Tetouan_Al_Hoceima.csv', 'sofitel _rabat-rabat.csv', 'Riad_Zahra-Essaouira.csv', 'Riu_Palace_Tikida-Agadir.csv']

for file in csv_files:
    file_name = os.path.basename(file)
    file_name, file_ext = os.path.splitext(file_name)
    name = file_name.split("-")[0]
    city = file.split("-")[1].split(".")[0]
    df = pd.read_csv(file)
    df['hotelName'] = name
    df['city'] = city
    df.to_csv(file, index=False)
'''



directory = '/home/abdel/Documents/DOTNET_Project/Data backup/DataRepo'

csv_files= [ 'Iberostar_Founty_Beach-Agadir.csv', 'LABRANDA_Les_Dunes_d_Or-Agadir.csv', 'White_Beach_Resort_Taghazout-Tamraght_Agadir.csv', 'Atlantic_Hostel-Essaouira.csv', 'halassa_sea_spa_MGallery-Essaouira.csv', 'Hotel_Riad_Benatar-Essaouira.csv', 'L_Heure_Bleue_Palais-Essaouira.csv', 'Lodge-Essaouira.csv', 'Riad_Chbanate-Essaouira.csv', 'Riad_Le_Grand_Large-Essaouira.csv', 'Sofitel_Essaouira_Mogador_Golf_Spa-Essaouira.csv', 'Dar_7_Louyat-Fes_Fes_Meknes.csv', 'Dar_El_Mandar_Farm-Fes_Fes_Meknes.csv', 'Dar_Hafsa-Fes_Fes_Meknes.csv', 'Fes_Marriott_Hotel_Jnan_Palace-Fes_Fes_Meknes.csv', 'Hostel_Medina_Social_Club-Fes_Fes_Meknes.csv', 'Hotel_Spa_Riad_Dar_Bensouda-Fes_Fes_Meknes.csv', 'Ibis_budget_Fes-Fes_Fes_Meknes.csv', 'Palais_Faraj_Suites_Spa-Fes_Fes_Meknes.csv', 'Riad_Braya-Fes_Fes_Meknes.csv', 'Riad_Fes_Maya_Suite_Spa-Fes_Fes_Meknes.csv', 'Riad_Ibn_Khaldoun-Fes_Fes_Meknes.csv', 'Riad_Laaroussa_Hotel_and_Spa-Fes_Fes_Meknes.csv', 'Riad_Le_Calife-Fes_Fes_Meknes.csv', 'Riad_Verus-Fes_Fes_Meknes.csv', 'Riad_Zitouna-Fes_Fes_Meknes.csv', 'Iberostar_Club_Palmeraie-Marrakech.csv', 'La_Maison_Arabe-Marrakech.csv', 'Movenpick_Hotel_Mansour_Eddahbi-Marrakech.csv', 'Sol_Oasis-Marrakech.csv', 'Dar_Daif-Ouarzazate.csv', 'Dar_Panorama-Skoura_Ouarzazate.csv', 'Espace_Kasbah_Amridil-Skoura_Ouarzazate.csv', 'Hotel_marmar-Ouarzazate.csv', 'Le_Berbere_Palace-Ouarzazate.csv', 'L_Ma_Lodge-Skoura_Ouarzazate.csv', 'Maison_d_hotes_Dar_Farhana-Ouarzazate.csv', 'Riad_Ouarzazate-Ouarzazate.csv', 'arriott_Hotel-Rabat.csv', 'Dar_El_Kebira-Rabat.csv', 'Dar_Shaan-Rabat.csv', 'Dar_Zouhour-Rabat.csv', 'Ibis_Rabat-Rabat_Agdal.csv', 'Ibis_Rabat_Agdal-Rabat.csv', 'La_Tour_Hassan_Palace-Rabat.csv', 'Le_Diwan-Rabat_MGallery.csv', 'Le_Pietri_Urban_Hotel-Rabat.csv', 'ONOMO_Hotel-Rabat_Medina.csv', 'Reviews-The_View_Hotel-Rabat.csv', 'Riad_Dar_Soufa-Rabat.csv', 'Riad_Kalaa-Rabat.csv', 'Riad_Meftaha-Rabat.csv', 'Riad_Zyo-Rabat.csv', 'STORY_Rabat-Rabat.csv', 'Villa_Mandarine-Rabat.csv', 'Barcelo_Anfa_Casablanca-Casablanca_Casablanca_Settat.csv', 'Dar_Bargach-Tangier_Tanger_Tetouan_Al_Hoceima.csv', 'Dar_Jameel-Tangier_Tanger_Tetouan_Al_Hoceima.csv', 'El_Minzah_Hotel-Tangier_Tanger_Tetouan_Al_Hoceima.csv', 'Four_Seasons_Hotel_Casablanca-Casablanca_Casablanca_Settat.csv', 'Grand_Hotel_Villa_de_France-Tangier_Tanger_Tetouan_Al_Hoceima.csv', 'Hilton_Garden_Inn_Tanger_City_Center-Tangier_Tanger_Tetouan_Al_Hoceima.csv', 'Hilton_Tanger_City_Center_Hotel_Residences-Tangier_Tanger_Tetouan_Al_Hoceima.csv', 'Hilton_Tangier_Al_Houara_Resort_Spa-Tangier_Tanger_Tetouan_Al_Hoceima.csv', 'Hotel_Astrid-Casablanca_Casablanca_Settat.csv', 'Hotel_Boustane-Casablanca_Casablanca_Settat.csv', 'Hotel_Central-Casablanca_Casablanca_Settat.csv', 'Hotel_El_Djenina-Tangier_Tanger_Tetouan_Al_Hoceima.csv', 'Hotel_Le_Doge-Casablanca_Casablanca_Settat.csv', 'Hotel_Marco_Polo-Tangier_Tanger_Tetouan_Al_Hoceima.csv', 'Hotel_Premiere_Classe_Casablanca_Centre_Ville-Casablanca_Casablanca_Settat.csv', 'Hotel_Royal_Tulip_City_Center_Tanger-Tangier_Tanger_Tetouan_Al_Hoceima.csv', 'Hotel_Volubilis-Casablanca_Casablanca_Settat.csv', 'Hyatt_Regency_Casablanca-Casablanca_Casablanca_Settat.csv', 'Ibis_Budget_Tanger-Tangier_Tanger_Tetouan_Al_Hoceima.csv', 'Ibis_Tanger_City_Center_Hotel-Tangier_Tanger_Tetouan_Al_Hoceima.csv', 'Kenzi_Tower_Hotel-Casablanca_Casablanca_Settat.csv', 'Le_Casablanca_Hotel-Casablanca_Casablanca_Settat.csv', 'Lhostel_a_Casablanca-Casablanca_Casablanca_Settat.csv', 'Mamora_Bay-Tangier_Tanger_Tetouan_Al_Hoceima.csv', 'Manzil_Hotel-Casablanca_Casablanca_Settat.csv', 'MELLIBER_Appart_Hotel-Casablanca_Casablanca_Settat.csv', 'Movenpick_Hotel_Casablanca-Casablanca_Casablanca_Settat.csv', 'Palais_Zahia-Tangier_Tanger_Tetouan_Al_Hoceima.csv', 'Pestana_Tanger_City_Center-Tangier_Tanger_Tetouan_Al_Hoceima.csv', 'Point_du_Jour-Casablanca_Casablanca_Settat.csv', 'Radisson_Blu_Hotel_Casablanca_City_Center-Casablanca_Casablanca_Settat.csv', 'The_Medina_Hostel-Tangier_Tanger_Tetouan_Al_Hoceima.csv', 'sofitel _rabat-rabat.csv', 'Riad_Zahra-Essaouira.csv', 'Riu_Palace_Tikida-Agadir.csv']

for filename in csv_files:
    file_name = os.path.basename(filename)
    file_name, file_ext = os.path.splitext(file_name)
    name = file_name.split("-")[0]
    city = filename.split("-")[1].split(".")[0]



    if filename.endswith('.csv'):
        with open(os.path.join(directory, filename), 'r') as f:
            reader = csv.reader(f)
            rows = list(reader)

        with open(os.path.join(directory, filename), 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(rows[0] + ['hotelName', 'city'])
            for row in rows[1:]:
                writer.writerow(row + [name, city])



