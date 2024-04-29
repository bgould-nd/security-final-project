import tkinter as tk
from tkinter import filedialog
from vigenere import vin_encrypt, vin_decrypt
from TripleDes import tripleEncode, tripleDecode
from rsa import rsa_decrypt, rsa_encrypt

def UploadAction(event=None):
    input_entry.delete(0, tk.END)
    filename = filedialog.askopenfilename()
    print('Selected:', filename)
    input_entry.grid(row=5,column=1)
    input_entry.insert(0, filename)

def save_data_to_file(data): 
    filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if filename:
        with open(filename, "w") as file:
            file.write(data)


def update_ui(*args):
    # change available options based on selection
    if selected_input.get() == "Text" or selected_input.get() == "Binary":
        input_entry.grid(row=0,column=1 ,padx=5,pady=5)
        open_file_button.grid_forget()
    else:
        open_file_button.grid(row=0, column=1, padx=5, pady=5)
        input_entry.grid_forget()
    
    if selected_option.get() == "RSA" and selected_mode.get() == "Encrypt":
        e_label.grid(row=1,column=0)        #pack(side=tk.LEFT , padx=(10, 0))
        e_entry.grid(row=1,column=1)                        #pack(side=tk.LEFT, padx=(0, 10))
        n_label.grid(row=2,column=0)                        #pack(side=tk.LEFT, padx=(10, 0))
        n_entry.grid(row=2,column=1)
    elif selected_option.get() == "RSA" and selected_mode.get() == "Decrypt": #                       pack(side=tk.LEFT, padx=(0, 10))
        d_label.grid(row=1,column=0)        #pack(side=tk.LEFT , padx=(10, 0))
        d_entry.grid(row=1,column=1)                        #pack(side=tk.LEFT, padx=(0, 10))
        n_label.grid(row=2,column=0)                        #pack(side=tk.LEFT, padx=(10, 0))
        n_entry.grid(row=2,column=1)
    else:
        e_label.grid_forget()
        e_entry.grid_forget()
        n_label.grid_forget()
        n_entry.grid_forget()
        d_label.grid_forget()
        d_entry.grid_forget()
        
    if selected_option.get() == "Vigenere":
        vin_label.grid(row=1,column=0)
        vin_entry.grid(row=1,column=1)
        selected_input.set("Text")
    else:
        vin_label.grid_forget()
        vin_entry.grid_forget()
        
    if selected_option.get() == "3DES":
        des_label1.grid(row=1,column=0)
        des_entry1.grid(row=1,column=1)
        des_label2.grid(row=2,column=0)
        des_entry2.grid(row=2,column=1)
        des_label3.grid(row=3,column=0)
        des_entry3.grid(row=3,column=1)
    else:
        des_label1.grid_forget()
        des_entry1.grid_forget()
        des_label2.grid_forget()
        des_entry2.grid_forget()
        des_label3.grid_forget()
        des_entry3.grid_forget()

    if selected_option.get() == "AES":
        aes_label.grid(row=1,column=0)
        aes_entry.grid(row=1,column=1)
    else:
        aes_label.grid_forget()
        aes_entry.grid_forget()
        

def encrypt():
    #get input text entry
    input_text = input_entry.get().strip()
    
    #process based on selection
    if selected_option.get() == "Vigenere":
        try:
            vin_key = vin_entry.get()
        except ValueError:
            output_entry.delete(0, tk.END)
            output_entry.insert(0, "must enter key value")
            return
        
        if selected_mode.get() == "Decrypt":
            output_text = vin_decrypt(vin_key, input_text)
        else:
            output_text = vin_encrypt(vin_key, input_text)
   
    elif selected_option.get() == "RSA":
        #get e and n values
        
        if selected_mode.get() == "Encrypt":
            try:
                e_value = int(e_entry.get())
            except ValueError:
                output_entry.delete(0, tk.END)
                output_entry.insert(0, "must enter e value")
                return
        else:
            try:
                d_value = int(d_entry.get())
            except ValueError:
                output_entry.delete(0, tk.END)
                output_entry.insert(0, "must enter d value")
                return            
        try:
            n_value = int(n_entry.get())
        except ValueError:
            output_entry.delete(0, tk.END)
            output_entry.insert(0, "must enter n value")
            return
        
        if selected_mode.get() == "Encrypt":
            output_text = rsa_encrypt(input_text, e_value, n_value,selected_input.get())
        else:
            output_text = rsa_decrypt(input_text, d_value, n_value,selected_input.get())
    
    if selected_option.get() == "3DES":
        try:
            key1 = des_entry1.get()
            key2 = des_entry2.get()
            key3 = des_entry3.get()
        except ValueError:
            output_entry.delete(0, tk.END)
            output_entry.insert(0, "must enter all keys")
            return
        if selected_mode.get() == "Decrypt":
            output_text = tripleDecode(key1, key2, key3, input_text,selected_input.get())
        else:
            output_text = tripleEncode(key1, key2, key3, input_text,selected_input.get())
            
    output_entry.delete(0, tk.END)
    output_entry.insert(0, output_text)
    
    if selected_input.get() == "File":
        output_filename = filedialog.asksaveasfilename(defaultextension=".bin", filetypes=[("binary files", "*.bin")])
        if output_filename:
            with open(output_filename, "w") as file:
                file.write(output_text)
        

root = tk.Tk()
root.title("Encryption/Decryption")
root.geometry("1200x600")
root.config(bg="skyblue", padx=10,pady=10)



#label for text
#input_label = tk.Label(root, text="Input:", font=("Helvetica", 16))
#input_label.grid(row=0,column=0,padx=5,pady=5)
selected_input = tk.StringVar(root)
selected_input.set("Text") 
selected_input.trace("w", update_ui) 
input_menu = tk.OptionMenu(root, selected_input, "Text", "File", "Binary")
input_menu.grid(row=0, column=0 ,padx=5,pady=5)

#text entry
input_entry = tk.Entry(root, width=30)
input_entry.grid(row=0,column=1 ,padx=5,pady=5)

open_file_button = tk.Button(root, text='Open File', command=UploadAction)
#open_file_button.grid(row=3, column=0, padx=5, pady=5)

#dropdown to choose encryption alg
selected_option = tk.StringVar(root)
selected_option.set("Select Algorithm") 
selected_option.trace("w", update_ui) 
options_menu = tk.OptionMenu(root, selected_option, "Vigenere", "RSA", "3DES", "AES")
options_menu.grid(row=0, column=2 ,padx=5,pady=5)



# e, n, d value (initially hidden)
e_label = tk.Label(root, text="e value:",font =("Helvetica", 16))
e_entry = tk.Entry(root, width=3)

d_label = tk.Label(root, text="d value:",font =("Helvetica", 16))
d_entry = tk.Entry(root, width=3)

n_label = tk.Label(root, text="n value:",font =("Helvetica", 16))
n_entry = tk.Entry(root, width=3)



vin_label = tk.Label(root, text ="Vinegere Key",font =("Helvetica", 16))
vin_entry = tk.Entry(root, width = 10)

des_label1 = tk.Label(root, text ="Key 1",font =("Helvetica", 16))
des_entry1 = tk.Entry(root, width = 30)
des_label2 = tk.Label(root, text ="Key 2",font =("Helvetica", 16))
des_entry2 = tk.Entry(root, width = 30)
des_label3 = tk.Label(root, text ="Key 3",font =("Helvetica", 16))
des_entry3 = tk.Entry(root, width = 30)

aes_label = tk.Label(root, text ="AES Key",font =("Helvetica", 16))
aes_entry = tk.Entry(root, width = 30)

# Text entry widget for output
#output_entry = tk.Entry(frame, width=20)
#output_entry.pack(side=tk.LEFT, padx=(10, 0))
selected_mode = tk.StringVar(root)
selected_mode.set("Select Mode",) 
selected_mode.trace("w", update_ui) 
mode_options_menu = tk.OptionMenu(root, selected_mode, "Encrypt", "Decrypt")
mode_options_menu.grid(row=0, column=3 ,padx=5,pady=5)

process_button = tk.Button(root, text="Run Program", command=encrypt,font =("Helvetica", 16))
process_button.grid(row=0,column=4 ,padx=5,pady=5)


output_label = tk.Label(root, text = "Output",font =("Helvetica", 16))
output_label.grid(row=0, column=5 ,padx=5,pady=5)
output_entry = tk.Entry(root, width=30)
output_entry.grid(row=0,column=6 ,padx=5,pady=5)

# Start the applications
root.mainloop()
