from tkinter import *
import cv2
from numpy import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
import os
from stegano import lsb

dict="aBb!@R#.CQcZdVeOfYgP)&Sh,]i-Aj[k+T=D_}lm%U^'nEo{p:qF\\*(;r|WGs<KH>tuXvLJw?~MxyNz$"+'"'+" "

print(dict)

def encrypt(msg, key):
    try:
        encmsg = ""
        for i in msg:
            loc = key + dict.index(i)
            loc %= 82
            encmsg += dict[loc]
        print(encmsg)
        return encmsg
    except Exception as e:
        print(f"Error: {e}")



def decrypt(c, m):
    try:
        decmsg = ""
        for i in c:
            if i in dict:
                loc = dict.index(i) - m
                loc = (loc + len(dict)) % len(dict)
                decmsg += dict[loc]
            else:
                # Append characters not found in dict unchanged
                decmsg += i

        # print("here's your msg->", decmsg)
        return decmsg
    except Exception as e:
        print(f"Error: {e}")

def Rndmkeygnrtr():
    key= list(dict)
    random.shuffle(key)
    return (''.join(key))


def encrypt2(x,ky):
    try:
        encmsg=""
        charsA=dict
        charsB=ky
        for i in x:
            index=charsA.find(i)
            encmsg+=charsB[index]
        print('\nencryption is complete')
        print('encrypted text is->',encmsg)
        return encmsg
    except Exception as e:
        print(f"Error: {e}")

def decrypt2(x,h) :
    try:
        dcmsg=""
        charsA = dict
        charsB = h
        charsA,charsB=charsB,charsA
        for i in x:
            index = charsA.find(i)
            dcmsg += charsB[index]
        print('\ndecryption is complete')
        print("decrypted text is->",dcmsg)
        return dcmsg
    except Exception as e:
        print("error is:",e)
def getval():
    try:
        print(f"msg is {msg.get()}")
        print(f"key is {key.get()}")
        x = msg.get()
        y = key.get()
        if y!=0:
           z= encrypt(x,y)
           return z
        if y==0:
            fout = open("key2.txt", 'w')
            key2 = Rndmkeygnrtr()
            fout.write(key2)
            # ky=fout.read()
            print("ky is",key2)
            z=encrypt2(x,key2)
            return z
    except Exception as e:
        print(f"Error: {e}")


def add_one_to_bits(image):
    try:
        # Add 1 to each binary bit of each pixel
        noisy_image = cv2.bitwise_not(image)
        return noisy_image
    except Exception as e:
        print(f"Error: {e}")



def retrieve_original(image):
    try:
        # Retrieve the original image by applying the same operation
        original_image = cv2.bitwise_not(image)
        return original_image
    except Exception as e:
        print(f"Error: {e}")


def noise():
    try:
        # Load an image from file
        image_path = 'hidden.png'
        original_image = cv2.imread(image_path)
        # cv2.imshow('original_image', original_image)
        # Add 1 to each binary bit of each pixel in the image
        noisy_image = add_one_to_bits(original_image)
        # cv2.imshow('noisy_image', noisy_image)
        # Display the noisy images
        cv2.imwrite("noised_image.png", noisy_image)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        input_image_path = "noised_image.png"
        compressed_image_path = "compressed_image.png"
        compress_image(input_image_path, compressed_image_path)
    except Exception as e:
        print(f"Error: {e}")

def denoise():
    try:
        image_path = 'decompressed_image.png'
        noisy_image = cv2.imread(image_path)
        # cv2.imshow('noised', noisy_image)
        # Retrieve the original image from the noisy image
        retrieved_image = retrieve_original(noisy_image)

        # Display the retrieved image
        # cv2.imshow('Retrieved Image', retrieved_image)
        cv2.imwrite("retrived_image.png", retrieved_image)
        # cv2.waitKey(0)
        Show()
        cv2.destroyAllWindows()
    except Exception as e:
        print(f"Error: {e}")


def rootclose():
    try:
        root.quit()
        fin.quit()
    except Exception as e:
        print(f"Error: {e}")

def compress_image(input_path, output_path, quality=30):
    try:
        # Open the image file
        img = Image.open(input_path)

        # Save the compressed image
        img.save(output_path, quality=quality)

        print(f"Image compressed successfully and saved to {output_path}")
    except Exception as e:
        print(f"Compression Error: {e}")

def decompress_image():
    try:
        input_path = "compressed_image.png"

        # Open the compressed image file
        img = Image.open(input_path)
        output_path = "decompressed_image.png"

        # Save the decompressed image
        img.save(output_path)

        print(f"Image decompressed successfully and saved to {output_path}")
        denoise()
    except Exception as e:
        print(f"Decompression Error: {e}")


win = Tk()

win.geometry("800x300")
usr = Label(win, text='enter your msg')
psd = Label(win, text='key')
usr.grid(row=0, column=1)
psd.grid(row=1, column=1)

msg = StringVar()
key = IntVar()

msgentry = Entry(win, textvariable=msg)
keyentry = Entry(win, textvariable=key)

msgentry.grid(row=0, column=10)
keyentry.grid(row=1, column=10)
b = Button(win, text='submit')
b.grid(row=2, column=1)

b = Button(win, text='close', command=win.destroy)
b.grid(row=2, column=2)
win.mainloop()


# functions
def showimage():
    try:
        global filename
        filename=filedialog.askopenfilename(initialdir=os.getcwd(),title="select image file",
                                            filetype=(("JPG file","*.jpg"),("PNG file","*.png"),("all file","*.*")))
        img=Image.open(filename)
        img=ImageTk.PhotoImage(img)
        lbl.configure(image=img,width=250,height=250)
        lbl.image=img
    except Exception as e:
        print(f"Error: {e}")


def Hide():
    try:
        global secret
        message = text1.get(1.0, END)
        secret = lsb.hide(str(filename), message)
    except Exception as e:
        print(f"Error: {e}")


def Show():
    try:

        clear_message = lsb.reveal("retrived_image.png")

        # Get the key from the key entry
        m = key.get()
        # Update the text area with the revealed and decrypted message
        text1.delete(1.0, END)
        text1.insert(1.0, clear_message)

        return clear_message
    except Exception as e:
        print(f"Error: {e}")

def save():
    try:
        s= secret.save("hidden.png")
        noise()

    except Exception as e:
        print(f"Error: {e}")

# 2nd interface

root = Tk()
root.title("steganography-hide your text !")
root.geometry("700x500+150+170")
root.resizable(False, False)
root.configure(bg="grey")
# icon
imageicon = PhotoImage(file="sec.png")
root.iconphoto(False, imageicon)

# logo
logo = PhotoImage(file="padlock.png")
Label(root, image=logo, bg="black", relief=RAISED).place(x=10, y=10)
Label(root, text=" Hiding Text", bg="blue", fg="red", font="arial 25 italic bold").place(x=250, y=10)

# 1st frame
f = Frame(root, bd=3, bg='black', width=340, height=280, relief=GROOVE)
f.place(x=10, y=140)
lbl = Label(f, bg="black")
lbl.place(x=40, y=10)

# 2nd frame
frame2 = Frame(root, bd=3, width=340, height=280, bg="white", relief=GROOVE)
frame2.place(x=350, y=140)
text1 = Text(frame2, font="arial 18", fg="black", relief=GROOVE)
text1.place(x=0, y=0)
if len(msg.get()) != 0 :
    x = str(getval())
    text1.insert(1.0, x)
# text1.config(state= DISABLED)
scrollbar1 = Scrollbar(frame2)
scrollbar1.place(x=320, y=0, height=280)
0scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

# third frame
frame3 = Frame(root, bd=3, bg="#2f4155", width=300, height=80, relief=GROOVE)
frame3.place(x=30, y=420)
Button(frame3, text="Open Image", width=10, height=1, font="arial 11 bold", command=showimage).place(x=20, y=30)
Button(frame3, text="Save Image", width=10, height=1, font="arial 11 bold", command=save).place(x=180, y=30)
Label(frame3, text="Picture,Image,Photo File", bg="#2f4155", fg="yellow").place(x=20, y=5)

# forth frame
frame4 = Frame(root, bd=3, bg="#2f4155", width=300, height=80, relief=GROOVE)
frame4.place(x=370, y=420)
Button(frame4, text="Hide Data", width=10, height=1, font="arial 11 bold", command=Hide).place(x=20, y=30)
Button(frame4, text="Show Data", width=10, height=1, font="arial 11 bold", command=decompress_image).place(x=180, y=30)

Label(frame4, text="Picture,Image,Photo File", bg="#2f4155", fg="yellow").place(x=20, y=5)

Button(root, text="Decrypt Data", width=10, height=1, font="arial 11 bold", command=rootclose).place(x=250, y=90)

root.mainloop()



#third frame
fin=Tk()
fin.geometry("700x600")
fin.title("Decryption...")
text4 = Text(fin, font="arial 18", fg="#66FF00",bg="black" ,relief=GROOVE)
text4.place(x=0, y=0)
encrypted_message = Show()
m = key.get()

if m!=0:
    dec = decrypt(encrypted_message, m)
if m==0:
    try:
        k = open("key2.txt", "r")
        h = k.read()
        dec = decrypt2(encrypted_message,h)
    except Exception as e:
        print("error is:", e)


text4.insert(1.5,f'your encrypted msg is ->{encrypted_message}')
text4.insert(2.5,f'\nyour decrypted msg is ->{dec}')
Button(fin, text="Thank You", width=10, height=1, font="arial 11 bold", command=rootclose).place(x=300, y=450)
fin.mainloop()