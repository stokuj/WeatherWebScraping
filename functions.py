import os
import sys
import pandas as pd
from bs4 import BeautifulSoup
import requests
import sqlite3 as sl
import csv
import os
import psycopg2
import plotly.express as px
import datetime
import plotly.graph_objects as go
import plotly.subplots as er
########################################
class MyClass():
    def __init__(self, id_stacji, stacja, data_pomiaru, godzina_pomiaru, temperatura, predkosc_wiatru, kierunek_wiatru, wilgotnosc_wzgledna, suma_opadu, cisnienie):
        self.id_stacji = id_stacji
        self.stacja = stacja
        self.data_pomiaru = data_pomiaru
        self.godzina_pomiaru = godzina_pomiaru
        self.temperatura = temperatura
        self.predkosc_wiatru = predkosc_wiatru
        self.kierunek_wiatru = kierunek_wiatru
        self.wilgotnosc_wzgledna = wilgotnosc_wzgledna
        self.suma_opadu = suma_opadu
        self.cisnienie = cisnienie
        
    def do_conn():
        return psycopg2.connect(
            host="localhost", database="html", user="postgres", password="1569"
        )
########################################


def table_exists(table_name):
    conn = MyClass.do_conn()
    cursor = conn.cursor()
    cursor.execute(f"SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = '{table_name}')")
    conn.close
    return cursor.fetchone()[0]
        
def save_data_to_csv(csv_file):
    data = []

    list_header = []
    r = requests.get('https://danepubliczne.imgw.pl/api/data/synop/format/html')
    soup = BeautifulSoup(r.content,'html.parser')
    header = soup.find_all("table")[0].find("tr")

    for items in header:
        try:
            list_header.append(items.get_text())
        except Exception:
            continue

    # for getting the data
    HTML_data = soup.find_all("table")[0].find_all("tr")[1:]

    for element in HTML_data:
        sub_data = []
        for sub_element in element:
            try:
                sub_data.append(sub_element.get_text())
            except Exception:
                continue
        data.append(sub_data)

    # Storing the data into Pandas
    # DataFrame
    dataFrame = pd.DataFrame(data = data, columns = list_header)

    # Converting Pandas DataFrame
    # into CSV file
    dataFrame.to_csv(csv_file)
#Can be used at the star or after wiping database
def create_table():
    # Connect to the database
    conn = MyClass.do_conn()

    # Create a cursor
    cur = conn.cursor()

    # Create the table
    cur.execute('''CREATE TABLE MyClass 
                (
                id SERIAL PRIMARY KEY,
                id_stacji INTEGER,
                stacja TEXT,
                data_pomiaru DATE,
                godzina_pomiaru TIME,
                temperatura FLOAT,
                predkosc_wiatru FLOAT,
                kierunek_wiatru FLOAT,
                wilgotnosc_wzgledna FLOAT,
                suma_opadu FLOAT,
                cisnienie FLOAT,
                data_godzina TIMESTAMP
    )''')

    # Commit the changes
    conn.commit()

    # Close the connection
    conn.close()

#Not used amt    
def insert_data(id_stacji, stacja, data_pomiaru, godzina_pomiaru, temperatura, predkosc_wiatru, kierunek_wiatru, wilgotnosc_wzgledna, suma_opadu, cisnienie):
    # Connect to the database
    conn = MyClass.do_conn()

    # Create a cursor
    cur = conn.cursor()

    # Insert the data
    cur.execute('''INSERT INTO MyClass (id_stacji, stacja, data_pomiaru, godzina_pomiaru, temperatura, predkosc_wiatru, kierunek_wiatru, wilgotnosc_wzgledna, suma_opadu, cisnienie)
                  VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''',
               (id_stacji, stacja, data_pomiaru, godzina_pomiaru, temperatura,predkosc_wiatru, kierunek_wiatru, wilgotnosc_wzgledna, suma_opadu, cisnienie))

    # Commit the changes
    conn.commit()

    # Close the connection
    conn.close()

def insert_data_from_csv(csv_file):
    # Connect to the database
    conn = MyClass.do_conn()
    # Create a cursor
    cur = conn.cursor()

    # Open the CSV file
    with open(csv_file, 'r', encoding='utf-8') as f:
        _extracted_from_insert_data_from_csv_10(f, cur)
    # Commit the changes
    conn.commit()

    # Close the connection
    conn.close()


# TODO Rename this here and in `insert_data_from_csv`
def _extracted_from_insert_data_from_csv_10(f, cur):
    # Create a CSV reader
    reader = csv.reader(f)

    # Skip the first row (headers)
    next(reader)

    # Execute the SELECT statement
    cur.execute('''SELECT COUNT(*) FROM MyClass''')

    # Fetch the result
    result = cur.fetchone()

        # Check if the table is empty
    if result[0] == 0:
        print("The table was empty")

    else:
        print("The table was not empty")

        #so we need to test if there is allready some data with the same date and time

        # Execute the SELECT statement
        cur.execute('''SELECT data_pomiaru, godzina_pomiaru FROM MyClass ORDER BY data_pomiaru DESC, godzina_pomiaru DESC LIMIT 1''')

        # Fetch the row
        row_tmp = cur.fetchone()

        # Print the values
        print(row_tmp[0]) #data_pomiaru
        print(row_tmp[1]) #godzina_pomiaru

    # its fine

    # Iterate over the rows
    for row in reader:
        if row[6] == '':
            row[6] = 0.0
        if row[7] == '':
            row[7] = 0.0   
        if row[8] == '':
            row[8] = 0.0 
        if row[9] == '':
            row[9] = 0.0
        if row[10] == '':
            row[10] = 0.0 
        if row[11] == '':
            row[11] = 0.0 
        # The time value
        time_value = datetime.datetime.strptime(row[5], '%H').time()

        # Convert the time value to a string
        time_value_str = time_value.strftime('%H:%M:%S')

        # The datetime value
        datetime_value = datetime.datetime.combine(datetime.datetime.strptime(row[4], '%Y-%m-%d').date(),
                                                datetime.datetime.strptime(time_value_str, '%H:%M:%S').time())

        # Execute the INSERT INTO query with the correct parameter values
        cur.execute('''INSERT INTO MyClass (id_stacji, stacja, data_pomiaru, godzina_pomiaru, temperatura, predkosc_wiatru, kierunek_wiatru, wilgotnosc_wzgledna, suma_opadu, cisnienie, data_godzina)
                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''',
                    (row[2], row[3], row[4], time_value, row[6], row[7], row[8], row[9], row[10],row[11],datetime_value))

def take_data_from_database(po_czym_filtrować, wartosc_kolumny):
    # Connect to the database
    conn = MyClass.do_conn()
    
    # Create a cursor
    cur = conn.cursor()

    # Execute the SELECT statement
    
    if po_czym_filtrować == 'stacja':
        cur.execute('''SELECT * FROM MyClass WHERE stacja = %s''', (wartosc_kolumny,))



    # Fetch all the rows
    rows = cur.fetchall()

    # Create a DataFrame from the rows
    df = pd.DataFrame(rows, columns=["id", "id_stacji", "stacja", "data_pomiaru", "godzina_pomiaru", "temperatura", "predkosc_wiatru", "kierunek_wiatru", "wilgotnosc_wzgledna", "suma_opadu", "cisnienie", "data_godzina"])

    # Print the DataFrame
    #print(df)

    # Close the connection
    conn.close()
    
    return df

def make_plot(df, y_value, zakres):

    #change df acoring to zakres value
    df = filter_df(df, zakres)

    if y_value == 'temperatura i opady':
        fig = _extracted_from_make_plot_6(df)
    elif y_value == 'suma_opadu':
        fig = px.bar(df, x='data_godzina', y='suma_opadu')
    elif y_value == 'kierunek_wiatru':

        # create wind_range column
        df['wind_range'] = pd.cut(df['kierunek_wiatru'], bins=[0, 45, 90, 135, 180, 225, 270, 315, 360], labels=['N', 'NE', 'E', 'SE', 'S', 'SW ', 'W', 'NW'])

        # count occurrences in each wind range
        occurrences = df.groupby(['wind_range']).size().reset_index(name='counts')

        # calculate mean air_speed for each wind range
        mean_air_speed = df.groupby(['wind_range'])['predkosc_wiatru'].mean().reset_index()

        # create bar polar chart with the correct number of bars and the bars colored based on air_speed
        fig = px.bar_polar(occurrences, r=occurrences.counts, theta=occurrences.wind_range, color=mean_air_speed.predkosc_wiatru,
                   color_discrete_sequence= px.colors.sequential.Plasma_r)


    else:
        fig = px.line(df, x='data_godzina', y=y_value) 

    fig.update_layout(
        annotations=[
            dict(
                x=0,
                y=-0.1,
                xref="paper",
                yref="paper",
                text="Dane pochodzą z  Instytutu Meteorologii i Gospodarki Wodnej",
                showarrow=False,
                font=dict(
                    family="Courier New, monospace",
                    size=10,
                    color="gray"
                )
            )
        ]
    )
    print(df)

    fig = update_title_and_x_y_based_on_kat(fig, y_value, zakres)
    fig.show()

def update_title_and_x_y_based_on_kat(fig, kat, zakres):

    if kat == 'temperatura':
        fig.update_layout(
            title_text=("Wykres temperatury [°C]. Zakres czasu: " + zakres),
            xaxis=dict(title="Data wraz z godziną pomiaru"),
            yaxis=dict(title="Temperatura  (°C)")
        )

    elif kat == 'temperatura i opady':
        fig.update_layout(
            title_text=("Wykres temperatury [°C] oraz sumy opadu deszczu [mm]. Zakres czasu: " + zakres),
            xaxis=dict(title="Data wraz z godziną pomiaru"),
            yaxis=dict(title="Temperatura (°C)"),
            yaxis2=dict(title="Suma opdau (mm)", overlaying="y", side="right")
        )

    elif kat == 'predkosc_wiatru':
        fig.update_layout(
            title_text=("Wykres prędkości wiatru [m/s]. Zakres czasu: " + zakres),
            xaxis=dict(title="Data wraz z godziną pomiaru"),
            yaxis=dict(title="Prędkość wiatru (m/s)")
        )

    elif kat == 'kierunek_wiatru':
        fig.update_layout(
            title_text=("Wykres kierunku wiatru [°]. Zakres czasu: " + zakres)
        )

    elif kat == 'wilgotnosc_wzgledna':
        fig.update_layout(
            title_text=("Wykres wilgotności względnej [%]. Zakres czasu: " + zakres),
            xaxis=dict(title="Data wraz z godziną pomiaru"),
            yaxis=dict(title="Wilgotność względna (%)")
        )

    elif kat == 'suma_opadu':
        fig.update_layout(
            title_text=("Wykres sumy opadu deszczu [mm]. Zakres czasu: " + zakres),
            xaxis=dict(title="Data wraz z godziną pomiaru"),
            yaxis=dict(title="Suma opadu (mm)")
        )

    elif kat == 'cisnienie':
        fig.update_layout(
            title_text=("Wykres ciśnienia [hPa]. Zakres czasu: " + zakres),
            xaxis=dict(title="Data wraz z godziną pomiaru"),
            yaxis=dict(title="Ciśnienie (hPa)")
        )


    return fig

# TODO Rename this here and in `make_plot`
def _extracted_from_make_plot_6(df):
        #fig = px.line(df, x='data_godzina', y='temperatura', title=('temperatura i opad' + " / Data wraz z godziną pomiaru"))
        #fig.add_bar(x=df['data_godzina'], y=df['suma_opadu']/10, name="Suma opadu")


    result = er.make_subplots(specs=[[{"secondary_y": True}]])
    result.add_trace(
        go.Scatter(
            x=df['data_godzina'], y=df['temperatura'], name="Temperatura"), 
        secondary_y=False,
    )

    result.add_trace(
        go.Bar(
            x=df['data_godzina'], y=df['suma_opadu'], name="Suma opadu",opacity=0.7), 
        secondary_y=True,
    )

    return result
    
def deleteDuplicates():
    # Connect to the database
    conn = MyClass.do_conn()

    # Create a cursor
    cur = conn.cursor()
    
    cur.execute('''
        DELETE FROM MyClass
        WHERE id IN (
            SELECT id
            FROM (
                SELECT id, ROW_NUMBER() OVER (PARTITION BY stacja, data_godzina ORDER BY id) AS row_number
                FROM MyClass
            ) t
            WHERE t.row_number > 1
        )''') 
    # Commit the changes
    print("done")
    conn.commit()

    # Close the connection
    conn.close()

def change_name_to_value(str):

    if str == 'Temperatury':
        str = 'temperatura'

    elif str == 'Temperatury i opadu':
        str = 'temperatura i opady'

    elif str == 'Predkosci wiatru':
        str = 'predkosc_wiatru'

    elif str == 'Kieruneku wiatru':
        str = 'kierunek_wiatru'

    elif str == 'Wilgotnosci wzglednej':
        str = 'wilgotnosc_wzgledna'

    elif str == 'Sumy opadów':
        str = 'suma_opadu'

    elif str == 'Cisnienia':
        str = 'cisnienie'
    else:
        str = 'suma_opadu'

    return str

def calc_mean(mean, df, kat, zakres):

    if kat == 'temperatura i opady':
        return "Nie można"

    df = filter_df(df, zakres)

    #Calculate mean, round it, and return it
    mean = df[kat].mean()
    mean = round(mean, 2)
    mean = str(mean)
    mean = add_unit(mean, kat)

    print(df)
    print(mean)
    return mean

def add_unit(str, kat):
    if kat == 'temperatura':
        str += ' (°C)'

    elif kat == 'temperatura i opady':
        str += ' (°C) | (mm)'

    elif kat == 'predkosc_wiatru':
        str += ' (m/s)'

    elif kat == 'kierunek_wiatru':
        str += ' (°)'

    elif kat == 'wilgotnosc_wzgledna':
        str += ' (%)'

    elif kat == 'suma_opadu':
        str += ' (mm)'

    elif kat == 'cisnienie':
        str += ' (hPa)'

    return str

def filter_df(df, zakres):

    print(zakres)
    df['data_godzina'] = pd.to_datetime(df['data_godzina'])

    # filter the dataframe based on the value of the zakres variable
    if zakres == 'Cały zakres':
        filtered_df = df
    elif zakres == 'Ostatni miesiąc':
        filtered_df = df[df['data_godzina'] >= (datetime.datetime.now() - datetime.timedelta(days=30))]
    elif zakres == 'Ostatni tydzień':
        filtered_df = df[df['data_godzina'] >= (datetime.datetime.now() - datetime.timedelta(days=7))]
    elif zakres == 'Ostatnie 3 dni':
        filtered_df = df[df['data_godzina'] >= (datetime.datetime.now() - datetime.timedelta(days=3))]
    elif zakres == 'Ostatnie 24h':
        filtered_df = df[df['data_godzina'] >= (datetime.datetime.now() - datetime.timedelta(hours=24))]
    elif zakres == 'Osatnie 12h':
        filtered_df = df[df['data_godzina'] >= (datetime.datetime.now() - datetime.timedelta(hours=12))]
    else:
        filtered_df = df

    return filtered_df


def save_selected_to_csv(table_name, zakres):
    conn = MyClass.do_conn()

    query = f"SELECT * FROM {table_name}"
    df = pd.read_sql_query(query, conn)

    #filter df
    df = filter_df(df, zakres)

    df.to_csv('downloaded.csv', index=False)
    conn.close()
    print('Data has been retrieved and saved to "downloaded.csv" file.')

#Uncommnet debugging/testing    
    
# Insert the data from html to the csv
#save_data_to_csv('data.csv')

# Insert the data from the CSV file to database
#insert_data_from_csv('data.csv')

# Insert some example data
#insert_data('12345', 'Station 1', '2022-01-01', '12:00:00', '25', 'NW', '70', '0.0', '1013')
#insert_data('23456', 'Station 2', '2022-01-01', '12:00:00', '28', 'SW', '65', '0.0', '1012')
#insert_data('34567', 'Station 3', '2022-01-01', '12:00:00', '30', 'SE', '60', '0.0', '1011')
    
#create_table()

#Test if there are tables in db
if table_exists('myclass'):
    print("Table 'MyClass' exists in the database")
else:
    create_table()
    
