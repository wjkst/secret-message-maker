from tkinter import messagebox, simpledialog, Tk
from random import choice

def is_even(number):
    return number % 2 == 0

def receive_even_letters(message):
    even_letters = []
    for counter in range(0 ,len(message)):
        if is_even(counter):
            even_letters.append(message[counter])
    return even_letters

def receive_odd_letters(message):
    odd_letters = []
    for counter in range(0, len(message)):
        if not is_even(counter):
            odd_letters.append(message[counter])
    return odd_letters

def change_letters(message):
    letter_list = []
    if not is_even(len(message)):
        message = message + 'x'
    even_letters = receive_even_letters(message)
    odd_letters = receive_even_letters(message)
    for counter in range(0, int(len(message)/2)):
        letter_list.append(odd_letters[counter])
        letter_list.append(even_letters[counter])
    new_message = ''.join(letter_list)
    return new_message

def encoding(message):
    encoded_list =[]
    false_letters = ['a', 'b', 'c', 'd', 'e']
    for counter in range(0, len(message)):
        encoded_list.append(message[counter])
        encoded_list.append(choice(false_letters))
    new_message = ''.join(encoded_list)
    return new_message

def decode(message):
    even_letters = receive_even_letters(message)
    new_message = ''.join(even_letters)
    return new_message

def receive_task():
    task = simpledialog.askstring('task', 'Do you want to encrypt or decrypt?')
    return task
def receive_message():
    message = simpledialog.askstring('message', 'enter the secret message: ')
    return message

root = Tk()

while True:
    task = receive_task()
    if task == 'encrypt':
        message = receive_message()
        encrypted = encoding(message)
        messagebox.showinfo('cipher text for the secret message is: ', encrypted)
    elif task == 'decrypt':
        message = receive_message()
        decrypted = decode(message)
        messagebox.showinfo('plain text for the secret message is: ', decrypted)
    else:
        break
root.mainloop
