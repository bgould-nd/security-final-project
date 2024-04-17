import tkinter as tk
from tkinter import filedialog
##############
# ENCRYPTION/DECRYPTION ALGORITHMS
###############

def UploadAction(event=None):
    filename = filedialog.askopenfilename()
    print('Selected:', filename)

def rsa_encrypt(plain, e, n):
    encrypted = []
    for num in plain: 
        encrypted.append(str(int(num)**e%n))

    return("".join(encrypted))


def update_ui(*args):
    # change available options based on selection
    if selected_input.get() == "Text":
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
        
    if selected_option.get() == "Vigenere":
        vin_label.grid(row=1,column=0)
        vin_entry.grid(row=1,column=1)
    else:
        vin_label.grid_forget()
        vin_entry.grid_forget()
        
    if selected_option.get() == "3DES":
        des_label.grid(row=1,column=0)
        des_entry.grid(row=1,column=1)
    else:
        des_label.grid_forget()
        des_entry.grid_forget()

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
        #to be implmented: currently just outputs text
        output_entry.delete(0, tk.END)
        output_entry.insert(0, input_text)
   
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
            output_text = rsa_encrypt(input_text, e_value, n_value)
        #else:
         #   output_text = rsa_decrypt(input_text, d_value, n_value)
        output_entry.delete(0, tk.END)
        output_entry.insert(0, output_text)
        

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
input_menu = tk.OptionMenu(root, selected_input, "Text", "File")
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

des_label = tk.Label(root, text ="DES Key",font =("Helvetica", 16))
des_entry = tk.Entry(root, width = 10)

aes_label = tk.Label(root, text ="AES Key",font =("Helvetica", 16))
aes_entry = tk.Entry(root, width = 10)

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
