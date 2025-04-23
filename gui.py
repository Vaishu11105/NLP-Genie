from tkinter import *
from mydb import Database
from tkinter import messagebox
import os

import nlpcloud
from dotenv import load_dotenv
load_dotenv()

class NLPApp:

    def __init__(self):
        self.db = Database()
        self.root = Tk()
        self.root.title("GUI APP")
       
        self.root.configure(bg='#17202a')
        self.login_gui()
        # self.sentiment_gui()

        self.root.mainloop()

    def login_gui(self):
        self.clear()
        self.root.geometry("1100x700")
        title = Label(text="PROJECT")
        title.pack(pady=(15,70))
        title.configure(bg='#17202a',fg='#f4f6f7',font=('timesnewroman',30,'bold'))

        email = Label(text="Enter Email: ")
        email.pack(pady=(15,15))
        email.configure(bg='#17202a',fg='#f4f6f7',font=('timesnewroman',15,'bold'))

        self.email_input = Entry(width=40)
        self.email_input.pack(pady=(10,10),ipady=8)

        password = Label(text="Enter Password: ")
        password.pack(pady=(15,15))
        password.configure(bg='#17202a',fg='#f4f6f7',font=('timesnewroman',15,'bold'))

        self.password_input = Entry(width=40,show="$")
        self.password_input.pack(pady=(10,30),ipady=8)

        login_button = Button(text="Login",command=self.perform_login)
        login_button.pack(pady=10)
        login_button.configure(bg='#17202a',fg='#f4f6f7',font=('timesnewroman',15,'bold'))

        footer = Label(text="Not registered ? Do it now ASAP!!")
        footer.pack(pady=(70,15))
        footer.configure(bg='#17202a',fg='#f4f6f7',font=('timesnewroman',15,'bold'))

        reg_button = Button(text="Register",command=self.register_gui)
        reg_button.pack(pady=10)
        reg_button.configure(bg='#17202a',fg='#f4f6f7',font=('timesnewroman',15,'bold'))

    def register_gui(self):
        self.clear()

        title = Label(text="REGISTRATION PAGE")
        title.pack(pady=(10,40))
        title.configure(bg='#17202a',fg='#f4f6f7',font=('timesnewroman',30,'bold'))

        email = Label(text="Enter Email: ")
        email.pack(pady=(10,10))
        email.configure(bg='#17202a',fg='#f4f6f7',font=('timesnewroman',15,'bold'))

        self.email_input = Entry(width=40)
        self.email_input.pack(pady=(10,10),ipady=8)

        password = Label(text="Enter Password: ")
        password.pack(pady=(10,10))
        password.configure(bg='#17202a',fg='#f4f6f7',font=('timesnewroman',15,'bold'))

        self.password_input = Entry(width=40,show="$")
        self.password_input.pack(pady=(10,10),ipady=8)

        confirm_password = Label(text="Confirm Password: ")
        confirm_password.pack(pady=(10,10))
        confirm_password.configure(bg='#17202a',fg='#f4f6f7',font=('timesnewroman',15,'bold'))

        self.confirm_password_input = Entry(width=40,show="$")
        self.confirm_password_input.pack(pady=(10,30),ipady=8)

        reg_button = Button(text="Register",command=self.perform_registration)
        reg_button.pack(pady=10)
        reg_button.configure(bg='#17202a',fg='#f4f6f7',font=('timesnewroman',15,'bold'))

        footer = Label(text="After registration, click here to login!")
        footer.pack(pady=(50,10))
        footer.configure(bg='#17202a',fg='#f4f6f7',font=('timesnewroman',15,'bold'))

        login_button = Button(text="Login",command=self.login_gui)
        login_button.pack(pady=10)
        login_button.configure(bg='#17202a',fg='#f4f6f7',font=('timesnewroman',15,'bold'))

    def perform_registration(self):
        email = self.email_input.get()
        password = self.password_input.get()
        confirm_password = self.confirm_password_input.get()

        if(email=="" or password=="" or confirm_password==""):
            messagebox.showinfo(message="Please do not leave the box empty\n Enter all the details correctly! ")
        elif(password!=confirm_password):
            messagebox.showinfo(message="Wrong password")    
        else:
            response = self.db.add_data(email,password)
            if response:
                messagebox.showinfo('Success','Registration successful !! Login now !!')
            else:
                messagebox.showinfo('Error','Email already exists') 

    def perform_login(self):
        email = self.email_input.get()
        password = self.password_input.get()

        if(email=="" or password==""):
            messagebox.showinfo(message="Fill all details")
        else:
            isValid = self.db.validate_credentials(email,password)

            if isValid:
                messagebox.showinfo(message="Login Successful!!")
                self.home_gui()
            else:
                messagebox.showinfo(message="You are a new user\nRegister first")    


    def home_gui(self):
        self.clear()
        self.root.geometry("1100x700")
        title = Label(text="NLPApp")
        title.pack(pady=(10,40))
        title.configure(bg='#17202a',fg='#f4f6f7',font=('timesnewroman',40,'bold'))

        sentiment_button = Button(text="Sentiment Analysis", command = self.sentiment_gui)
        sentiment_button.pack(pady=(35, 25))
        sentiment_button.configure(width = 30,height= 5,bg='#17202a',fg='#f4f6f7',font=('timesnewroman',15,'bold'))

        ner_button = Button(text="Named Entity Recognition", command = self.ner_gui)
        ner_button.pack(pady=(25, 25))
        ner_button.configure(width = 30,height= 5,bg='#17202a',fg='#f4f6f7',font=('timesnewroman',15,'bold'))

        paraphrasing_button = Button(text="Paraphrase", command = self.paraphrasing_gui)
        paraphrasing_button.pack(pady=(25, 35))
        paraphrasing_button.configure(width = 30,height= 5,bg='#17202a',fg='#f4f6f7',font=('timesnewroman',15,'bold'))


    def sentiment_gui(self):
        self.clear()

        self.root.geometry("500x700")

        title = Label(text="NLPApp")
        title.pack(pady=(10,20))
        title.configure(bg='#17202a',fg='#f4f6f7',font=('timesnewroman',40,'bold'))

        title2 = Label(text="Sentiment Analysis")
        title2.pack(pady=(7,15))
        title2.configure(bg='#17202a',fg='#f4f6f7',font=('timesnewroman',30,'bold'))

        label1 = Label(self.root, text='Enter the text')
        label1.pack(pady=(7, 15))
        label1.configure(bg='#17202a',fg='#f4f6f7',font=('timesnewroman',20,'bold'))

        self.sentiment_input = Text(self.root, width = 50, height = 15)
        self.sentiment_input.pack()

        sentiment_button = Button(text="Analyse Sentiment",command=self.perform_sentiment)
        sentiment_button.pack(pady=(15, 15))
        sentiment_button.configure(width = 20,height = 2,bg='#17202a',fg='#f4f6f7',font=('timesnewroman',10,'bold'))

        go_back_button = Button(text="Go Back To NLPApp",command=self.home_gui)
        go_back_button.pack(pady=(10, 10))
        go_back_button.configure(width = 15, height =3,bg='#17202a',fg='#f4f6f7',font=('timesnewroman',6,'bold'))

        go_to_login_button = Button(text="Go to Login Page",command=self.login_gui)
        go_to_login_button.pack(pady=(10,10))
        go_to_login_button.configure(width = 15, height =3,bg='#17202a',fg='#f4f6f7',font=('timesnewroman',6,'bold'))

    def perform_sentiment(self):

        para = self.sentiment_input.get("1.0","end-1c")

        if(para==""):
            messagebox.showinfo(message="Paragraph cannot be empty")   
        else:
            self.clear()
            api_key = os.getenv("API_KEY")

            client = nlpcloud.Client("finetuned-llama-3-70b", api_key, gpu=True)
            result = client.sentiment(para, target="NLP Cloud")

            val = result['scored_labels']


            sentiment_box = Text(self.root, height = 15, width = 50)
            sentiment_box.pack()

            for i in val:
                sentiment_box.insert(END,"{}:{}\n".format(i['label'],i['score']))

            back_button = Button(text="Go Back",command=self.sentiment_gui)
            back_button.pack(pady=(10, 10))
            back_button.configure(width = 15, height =3,bg='#17202a',fg='#f4f6f7',font=('timesnewroman',6,'bold'))    


            


    

    def ner_gui(self):
        self.clear()

        self.root.geometry("500x700")

        title = Label(text="NLPApp")
        title.pack(pady=(10,20))
        title.configure(bg='#17202a',fg='#f4f6f7',font=('timesnewroman',40,'bold'))

        title2 = Label(text="Named Entity Recognition")
        title2.pack(pady=(7,15))
        title2.configure(bg='#17202a',fg='#f4f6f7',font=('timesnewroman',30,'bold'))

        label1 = Label(self.root, text='Enter the text')
        label1.pack(pady=(6, 14))
        label1.configure(bg='#17202a',fg='#f4f6f7',font=('timesnewroman',20,'bold'))

        self.ner_input = Text(self.root, width = 50, height = 10)
        self.ner_input.pack()

        label2 = Label(self.root, text='Enter the entity which you want to search')
        label2.pack(pady=(6, 14))
        label2.configure(bg='#17202a',fg='#f4f6f7',font=('timesnewroman',20,'bold'))

        self.entity_input = Text(self.root, width = 50, height = 5)
        self.entity_input.pack()

        ner_button = Button(text="Analyse NER",command=self.perform_ner)
        ner_button.pack(pady=(15, 15))
        ner_button.configure(width = 20,height = 2,bg='#17202a',fg='#f4f6f7',font=('timesnewroman',10,'bold'))

        go_back_button = Button(text="Go Back To NLPApp",command=self.home_gui)
        go_back_button.pack(pady=(10, 10))
        go_back_button.configure(width = 15, height =3,bg='#17202a',fg='#f4f6f7',font=('timesnewroman',6,'bold'))

        go_to_login_button = Button(text="Go to Login Page",command=self.login_gui)
        go_to_login_button.pack(pady=(10,10))
        go_to_login_button.configure(width = 15, height =3,bg='#17202a',fg='#f4f6f7',font=('timesnewroman',6,'bold'))


    def perform_ner(self):
        para = self.ner_input.get("1.0", "end-1c")
        entity_type = self.entity_input.get("1.0", "end-1c")

        if para.strip() == "" or entity_type.strip() == "":
            messagebox.showinfo(message="Both fields must be filled.")
        else:
            self.clear()
            api_key = os.getenv("API_KEY")

            client = nlpcloud.Client("finetuned-llama-3-70b", api_key, gpu=True)
            result = client.entities(para, searched_entity=entity_type)

            val = result['entities']

            result_box = Text(self.root, height=15, width=70)
            result_box.pack()

            if val:
                for i in val:
                    result_box.insert(END, f"{i['text']} - {i['type']}\n")
            else:
                result_box.insert(END, "No matching entities found.")


            back_button = Button(self.root, text="Go Back", command=self.ner_gui)
            back_button.pack(pady=(10, 10))
            back_button.configure(width=15, height=2, bg='#17202a', fg='#f4f6f7', font=('timesnewroman', 10, 'bold'))



    def paraphrasing_gui(self):
        self.clear()

        self.root.geometry("500x700")

        title = Label(text="NLPApp")
        title.pack(pady=(10,20))
        title.configure(bg='#17202a',fg='#f4f6f7',font=('timesnewroman',40,'bold'))

        title2 = Label(text="Paraphrasing")
        title2.pack(pady=(7,15))
        title2.configure(bg='#17202a',fg='#f4f6f7',font=('timesnewroman',30,'bold'))

        label1 = Label(self.root, text='Enter the text')
        label1.pack(pady=(7, 15))
        label1.configure(bg='#17202a',fg='#f4f6f7',font=('timesnewroman',20,'bold'))

        self.paraphrasing_input = Text(self.root, width = 50, height = 15)
        self.paraphrasing_input.pack()

        para_button = Button(text="Paraphrase",command=self.perform_paraphrasing)
        para_button.pack(pady=(15, 15))
        para_button.configure(width = 20,height = 2,bg='#17202a',fg='#f4f6f7',font=('timesnewroman',10,'bold'))

        go_back_button = Button(text="Go Back To NLPApp",command=self.home_gui)
        go_back_button.pack(pady=(10, 10))
        go_back_button.configure(width = 15, height =3,bg='#17202a',fg='#f4f6f7',font=('timesnewroman',6,'bold'))

        go_to_login_button = Button(text="Go to Login Page",command=self.login_gui)
        go_to_login_button.pack(pady=(10,10))
        go_to_login_button.configure(width = 15, height =3,bg='#17202a',fg='#f4f6f7',font=('timesnewroman',6,'bold'))


    def perform_paraphrasing(self):
        para = self.paraphrasing_input.get("1.0","end-1c")

        if(para==""):
            messagebox.showinfo(message="Paragraph cannot be empty")   
        else:
            self.clear()
            api_key = os.getenv("API_KEY")
            client = nlpcloud.Client("finetuned-llama-3-70b",api_key, gpu=True)
            result=client.paraphrasing(para)

            para_box = Text(self.root,height = 15, width=50)
            para_box.pack()
            val = result['paraphrased_text']
            para_box.insert(END,val)

            back_button = Button(self.root, text="Go Back", command=self.paraphrasing_gui)
            back_button.pack(pady=(10, 10))
            back_button.configure(width=15, height=2, bg='#17202a', fg='#f4f6f7', font=('timesnewroman', 10, 'bold'))
            
        






    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()








ob = NLPApp()        