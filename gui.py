import tkinter as tk
##############
# ENCRYPTION/DECRYPTION ALGORITHMS
###############
def rsa_encrypt(plain, e, n):
    encrypted = []
    for num in plain: 
        encrypted.append(str(int(num)**e%n))

    return("".join(encrypted))



def update_ui(*args):
    # change available options based on selection
    if selected_option.get() == "RSA":
        e_label.pack(side=tk.LEFT , padx=(10, 0))
        e_entry.pack(side=tk.LEFT, padx=(0, 10))
        n_label.pack(side=tk.LEFT, padx=(10, 0))
        n_entry.pack(side=tk.LEFT, padx=(0, 10))

    else:
        e_label.pack_forget()
        e_entry.pack_forget()
        n_label.pack_forget()
        n_entry.pack_forget()

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
        try:
            e_value = int(e_entry.get())
        except ValueError:
            output_entry.delete(0, tk.END)
            output_entry.insert(0, "must enter e value")
            return
        try:
            n_value = int(n_entry.get())
        except ValueError:
            output_entry.delete(0, tk.END)
            output_entry.insert(0, "must enter e value")
            return
        
        output_text = rsa_encrypt(input_text, e_value, n_value)
        output_entry.delete(0, tk.END)
        output_entry.insert(0, output_text)
        

root = tk.Tk()
root.title("Encryption/Decryption")

#main frame
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

#label for text
input_label = tk.Label(frame, text="Enter Plain Text:")
input_label.pack(side=tk.LEFT, padx=(0, 10))

#text entry
input_entry = tk.Entry(frame, width=20)
input_entry.pack(side=tk.LEFT)

#dropdown to choose encryption alg
selected_option = tk.StringVar(frame)
selected_option.set("Vigenere")  # set default value
selected_option.trace("w", update_ui)  # Trace changes to this variable
options_menu = tk.OptionMenu(frame, selected_option, "Vigenere", "RSA")
options_menu.pack(side=tk.LEFT, padx=(10, 0))

#trigger encryption
#process_button = tk.Button(frame, text="encrypt", command=encrypt)
#process_button.pack(side=tk.LEFT, padx=(10, 0))

# e, n value (initially hidden)
e_label = tk.Label(frame, text="e value:")
e_entry = tk.Entry(frame, width=3)
n_label = tk.Label(frame, text="n value:")
n_entry = tk.Entry(frame, width=3)

# Text entry widget for output
#output_entry = tk.Entry(frame, width=20)
#output_entry.pack(side=tk.LEFT, padx=(10, 0))

process_button = tk.Button(frame, text="encrypt", command=encrypt)
process_button.pack(side=tk.LEFT, padx=(10, 0))

output_entry = tk.Entry(frame, width=20)
output_entry.pack(side=tk.LEFT, padx=(10, 0))

# Start the application
root.mainloop()