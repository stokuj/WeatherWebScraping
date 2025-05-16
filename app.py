import tkinter as tk
from tkinter import ttk
import functions as f
import sv_ttk
from tkinter import PhotoImage

class App:
    def __init__(self, master):
        self.master = master
        self.create_widgets()
        #ttk.Style().theme_use('clam')

    def create_widgets(self):
        lista_stacji = [
            'Białystok',
            'Bielsko Biała',
            'Chojnice',
            'Częstochowa',
            'Elbląg',
            'Gdańsk',
            'Gorzów',
            'Hel',
            'Jelenia Góra',
            'Kalisz',
            'Kasprowy Wierch',
            'Katowice',
            'Kętrzyn',
            'Kielce',
            'Kłodzko',
            'Koło',
            'Kołobrzeg',
            'Koszalin',
            'Kozienice',
            'Kraków',
            'Krosno',
            'Legnica',
            'Lesko',
            'Lębork',
            'Lublin',
            'Łeba',
            'Łódź',
            'Mikołajki',
            'Mława',
            'Nowy Sącz',
            'Olsztyn',
            'Opole',
            'Ostrołęka',
            'Piła',
            'Platforma',
            'Płock',
            'Poznań',
            'Przemyśl',
            'Racibórz',
            'Resko',
            'Rzeszów',
            'Sandomierz',
            'Siedlce',
            'Słubice',
            'Sulejów',
            'Suwałki',
            'Szczecin',
            'Szczecinek',
            'Śnieżka',
            'Świnoujście',
            'Tarnów',
            'Terespol',
            'Toruń',
            'Ustka',
            'Warszawa',
            'Wieluń',
            'Włodawa',
            'Wrocław',
            'Zakopane',
            'Zamość',
            'Zielona Góra'
        ]
        lista_wykresow = [
            'Temperatury',
            'Temperatury i opadu',
            'Predkosci wiatru',
            'Kieruneku wiatru',
            'Wilgotnosci wzglednej',
            'Sumy opadów',
            'Cisnienia'
        ]
        lista_zakresow=[
            'Cały zakres',
            'Ostatni miesiąc',
            'Ostatni tydzień',
            'Ostatnie 3 dni',
            'Ostatnie 24h',
            'Osatnie 12h'
        ]

        ### FRAME DEFINITION
        self.frame1 = ttk.LabelFrame(self.master, width=800, height=150, text ='')
        self.frame2 = ttk.LabelFrame(self.master, width=800, height=310)
        self.frame3 = ttk.LabelFrame(self.master, width=800, height=130)
        self.frame4 = ttk.LabelFrame(self.master, width=800, height=130)
        self.frame5 = ttk.LabelFrame(self.master, width=800, height=150)

        #### ELEMENT DEFFINITION
        self.button1 = ttk.Button(self.frame1, text="Rozpocznij zbieranie danych", style='Accent.TButton', command=self.button1_callback)
        self.combobox1 = ttk.Combobox(self.frame2, values=lista_stacji)
        self.combobox1.set('Hel')  # Set default value
        self.label2 = tk.Label(self.frame2, text="Stacja:")
        self.combobox2 = ttk.Combobox(self.frame2, values=lista_wykresow)
        self.combobox2.set('Temperatury')  # Set default value
        self.label3 = tk.Label(self.frame2, text="Typ wykresu:")
        self.combobox3 = ttk.Combobox(self.frame2, values=lista_zakresow)
        self.combobox3.set('Cały zakres')  # Set default value
        self.label4 = tk.Label(self.frame2, text="Wyszukaj:")
        self.label4.configure(bg='#e3e1e1')
        self.label5 = tk.Label(self.frame3, text="")
        self.mean = 0
        self.button4 = ttk.Button(self.frame3, text="Oblicz średnią", command=self.button4_callback)
        self.button2 = ttk.Button(self.frame4, text="Otwórz wykres", command=self.button2_callback)
        self.button3 = ttk.Button(self.frame4, text="Pobierz", command=self.button3_callback)
        self.label1 = tk.Label(self.frame5, text="Dane pochodzą z  \nInstytutu Meteorologii i Gospodarki Wodnej")
        self.label5.configure(bg='#e3e1e1')        ### ELEMENT POSITIONING

        ### FRAME 1
        self.frame1.place(x=100, y=50)
        self.button1.place(x=self.frame1.winfo_x()+10, y=self.frame1.winfo_y(), width=780, height=100)

        ### FRAME 2
        self.frame2.place(x=100, y=200)

        self.combobox1.place(x=self.frame2.winfo_x()+410,       y=self.frame2.winfo_y(),            width=380, height=75)
        self.label2.place   (x=self.frame2.winfo_x()+10,        y=self.frame2.winfo_y(),            width=380, height=75)

        self.combobox2.place(x=self.frame2.winfo_x()+410,       y=self.frame2.winfo_y()+75+15,      width=380, height=75)
        self.label3.place   (x=self.frame2.winfo_x()+10,        y=self.frame2.winfo_y()+75+15,      width=380, height=75)

        self.combobox3.place(x=self.frame2.winfo_x()+410,       y=self.frame2.winfo_y()+150+30,     width=380, height=75)
        self.label4.place   (x=self.frame2.winfo_x()+10,        y=self.frame2.winfo_y()+150+30,     width=380, height=75)

        ### FRAME 3 
        self.frame3.place(x=100, y=515)

        self.label5.place   (x=self.frame3.winfo_x()+410,       y=self.frame3.winfo_y(),            width=380, height=75)
        self.button4.place  (x=self.frame3.winfo_x()+10,        y=self.frame3.winfo_y(),            width=380, height=75)
        
        ### FRAME 4 
        self.frame4.place(x=100, y=650)

        self.button2.place  (x=self.frame4.winfo_x()+410,       y=self.frame4.winfo_y(),            width=380, height=75)
        self.button3.place  (x=self.frame4.winfo_x()+10,        y=self.frame4.winfo_y(),            width=380, height=75)
        
        ### FRAME 5 
        self.frame5.place(x=100, y=780)

        self.label1.place  (x=self.frame5.winfo_x()+10,        y=self.frame5.winfo_y(),            width=780, height=100)


        self.label1.configure(bg='#FFFDF0')
        self.label2.configure(bg='#e3e1e1')
        self.label3.configure(bg='#e3e1e1')


    def button1_callback(self):
        f.save_data_to_csv('data.csv')
        f.insert_data_from_csv('data.csv')
        self.frame1["text"] = "Pracuje"

        minuts = 5
        self.master.after(minuts*60*1000, self.button1_callback)

    def button2_callback(self):
        #Take value from combbbox
        stacja = self.combobox1.get()
        kategoria = f.change_name_to_value(self.combobox2.get())
        
        #Make pandas table
        df = f.take_data_from_database("stacja", stacja)
        df.sort_values(by='data_godzina', inplace=True)
        
        f.deleteDuplicates()
        
        f.make_plot(df, kategoria, zakres=self.combobox3.get())
    
    def button3_callback(self):
        f.save_selected_to_csv("MyClass", zakres=self.combobox3.get())


    def button4_callback(self):
        #Take value from combbbox
        stacja = self.combobox1.get()
        kategoria = f.change_name_to_value(self.combobox2.get())
        
        #Make pandas table
        df = f.take_data_from_database("stacja", stacja)
        df.sort_values(by='data_godzina', inplace=True)
        
        f.deleteDuplicates()


        self.mean = f.calc_mean(self.mean, df, kategoria, zakres=self.combobox3.get())
        self.label5.config(text=self.mean)

if __name__ == "__main__":
    root = tk.Tk()
    root.wm_title("Aplikacja Pogodowa")
    
    # Simply set the theme
    sv_ttk.set_theme("light")

    #root.tk.call("source", "azure.tcl")
    #root.tk.call("set_theme", "light")
    #root.tk.call('source', 'forest-light.tcl')
    #ttk.Style().theme_use('forest-light')
    root.geometry("1000x1000")

    img = PhotoImage(file='icon.png')
    root.tk.call('wm', 'iconphoto', root._w, img)
    app = App(root)
    root.mainloop()

