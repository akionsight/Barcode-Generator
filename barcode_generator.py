import PySimpleGUI as sg
import random

sg.change_look_and_feel('DarkAmber')
layout = [ [sg.Text("enter text or link in barcode")],
            [sg.Input()],
            [sg.OK()]]


window = sg.Window("barcode generator").Layout(layout)

while True:
    event, values = window.read()
    if event in (None, 'OK'):	
        text = values[0]
        break
    
def main(text):
    import pdf417
    codes = pdf417.encode(text, security_level=5)
    image = pdf417.render_image(codes)
    random_file_name = random.randint(1000000000,9999999999)
    image.save(f'{random_file_name}.jpg')
    sg.popup(f'barcode is now created. its file name is {random_file_name}.jpg')
    
main(text)
