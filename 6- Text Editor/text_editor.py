import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file():
  filepath = askopenfilename(filetypes=[
    ('Text Files', '*.txt'),
    ('All Files', '*.*'),])
  
  if not filepath:
    return
  
  txt_edit.delete(1.0, tk.END)
  with open(filepath, 'r') as input_file:
    text = input_file.read()
    txt_edit.insert(tk.END, text)
  
  window.title(f'Elzoz Text Editor - {filepath}')

def save_file():
  filepath = asksaveasfilename(defaultextension='txt',
    filetypes=[
    ('Text Files', '*.txt'),
    ('All Files', '*.*'),])
  
  if not filepath:
    return
  
  with open(filepath, 'w') as output_file:
    output_file.write(txt_edit.get(1.0, tk.END))
  
  window.title(f'Elzoz Text Editor - {filepath}')

window = tk.Tk()
window.title('Elzoz Text Editor')
window.rowconfigure(0, minsize=500)
window.columnconfigure(1, minsize=700)

txt_edit = tk.Text(window)
txt_edit.grid(column=1, row=0, sticky='nsew')
txt_edit.configure(bg='gold')

frame_buttons = tk.Frame(window, relief=tk.RAISED)
frame_buttons.grid(column=0, row=0, padx=7, pady=7, sticky='nw')

btn_open = tk.Button(frame_buttons, text='Open File', command=open_file)
btn_save = tk.Button(frame_buttons, text='Save As', command=save_file)

btn_open.grid(column=0, row=0, sticky='ew')
btn_save.grid(column=0, row=1, pady=7, sticky='ew')

tk.mainloop()