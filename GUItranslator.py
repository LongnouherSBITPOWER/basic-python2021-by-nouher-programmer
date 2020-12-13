#GUItranslator.py
from tkinter import *
#จากไลบรารีชือ tkinter,*คือให้ถึงความสามารถหลักทั้งหมด
from tkinter import ttk #ttk is theme of tk
###---------Google Translate------------
from googletrans import Translator
translator = Translator()#สร้างฟังสชันเเปลพาษา

GUI = Tk() #สร้างหน้าต่างหลัก
GUI.geometry('500x300') #กว้าง X สูง
GUI.title('ໂປຣເເກຣມເເປພາສາໂດຍ SB IT POWER')#การใช้หัวข้อของโปณเเกรมหลืชื่อโปรเเกรม
#-----config------
FONT = ('phetsarath ot',15)
#-----Label------
L = ttk.Label(GUI,text='ກະລຸນາໃສ່ຄຳສັບທີ່ຕ້ອງກັນເເປ',font=FONT)
L.pack()

#-----Entry(ช่องกรอกข้อความ)-----
v_vocab = StringVar()#กล่องเก็บข้อความ
E1 = ttk.Entry(GUI,textvariable = v_vocab,font=FONT,width=40)
E1.pack(pady=20)


#-----Button(ปุ่มเเปล)-----
def Translate():
    vocab = v_vocab.get()#.getคือให้เเสดวผลออกมา
    meaning = translator.translate(vocab,dest='lo')
    print(vocab + ':' + meaning.text)
    print(meaning.pronunciation)
    v_result.set(vocab + ':' + meaning.text)
    
B1 = ttk.Button(GUI,text='Translate',command=Translate)#สร้างปุ่มขื้้นมา
B1.pack(ipadx=20,ipady=10)#show ปุ่มขื้นมาวางจากบนลงล่าง

#-----Label------
L = ttk.Label(GUI,text='ຄຳເເປ',font=FONT)
L.pack()
#-------Result-----
v_result = StringVar()#นี้คือกล่องสำหรับเก็บคำเเปล
FONT2 = ('phetsarath ot',15)
R1 = ttk.Label(GUI,textvariable=v_result,font=FONT2,foreground='green')
R1.pack()
GUI.mainloop() #ทำให้โปรเเกรมรันได้ตหลอเวลาจนกว่าจะปิด
