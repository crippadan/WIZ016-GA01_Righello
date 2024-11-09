from IPython.display import display, Image
import ipywidgets as widgets
import pyzipper
import io
import requests
import pandas as pd
import json

import warnings
warnings.simplefilter("ignore", category=DeprecationWarning)

class Ruler:
    def __init__(self, pw):
        self.input_text = widgets.Text(
            value='',
            placeholder='Scrivi qui...',
            description='',
            disabled=False
        )

        self.output_box = widgets.Output()
        self.answer_box = widgets.Output()
        self.input_text.on_submit(self.on_submit)
        self.status = 0
        self.check = False
        self.pw = pw

        self.get_assets()
        self.get_config()

        with self.output_box:
            print('Qual è il tuo nome?')
            self.input_text.value = ''

    def get_config(self):
        url = 'https://github.com/crippadan/WIZ016-GA01_Righello/raw/refs/heads/main/config.zip'
        response = requests.get(url)
        with pyzipper.AESZipFile(io.BytesIO(response.content), 'r') as zip_file:
            zip_file.pwd = self.pw.encode('utf-8')
            with zip_file.open('config/rules.csv', 'r') as file:
                df = pd.read_csv(file, header=None)
                self.rules = df[0].tolist()

            with zip_file.open('config/avatars.json', 'r') as file:
                self.avatars = json.load(file)

    def get_assets(self):
        url = 'https://github.com/crippadan/WIZ016-GA01_Righello/raw/refs/heads/main/assets.zip'
        response = requests.get(url)

        with pyzipper.AESZipFile(io.BytesIO(response.content), 'r') as zip_file:
            zip_file.pwd = self.pw.encode('utf-8')
            
            with zip_file.open('assets/A.png', 'r') as file:
                img_data = file.read()
                self.image_widget_A = widgets.Image(value=img_data, format='png', width=600, height=300)

            with zip_file.open('assets/B.png', 'r') as file:
                img_data = file.read()
                self.image_widget_B = widgets.Image(value=img_data, format='png', width=300, height=300)

            with zip_file.open('assets/C.jpg', 'r') as file:
                img_data = file.read()
                self.image_widget_C = widgets.Image(value=img_data, format='png', width=300, height=300)

            with zip_file.open('assets/D.png', 'r') as file:
                img_data = file.read()
                self.image_widget_D = widgets.Image(value=img_data, format='png', width=300, height=300)

            with zip_file.open('assets/E.png', 'r') as file:
                img_data = file.read()
                self.image_widget_E = widgets.Image(value=img_data, format='png', width=300, height=300)

            with zip_file.open('assets/F.png', 'r') as file:
                img_data = file.read()
                self.image_widget_F = widgets.Image(value=img_data, format='png', width=200, height=200)

            self.image_widget_rule = []
            for i in range(1, 8):
                with zip_file.open(f'assets/{i}.png', 'r') as file:
                    img_data = file.read()
                    self.image_widget_rule.append(widgets.Image(value=img_data, format='png', width=1000, height=400))


    def on_submit(self, text):
        with self.output_box:
            self.output_box.clear_output()
            self.answer_box.clear_output()
            user_input = self.input_text.value

            # Verifica iniziale
            if self.status == 0:
                self.player = user_input
                if user_input not in self.avatars.keys():
                    print(f'Non ti è permesso accedere {user_input}.')
                else:
                    if user_input == 'Widkan':
                        print('Benvenuta Osservatrice!')
                        print('Il Ruler ti mostrerà le Regole, se gli darai le risposte corrette (ti avevo detto che avrei usato un modo alternativo :D ).')
                    else:
                        if self.avatars[user_input] == 'M':
                            print(f'Benvenuto {user_input}!')
                        else:
                            print(f'Benvenuta {user_input}!')
                        print('Il Ruler ti mostrerà le Regole, se gli darai le risposte corrette.')
                    print('Le risposte sono sempre una singola parola al singolare, in minuscolo, con iniziale maiuscola.')
                    print('Tutte le risposte sono parole relative a concetti astratti, mai a persone o oggetti.')
                    print('Per ogni Regola avrai a disposizione almeno un indizio.')
                    print('Per cominciare premi invio.')
                    self.status += 1


            # Livello 1
            elif self.status == 1:
                print('Regola numero 1.')
                if user_input != self.rules[self.status-1]:
                    image_box = widgets.VBox([self.image_widget_A, self.image_widget_B])
                    display(image_box)
                    if self.check:
                        with self.answer_box:
                            print('Risposta sbagliata, riprova.')
                    self.check = True
                else:
                    display(self.image_widget_rule[self.status-1])
                    with self.answer_box:
                        print('Premi invio per continuare')
                    self.status += 1
                    self.check = False

            # Livello 2
            elif self.status == 2:
                print('Regola numero 2.')
                if user_input != self.rules[self.status-1]:
                    print('\n')
                    print('BGGHVXGST')
                    display(self.image_widget_C)
                    if self.check:
                        with self.answer_box:
                            print('Risposta sbagliata, riprova.')
                    self.check = True
                else:
                    display(self.image_widget_rule[self.status-1])
                    with self.answer_box:
                        print('Premi invio per continuare')
                    self.status += 1
                    self.check = False

            # Livello 3
            elif self.status == 3:
                print('Regola numero 3.')
                if user_input != self.rules[self.status-1]:
                    print('\n')
                    print('"Net won" : "Gravità", "Seein\' tin" : "Relatività", "Beer hinges" : x')
                    print('\n')
                    if self.check:
                        with self.answer_box:
                            print('Risposta sbagliata, riprova.')
                    self.check = True
                else:
                    display(self.image_widget_rule[self.status-1])
                    with self.answer_box:
                        print('Premi invio per continuare')
                    self.status += 1
                    self.check = False

            # Livello 4
            elif self.status == 4:
                print('Regola numero 4.')
                if user_input != self.rules[self.status-1]:
                    print('\n')
                    print('Drowzee, G7, L5')
                    display(self.image_widget_D)
                    if self.check:
                        with self.answer_box:
                            print('Risposta sbagliata, riprova.')
                    self.check = True
                else:
                    display(self.image_widget_rule[self.status-1])
                    with self.answer_box:
                        print('Premi invio per continuare')
                    self.status += 1
                    self.check = False

            # Livello 5
            elif self.status == 5:
                print('Regola numero 5.')
                if user_input != self.rules[self.status-1]:
                    print('\n')
                    print('"Ogni enunciato (o formula o proprietà) che può essere dimostrato, cioè che può essere dedotto logicamente dagli enunciati primitivi, detti assiomi o postulati."')
                    print('\n')
                    print('"όλα είναι..."')
                    display(self.image_widget_E)
                    if self.check:
                        with self.answer_box:
                            print('Risposta sbagliata, riprova.')
                    self.check = True
                else:
                    display(self.image_widget_rule[self.status-1])
                    with self.answer_box:
                        print('Premi invio per continuare')
                    self.status += 1
                    self.check = False

            # Livello 6
            elif self.status == 6:
                print('Regola numero 6.')
                if user_input != self.rules[self.status-1]:
                    print('\n')
                    print('"O l\'avi seri..."')
                    display(self.image_widget_F)
                    if self.check:
                        with self.answer_box:
                            print('Risposta sbagliata, riprova.')
                    self.check = True
                else:
                    display(self.image_widget_rule[self.status-1])
                    with self.answer_box:
                        print('Premi invio per continuare')
                    self.status += 1
                    self.check = False

            # Livello 7
            elif self.status == 7:
                print('Regola numero 7.')
                if user_input != self.rules[self.status-1]:
                    print('\n')
                    print('Se son debole, non parti.')
                    print('Se son forte, non ti fermi.')
                    print('Se ci sarò, non rimarrai a terra.')
                    print('Se mancherò, cadere non sarà un problema.')
                    print('Trasformo dubbi in scelte, illusioni in obbiettivi.')
                    print('Alla fine, vivrò più di te.')
                    print('Cosa sono?')
                    print('\n')
                    if self.check:
                        with self.answer_box:
                            print('Risposta sbagliata, riprova.')
                    self.check = True
                else:
                    display(self.image_widget_rule[self.status-1])
                    with self.answer_box:
                        print('Premi invio per continuare')
                    self.status += 1
                    self.check = False

            elif self.status == 8:
                self.input_text.close()

            else:
                raise ValueError('Errore nel cambio di stato.')

            self.input_text.value = ''

    def play(self):
        display(self.output_box, self.answer_box, self.input_text)