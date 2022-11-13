from tkinter import *
import os
import tkinter as tk


def btn_clicked():
    class FitnessCalculator:
        def __init__(self):
            
            calculator=tk.Toplevel(win)
            calculator.title('Fitness Calculator')
            calculator.resizable(False,False)

            mainmenu=Menu(calculator,background='#76a9c1', fg='white')
            def About():
                print("Let me tell you About us \n")
                os.startfile("ABOUT.txt")
            def REC():
                print("Showing User Lists \n")
                os.startfile("RECORDS.txt")
            def Help():
                print("Happy to Help \n")
                os.startfile("HELP.txt")
                #f = open("Help.txt",'r')
                #print(f.read())
            def myfunc():
                print("HELLO")
            m1=Menu(mainmenu,tearoff=0,background='grey',fg='white')
            m1.add_command(label="New",command=myfunc)
            m1.add_command(label="Save",command=myfunc)
            m1.add_command(label="Open",command=REC)
            m1.add_separator()
            m1.add_command(label="Exit",command=calculator.destroy)
            calculator.config(menu=mainmenu)
            edit = Menu(mainmenu, tearoff = 0,background='grey',fg="white")
            mainmenu.add_cascade(label ='Edit', menu = edit)
            edit.add_command(label ='Cut', command = None)
            edit.add_command(label ='Copy', command = None)
            edit.add_command(label ='Paste', command = None)
            edit.add_command(label ='Select All', command = None)
            edit.add_separator()
            edit.add_command(label ='Find...', command = None)
            edit.add_command(label ='Find again', command = None)
            mainmenu.add_cascade(label="File",menu=m1)
            m2=Menu(mainmenu,tearoff=0,background='grey',fg="white")
            m2.add_command(label="About us",command=About)
            m2.add_separator()
            m2.add_command(label="Information",command=Help)
            calculator.config(menu=mainmenu)
            mainmenu.add_cascade(label="Help",menu=m2)
    

        #Name and Age Entry Fields 
            name=StringVar()
            age=IntVar()
            Label(calculator,text='Name : ',width=10).grid(row=0,column=1)
            Entry(calculator,width=25,relief='ridge',bd=2,textvariable=name).grid(row=0,column=2)
            Label(calculator,text='Age : ',width=10).grid(row=1,column=1)
            Entry(calculator,width=25,relief='ridge',bd=2,textvariable=age).grid(row=1,column=2)
         
        #The Gender Radio Button
            v=IntVar()
            Label(calculator,text='Gender : ').grid(row=2,column=1)
            Radiobutton(calculator,text='Male',variable=v,value=1).grid(row=2,column=2)
            Radiobutton(calculator,text='Female',variable=v,value=2).grid(row=2,column=4)
        
        #Generating the fields for Entry Fields
            fields=('Weight (Kg)','Height (Mts)','BP Low (Systolic) mm/Hg','BP High (Diastolic) mm/Hg','Pulse Rate','RBC Count (trillion Cells/L)','WBC Count (billions cells/L)','Platelets','HB','Uric Acid (mg/dL)','Cholestrol (mg/dL)')
            r=3
            entries=[]
            for field in fields:
                Label(calculator,text=field+' : ',width=30,bg='grey',fg='white').grid(row=r,column=1,sticky='NWSWSE')
                en=Entry(calculator,width=30,relief='ridge',bd=2)
                en.grid(row=r,column=2,sticky='NWSWSE')
                entries.append(en)
                r+=1
        #Report Label
            Label(calculator,text='Report Of',width=30,bg='black',fg='white').grid(row=14,column=1,sticky='NWSWSE') 
            Label(calculator,text='BMI (High/Medium/Low)',width=30,fg='black',bg='gainsboro',textvariable=name).grid(row=14,column=2,sticky='NWSWSE') 


        #Results TextVariables
            bmi_calculated=StringVar()
            bp_calc=StringVar()
            pulse_calulated=StringVar()
            cholestrol_calculated=StringVar()
            wbc_final=StringVar()
            rbc_final=StringVar()
            platelets_final=StringVar()
            uric_acid=StringVar()
            haemoglobin_calc=StringVar()

        #Final_Labels
            Label(calculator,text='BMI (High/Medium/Low)',width=30,bg='grey',fg='white').grid(row=15,column=1,sticky='NWSWSE')
            Label(calculator,text='BP (High/Medium/Low)',width=30,bg='grey',fg='white').grid(row=16,column=1,sticky='NWSWSE')
            Label(calculator,text='Pulse Rate (High/Medium/Low)',width=30,bg='grey',fg='white').grid(row=17,column=1,sticky='NWSWSE')
            Label(calculator,text='RBC Count (High/Medium/Low)',width=30,bg='grey',fg='white').grid(row=18,column=1,sticky='NWSWSE')
            Label(calculator,text='WBC Count (High/Medium/Low)',width=30,bg='grey',fg='white').grid(row=19,column=1,sticky='NWSWSE')
            Label(calculator,text='Platelets (High/Medium/Low)',width=30,bg='grey',fg='white').grid(row=20,column=1,sticky='NWSWSE')
            Label(calculator,text='HB (High/Medium/Low)',width=30,bg='grey',fg='white').grid(row=21,column=1,sticky='NWSWSE')
            Label(calculator,text='Uric Acid (High/Medium/Low)',width=30,bg='grey',fg='white').grid(row=22,column=1,sticky='NWSWSE')
            Label(calculator,text='Cholestrol (High/Medium/Low)',width=30,bg='grey',fg='white').grid(row=23,column=1,sticky='NWSWSE')


            Label(calculator,text='BMI (High/Medium/Low)',width=30,fg='black',bg='gainsboro',textvariable=bmi_calculated).grid(row=15,column=2,sticky='NWSWSE')
            Label(calculator,text='BP (High/Normal/Low)',width=30,fg='black',bg='gainsboro',textvariable=bp_calc).grid(row=16,column=2,sticky='NWSWSE')
            Label(calculator,text='Pulse Rate (High/Medium/Low)',width=30,bg='gainsboro',fg='black',textvariable=pulse_calulated).grid(row=17,column=2,sticky='NWSWSE')
            Label(calculator,text='RBC Count (High/Medium/Low)',width=30,bg='gainsboro',fg='black',textvariable=rbc_final).grid(row=18,column=2,sticky='NWSWSE')
            Label(calculator,text='WBC Count (High/Medium/Low)',width=30,bg='gainsboro',fg='black',textvariable=wbc_final).grid(row=19,column=2,sticky='NWSWSE')
            Label(calculator,text='Platelets (High/Medium/Low)',width=30,bg='gainsboro',fg='black',textvariable=platelets_final).grid(row=20,column=2,sticky='NWSWSE')
            Label(calculator,text='HB (High/Medium/Low)',width=30,fg='black',bg='gainsboro',textvariable=haemoglobin_calc).grid(row=21,column=2,sticky='NWSWSE')
            Label(calculator,text='Uric Acid (High/Medium/Low)',width=30,bg='gainsboro',fg='black',textvariable=uric_acid).grid(row=22,column=2,sticky='NWSWSE')
            Label(calculator,text='Cholestrol (High/Medium/Low)',width=30,bg='gainsboro',fg='black',textvariable=cholestrol_calculated).grid(row=23,column=2,sticky='NWSWSE')

    
        #making the bottom Label
            Label(calculator,bg='black',fg='white',width=30).grid(row=25,column=1,ipadx=5)       
            def get_entries():
                print(name.get())
                print(age.get())
                for entry in entries:
                    print(entry.get())


        
        #BMI calculator
            def calculate_bmi():
                weight=float(entries[0].get())
                height=float(entries[1].get())
                bmi=(weight/height)/height
                if bmi < 15:
                    value='Low'
                elif bmi >15 and bmi<20:
                    value='Medium'
                else:
                    value='High'
                bmi_calculated.set(value)
            

        #BP monitor
            def blood_pressure():
                bpl=float(entries[2].get())
                bph=float(entries[3].get())
                if bpl<120 and bph <80:
                    value='Normal'
                else:
                    value='High'
                bp_calc.set(value) 

            
        
        #Pulse Monitor
            def pulse_rate():
                pulse=int(entries[4].get())
                if pulse <72:
                    value='Low'
                elif pulse >72 and pulse <90:
                    value='Medium'
                else:
                    alue='High'
                pulse_calulated.set(value)


        #Blood Monitor
            def blood_monitor():
                rbc=float(entries[5].get())
                wbc=float(entries[6].get())
                platelets=float(entries[7].get())
                haemoglobin=float(entries[8].get())
           
           #calculating Haemoglobin Levels

                if haemoglobin <13:
                    h_value='Low'
                elif haemoglobin >13 and haemoglobin <16:
                    h_value='Medium'
                else:
                    h_value='High'
          # calculating rbc levels 

                if rbc < 4.32:
                    r_value='Low'
                if rbc > 4.32 and rbc < 5.72:
                    r_value='Medium'    
                else:
                    r_value='High'

        #calculating wbc values 
            
                if wbc<3:
                    w_value='Low'
                if wbc >3 and wbc<10:
                    w_value='Medium'
                else:
                    w_value='High'
        #calculating platelets levels 

                if platelets >150 and platelets <450:
                    p_value='Medium'
                elif platelets<150:
                    p_value='Low'
                else:
                    p_value='High'

        #setting Label Values 
                haemoglobin_calc.set(h_value) 
                rbc_final.set(r_value)
                wbc_final.set(w_value)
                platelets_final.set(p_value)


        #urine Monitor
            def urine_monitor():
                urine=float(entries[9].get())
                if urine <4:
                    value='Low'
                elif urine > 4 and urine <8.5:
                    value='Medium'
                else:
                    value='High'
                uric_acid.set(value)


        #get Cholestrol
            def get_cholestrol():
                cholestrol=float(entries[10].get())
                if cholestrol <200:
                    value='Low (Good)'
                elif cholestrol >200 and cholestrol<239:
                    value='Medium'
                else:
                    value='High'
                cholestrol_calculated.set(value)

            def show_results():
                name.set(name.get())
                get_entries()
                calculate_bmi()
                blood_pressure()
                pulse_rate()
                blood_monitor()
                urine_monitor()
                get_cholestrol()

            def Log():
                window2 = tk.Toplevel(calculator)
                window2.title("Log-IN / Sign-UP")

                window2.geometry("1000x600")
                window2.configure(bg = "#aaaaaa")
                canvas = Canvas(
                    window2,
                    bg = "#aaaaaa",
                    height = 600,
                    width = 1000,
                    bd = 0,
                    highlightthickness = 0,
                    relief = "ridge")
                canvas.place(x = 0, y = 0)

                background_img = PhotoImage(file = f"bg.png")
                background = canvas.create_image(
                    500.0, 300.0,
                    image=background_img)

                entry0_img = PhotoImage(file = f"img_textBox0.png")
                entry0_bg = canvas.create_image(
                    616.0, 314.5,
                    image = entry0_img)
                E0=StringVar()
                E1=StringVar()
                E2=StringVar()
                entry0 = Entry(window2,textvariable=E0,
                    bd = 0,
                    bg = "#76a9c1",
                    highlightthickness = 0)

                entry0.place(
                    x = 448, y = 284,
                    width = 336,
                    height = 59)

                entry1_img = PhotoImage(file = f"img_textBox1.png")
                entry1_bg = canvas.create_image(
                    616.0, 175.5,
                    image = entry1_img)

                entry1 = Entry(window2,textvariable=E1,
                    bd = 0,
                    bg = "#76a9c1",
                    highlightthickness = 0)

                entry1.place(
                    x = 448, y = 145,
                    width = 336,
                    height = 59)

                entry2_img = PhotoImage(file = f"img_textBox2.png")
                entry2_bg = canvas.create_image(
                    616.0, 452.5,
                    image = entry2_img)

                entry2 = Entry(window2,textvariable=E2,
                    bd = 0,
                    bg = "#76a9c1",
                    highlightthickness = 0)

                entry2.place(
                    x = 448, y = 422,
                    width = 336,
                    height = 59)

            
                def btn_clicked():
                    print(f"{E1.get(), E0.get(), E2.get()}")
                    with open("RECORDS.txt","a") as f:
                        f.write(f"{E1.get(), E0.get(), E2.get(), entries[0].get(), entries[1].get(), entries[2].get(), entries[3].get(), entries[4].get(), entries[5].get(), entries[6].get(), entries[7].get(), entries[8].get(), entries[9].get(), entries[9].get() }\n")
                     

                img0 = PhotoImage(file = f"0.png")
                b0 = Button(window2,
                    image = img0,
                    borderwidth = 0,
                    highlightthickness = 0,
                    cursor="Heart",
                    command = btn_clicked,
                    relief = "flat").place(
                    x = 839, y = 521,
                    width = 131,
                    height = 49)

        

                window2.resizable(True,True)
                window2.mainloop()

        #Button to Show the results of the report 
            Button(calculator,text="Show Report",relief='ridge',bg='grey',fg='white',bd=2,command=show_results).grid(row=14,column=4,ipadx=4)
            Button(calculator,text="Log-IN",relief='ridge',bg='grey',fg='white',bd=2,command=Log).grid(row=25,column=4,ipadx=4)
        #Initiating the GUI mainloop Instance (event loop)
            calculator.mainloop()




#calling the default constructor to create the GUI
    FitnessCalculator()


win = Tk()
win.title("Fitness Calculator")
win.geometry("496x700")
win.configure(bg = "#ffffff")
canvas = Canvas(
    win,
    bg = "#ffffff",
    height = 700,
    width = 496,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    247.5, 298.0,
    image=background_img)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(win,
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    cursor="Heart",
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 17, y = 621,
    width = 468,
    height = 65)

win.resizable(False, False)
win.mainloop()
