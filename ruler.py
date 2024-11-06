from IPython.display import display, Image
import ipywidgets as widgets
from utils import get_avatars

p = r'C:\Users\cripp\OneDrive\Desktop\WIZ016-GA01_Righello\pngtree-isolated-cat-on-white-background-png-image_7094927.png'

class Ruler:
    def __init__(self):
        self.input_text = widgets.Text(
            value='',
            placeholder='Scrivi qui...',
            description='',
            disabled=False
        )

        self.output_box = widgets.Output()
        self.input_text.on_submit(self.on_submit)
        self.status = -1

        self.avatars = get_avatars()
        
        with self.output_box:
            print('Qual è il tuo nome?')
            self.input_text.value = ''

    def on_submit(self, text):
        with self.output_box:
            self.output_box.clear_output()
            user_input = self.input_text.value

            # Verifica iniziale
            if self.status == -1:
                self.player = user_input
                if user_input not in self.avatars:
                    print('Non ti è permesso accedere.')
                else:
                    print('Benvenuto!')
                    print('Ti avevo detto che avrei usato un modo alternativo :)')
                    print('Per cominciare scrivi il nome di un altro Avatar.')
                    self.status += 1
                    
            # Inizio del gioco
            elif self.status == 0:
                if user_input not in self.avatars:
                    print('Riprova.')
                elif user_input in self.avatars and user_input == self.player:
                    print('Non puoi usare ancora il tuo nome.')
                else:
                    self.status += 1

            # Livello 1
            elif self.status == 1:
                print('Cominciamo.')
                self.image_widget = widgets.Image(
                    value=open(p, 'rb').read(),  # Sostituisci con il percorso dell'immagine
                    format='png',
                    width=300,
                    height=300
                )
                display(self.image_widget)

            else:
                raise ValueError('Errore nel cambio di stato.')

            self.input_text.value = ''
    
    def play(self):
        display(self.output_box, self.input_text)