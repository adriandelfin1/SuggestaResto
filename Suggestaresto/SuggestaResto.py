import tkinter as intro
window = intro.Tk()
window.title('SUGGESTARESTO')
window.geometry('400x350')
window.configure(bg='plum3')

intro.Label(window, bg='pink', fg='purple', width=50, height=1, text='Hello, I know you have a hard time picking which ').pack()
intro.Label(window, bg='pink', fg='purple', width=50, height=1, text='restaurant to go to when you want to eat. So, I made').pack()
intro.Label(window, bg='pink', fg='purple', width=50, height=1, text='this for you to help you decide. This is a restaurant').pack()
intro.Label(window, bg='pink', fg='purple', width=50, height=1, text='suggestor that knows all your favorite restaurants, from').pack()
intro.Label(window, bg='pink', fg='purple', width=50, height=1, text='all your favorite cuisines. Whenever you are ready, click').pack()
intro.Label(window, bg='pink', fg='purple', width=50, height=1, text='the button below to have a restaurant suggested to you.').pack()


def main():
    import tkinter as res

    window = res.Tk()
    window.title('Restaurant Suggestor')
    window.geometry('400x350')
    window.configure(bg='plum3')
    res.Label(window, bg='pink', fg='purple', width=100, text='What Kind of Food do you want').pack() 

    def chi_res():
        import random
        with open('chi_res_file.txt', 'r') as file:
            data = file.read()
            words = data.split('\n')
        word_pos = random.randint(0, len(words)-1)
        file.close()
        return(words[word_pos])

    def fil_res():
        import random
        with open('fil_res_file.txt', 'r') as file:
            data = file.read()
            words = data.split('\n')
        word_pos = random.randint(0, len(words)-1)
        file.close()
        return(words[word_pos])            
        
        
    def ind_res():
        import random
        with open('ind_res_file.txt', 'r') as file:
            data = file.read()
            words = data.split('\n')
        word_pos = random.randint(0, len(words)-1)
        file.close()
        return(words[word_pos])

    def jap_res():
        import random
        with open('jap_res_file.txt', 'r') as file:
            data = file.read()
            words = data.split('\n')
        word_pos = random.randint(0, len(words)-1)
        file.close()
        return(words[word_pos])

    def kor_res():
        import random
        with open('kor_res_file.txt', 'r') as file:
            data = file.read()
            words = data.split('\n')
        word_pos = random.randint(0, len(words)-1)
        file.close()
        return(words[word_pos])

    def vie_res():
        import random
        with open('vie_res_file.txt', 'r') as file:
            data = file.read()
            words = data.split('\n')
        word_pos = random.randint(0, len(words)-1)
        file.close()
        return(words[word_pos])

    def mex_res():
        import random
        with open('mex_res_file.txt', 'r') as file:
            data = file.read()
            words = data.split('\n')
        word_pos = random.randint(0, len(words)-1)
        file.close()
        return(words[word_pos])

    def tha_res():
        import random
        with open('tha_res_file.txt', 'r') as file:
            data = file.read()
            words = data.split('\n')
        word_pos = random.randint(0, len(words)-1)
        return(words[word_pos])
        file.close()

    def fas_res():
        import random
        with open('fas_res_file.txt', 'r') as file:
            data = file.read()
            words = data.split('\n')
        word_pos = random.randint(0, len(words)-1)
        file.close()
        return(words[word_pos])        

    def eur_res():
        import random
        with open('eur_res_file.txt', 'r') as file:
            data = file.read()
            words = data.split('\n')
        word_pos = random.randint(0, len(words)-1)
        file.close()
        return(words[word_pos])

    def Chinese_Option():
        import tkinter as chi
        window = chi.Tk()
        window.title('Chinese Options')
        window.geometry('250x250')
        window.configure(bg='plum3')
        x = chi.Label(window,  bg='pink', fg='purple', width=25, text='Do you want')
        x.pack()
        y = chi.Label(window, bg='pink', fg='purple', width=25, text=chi_res())
        y.pack()
        def yes():
            chi.Label(window, bg='pink', fg='purple', width=25, text='Ok let\'s go!!').pack()
            e_btn = chi.Button(window,text='Let\'s go', bg='grey', fg='white', activebackground='black',activeforeground='white', command=exit).pack(pady=5)

        def no():
            x.config(text='What about')
            y.config(text=chi_res())
        
        y_btn = chi.Button(window, text='yes', height=1, width=2, bg='dark sea green', fg='white', activebackground='black',activeforeground='white', command=yes).pack(pady=1)
        n_btn = chi.Button(window, text='no', height=1, width=2, bg='coral1', fg='white', activebackground='black',activeforeground='white', command=no).pack(pady=1)

        window.mainloop
    def Filipino_Option():
        import tkinter as fil
        window = fil.Tk()
        window.title('Filipino Options')
        window.geometry('250x250')
        window.configure(bg='plum3')
        x = fil.Label(window,  bg='pink', fg='purple', width=25, text='Do you want')
        x.pack()
        y = fil.Label(window, bg='pink', fg='purple', width=25, text=fil_res())
        y.pack()
        def yes():
            fil.Label(window, bg='pink', fg='purple', width=25, text='Ok let\'s go!!').pack()
            e_btn = fil.Button(window,text='Let\'s go', bg='grey', fg='white', activebackground='black',activeforeground='white', command=exit).pack(pady=5)

        def no():
            x.config(text='What about')
            y.config(text=fil_res())
        
        y_btn = fil.Button(window, text='yes', height=1, width=2, bg='dark sea green', fg='white', activebackground='black',activeforeground='white', command=yes).pack(pady=1)
        n_btn = fil.Button(window, text='no', height=1, width=2, bg='coral1', fg='white', activebackground='black',activeforeground='white', command=no).pack(pady=1)

        window.mainloop
    def Indian_Option():
        import tkinter as ind
        window = ind.Tk()
        window.title('Indian Options')
        window.geometry('250x250')
        window.configure(bg='plum3')
        x = ind.Label(window,  bg='pink', fg='purple', width=25, text='Do you want')
        x.pack()
        y = ind.Label(window, bg='pink', fg='purple', width=25, text=ind_res())
        y.pack()
        def yes():
            ind.Label(window, bg='pink', fg='purple', width=25, text='Ok let\'s go!!').pack()
            e_btn = ind.Button(window,text='Let\'s go', bg='grey', fg='white', activebackground='black',activeforeground='white', command=exit).pack(pady=5)

        def no():
            x.config(text='What about')
            y.config(text=ind_res())
        
        y_btn = ind.Button(window, text='yes', height=1, width=2, bg='dark sea green', fg='white', activebackground='black',activeforeground='white', command=yes).pack(pady=1)
        n_btn = ind.Button(window, text='no', height=1, width=2, bg='coral1', fg='white', activebackground='black',activeforeground='white', command=no).pack(pady=1)

        window.mainloop
    def Japanese_Option():
        import tkinter as jap
        window = jap.Tk()
        window.title('Japanese Options')
        window.geometry('250x250')
        window.configure(bg='plum3')
        x = jap.Label(window,  bg='pink', fg='purple', width=25, text='Do you want')
        x.pack()
        y = jap.Label(window, bg='pink', fg='purple', width=25, text=jap_res())
        y.pack()
        def yes():
            jap.Label(window, bg='pink', fg='purple', width=25, text='Ok let\'s go!!').pack()
            e_btn = jap.Button(window,text='Let\'s go', bg='grey', fg='white', activebackground='black',activeforeground='white', command=exit).pack(pady=5)

        def no():
            x.config(text='What about')
            y.config(text=jap_res())
        
        y_btn = jap.Button(window, text='yes', height=1, width=2, bg='dark sea green', fg='white', activebackground='black',activeforeground='white', command=yes).pack(pady=1)
        n_btn = jap.Button(window, text='no', height=1, width=2, bg='coral1', fg='white', activebackground='black',activeforeground='white', command=no).pack(pady=1)

        window.mainloop
    def Korean_Option():
        import tkinter as kor
        window = kor.Tk()
        window.title('Korean Options')
        window.geometry('250x250')
        window.configure(bg='plum3')
        x = kor.Label(window,  bg='pink', fg='purple', width=25, text='Do you want')
        x.pack()
        y = kor.Label(window, bg='pink', fg='purple', width=25, text=kor_res())
        y.pack()
        def yes():
            kor.Label(window, bg='pink', fg='purple', width=25, text='Ok let\'s go!!').pack()
            e_btn = kor.Button(window,text='Let\'s go', bg='grey', fg='white', activebackground='black',activeforeground='white', command=exit).pack(pady=5)

        def no():
            x.config(text='What about')
            y.config(text=kor_res())
        
        y_btn = kor.Button(window, text='yes', height=1, width=2, bg='dark sea green', fg='white', activebackground='black',activeforeground='white', command=yes).pack(pady=1)
        n_btn = kor.Button(window, text='no', height=1, width=2, bg='coral1', fg='white', activebackground='black',activeforeground='white', command=no).pack(pady=1)

        window.mainloop    
    def Vietnamese_Option():
        import tkinter as vie
        window = vie.Tk()
        window.title('Vietnamese Options')
        window.geometry('250x250')
        window.configure(bg='plum3')
        x = vie.Label(window,  bg='pink', fg='purple', width=25, text='Do you want')
        x.pack()
        y = vie.Label(window, bg='pink', fg='purple', width=25, text=vie_res())
        y.pack()
        def yes():
            vie.Label(window, bg='pink', fg='purple', width=25, text='Ok let\'s go!!').pack()
            e_btn = vie.Button(window,text='Let\'s go', bg='grey', fg='white', activebackground='black',activeforeground='white', command=exit).pack(pady=5)

        def no():
            x.config(text='What about')
            y.config(text=vie_res())
        
        y_btn = vie.Button(window, text='yes', height=1, width=2, bg='dark sea green', fg='white', activebackground='black',activeforeground='white', command=yes).pack(pady=1)
        n_btn = vie.Button(window, text='no', height=1, width=2, bg='coral1', fg='white', activebackground='black',activeforeground='white', command=no).pack(pady=1)

        window.mainloop
    def Mexican_Option():
        import tkinter as mex
        window = mex.Tk()
        window.title('Mexican Options')
        window.geometry('250x250')
        window.configure(bg='plum3')
        x = mex.Label(window,  bg='pink', fg='purple', width=25, text='Do you want')
        x.pack()
        y = mex.Label(window, bg='pink', fg='purple', width=25, text=mex_res())
        y.pack()
        def yes():
            mex.Label(window, bg='pink', fg='purple', width=25, text='Ok let\'s go!!').pack()
            e_btn = mex.Button(window,text='Let\'s go', bg='grey', fg='white', activebackground='black',activeforeground='white', command=exit).pack(pady=5)

        def no():
            x.config(text='What about')
            y.config(text=mex_res())
        
        y_btn = mex.Button(window, text='yes', height=1, width=2, bg='dark sea green', fg='white', activebackground='black',activeforeground='white', command=yes).pack(pady=1)
        n_btn = mex.Button(window, text='no', height=1, width=2, bg='coral1', fg='white', activebackground='black',activeforeground='white', command=no).pack(pady=1)

        window.mainloop
    def Thai_Option():
        import tkinter as tha
        window = tha.Tk()
        window.title('Thai Options')
        window.geometry('250x250')
        window.configure(bg='plum3')
        x = tha.Label(window,  bg='pink', fg='purple', width=25, text='Do you want')
        x.pack()
        y = tha.Label(window, bg='pink', fg='purple', width=25, text=tha_res())
        y.pack()
        def yes():
            tha.Label(window, bg='pink', fg='purple', width=25, text='Ok let\'s go!!').pack()
            e_btn = tha.Button(window,text='Let\'s go', bg='grey', fg='white', activebackground='black',activeforeground='white', command=exit).pack(pady=5)

        def no():
            x.config(text='What about')
            y.config(text=tha_res())
        
        y_btn = tha.Button(window, text='yes', height=1, width=2, bg='dark sea green', fg='white', activebackground='black',activeforeground='white', command=yes).pack(pady=1)
        n_btn = tha.Button(window, text='no', height=1, width=2, bg='coral1', fg='white', activebackground='black',activeforeground='white', command=no).pack(pady=1)

        window.mainloop  
    def FastFood_Option():
        import tkinter as fas
        window = fas.Tk()
        window.title('Fast Food Options')
        window.geometry('250x250')
        window.configure(bg='plum3')
        x = fas.Label(window,  bg='pink', fg='purple', width=25, text='Do you want')
        x.pack()
        y = fas.Label(window, bg='pink', fg='purple', width=25, text=fas_res())
        y.pack()
        def yes():
            fas.Label(window, bg='pink', fg='purple', width=25, text='Ok let\'s go!!').pack()
            e_btn = fas.Button(window,text='Let\'s go', bg='grey', fg='white', activebackground='black',activeforeground='white', command=exit).pack(pady=5)

        def no():
            x.config(text='What about')
            y.config(text=fas_res())
        
        y_btn = fas.Button(window, text='yes', height=1, width=2, bg='dark sea green', fg='white', activebackground='black',activeforeground='white', command=yes).pack(pady=1)
        n_btn = fas.Button(window, text='no', height=1, width=2, bg='coral1', fg='white', activebackground='black',activeforeground='white', command=no).pack(pady=1)

        window.mainloop
    def European_Option():
        import tkinter as eur
        window = eur.Tk()
        window.title('European Options')
        window.geometry('250x250')
        window.configure(bg='plum3')
        x = eur.Label(window,  bg='pink', fg='purple', width=25, text='Do you want')
        x.pack()
        y = eur.Label(window, bg='pink', fg='purple', width=25, text=eur_res())
        y.pack()
        def yes():
            eur.Label(window, bg='pink', fg='purple', width=25, text='Ok let\'s go!!').pack()
            e_btn = eur.Button(window,text='Let\'s go', bg='grey', fg='white', activebackground='black',activeforeground='white', command=exit).pack(pady=5)

        def no():
            x.config(text='What about')
            y.config(text=eur_res())
        
        y_btn = eur.Button(window, text='yes', height=1, width=2, bg='dark sea green', fg='white', activebackground='black',activeforeground='white', command=yes).pack(pady=1)
        n_btn = eur.Button(window, text='no', height=1, width=2, bg='coral1', fg='white', activebackground='black',activeforeground='white', command=no).pack(pady=1)

        window.mainloop


    chi_btn = res.Button(window, text='Chinese', height=1, width=8, bg='pink', fg='magenta4', activebackground='black',activeforeground='white', command=Chinese_Option).pack(pady=3)
    fil_btn = res.Button(window, text='Filipino', height=1, width=8, bg='pink', fg='magenta4', activebackground='black',activeforeground='white', command=Filipino_Option).pack(pady=3)
    ind_btn = res.Button(window, text='Indian', height=1, width=8, bg='pink', fg='magenta4', activebackground='black',activeforeground='white', command=Indian_Option).pack(pady=3)
    jap_btn = res.Button(window, text='Japanese', height=1, width=8, bg='pink', fg='magenta4', activebackground='black',activeforeground='white', command=Japanese_Option).pack(pady=3)
    kor_btn = res.Button(window, text='Korean', height=1, width=8, bg='pink', fg='magenta4', activebackground='black',activeforeground='white', command=Korean_Option).pack(pady=3)
    vie_btn = res.Button(window, text='Vietnamese', height=1, width=8, bg='pink', fg='magenta4', activebackground='black',activeforeground='white', command=Vietnamese_Option).pack(pady=3)
    mex_btn = res.Button(window, text='Mexican', height=1, width=8, bg='pink', fg='magenta4', activebackground='black',activeforeground='white', command=Mexican_Option).pack(pady=3)
    tha_btn = res.Button(window, text='Thai', height=1, width=8, bg='pink', fg='magenta4', activebackground='black',activeforeground='white', command=Thai_Option).pack(pady=3)
    fas_btn = res.Button(window, text='Fast Food', height=1, width=8, bg='pink', fg='magenta4', activebackground='black',activeforeground='white', command=FastFood_Option).pack(pady=3)
    fan_btn = res.Button(window, text='European', height=1, width=8, bg='pink', fg='magenta4', activebackground='black',activeforeground='white', command=European_Option).pack(pady=3)
 
    window.mainloop()

def add_res():
    import tkinter as add

    window = add.Tk()
    window.title('Add a restaurant to your list')
    window.geometry('400x350')
    window.configure(bg='plum3')
    lab = add.Label(window, bg='pink', fg='purple', width=100, text='Which cuisine list would you like to add to?')
    lab.pack()
    def Add_Chinese_Option():
        import tkinter as addchi
        window = addchi.Tk()
        window.title('Add a restaurant to Chinese list')
        window.geometry('400x350')
        window.configure(bg='plum3')
        chilab = addchi.Label(window, bg='pink', fg='purple', width=100, text='What restaurant would tou like to add?')
        chilab.pack()
        
    def Add_Filipino_Option():
        lab.config(text='This has been added')
        window.mainloop

    def Add_Indian_Option():
        lab.config(text='This has been added')
        window.mainloop
        
    def Add_Japanese_Option():
        lab.config(text='This has been added')
        window.mainloop

    def Add_Korean_Option():
        lab.config(text='This has been added')
        window.mainloop

    def Add_Vietnamese_Option():
        lab.config(text='This has been added')
        window.mainloop

    def Add_Mexican_Option():
        lab.config(text='This has been added')
        window.mainloop

    def Add_Thai_Option():
        lab.config(text='This has been added')
        window.mainloop

    def Add_FastFood_Option():
        lab.config(text='This has been added')
        window.mainloop

    def Add_European_Option():
        lab.config(text='This has been added')
        window.mainloop
    

    
         
    chi_btn = add.Button(window, text='Chinese', height=1, width=8, bg='pink', fg='magenta4', activebackground='black',activeforeground='white', command=Add_Chinese_Option).pack(pady=3)
    fil_btn = add.Button(window, text='Filipino', height=1, width=8, bg='pink', fg='magenta4', activebackground='black',activeforeground='white', command=Add_Filipino_Option).pack(pady=3)
    ind_btn = add.Button(window, text='Indian', height=1, width=8, bg='pink', fg='magenta4', activebackground='black',activeforeground='white', command=Add_Indian_Option).pack(pady=3)
    jap_btn = add.Button(window, text='Japanese', height=1, width=8, bg='pink', fg='magenta4', activebackground='black',activeforeground='white', command=Add_Japanese_Option).pack(pady=3)
    kor_btn = add.Button(window, text='Korean', height=1, width=8, bg='pink', fg='magenta4', activebackground='black',activeforeground='white', command=Add_Korean_Option).pack(pady=3)
    vie_btn = add.Button(window, text='Vietnamese', height=1, width=8, bg='pink', fg='magenta4', activebackground='black',activeforeground='white', command=Add_Vietnamese_Option).pack(pady=3)
    mex_btn = add.Button(window, text='Mexican', height=1, width=8, bg='pink', fg='magenta4', activebackground='black',activeforeground='white', command=Add_Mexican_Option).pack(pady=3)
    tha_btn = add.Button(window, text='Thai', height=1, width=8, bg='pink', fg='magenta4', activebackground='black',activeforeground='white', command=Add_Thai_Option).pack(pady=3)
    fas_btn = add.Button(window, text='Fast Food', height=1, width=8, bg='pink', fg='magenta4', activebackground='black',activeforeground='white', command=Add_FastFood_Option).pack(pady=3)
    fan_btn = add.Button(window, text='European', height=1, width=8, bg='pink', fg='magenta4', activebackground='black',activeforeground='white', command=Add_European_Option).pack(pady=3)
    window.mainloop

run_btn = intro.Button(window, text='Where should I eat', height=5, width=15, bg='bisque', fg='black',activebackground='black',activeforeground='white', command=main).pack(pady=5)
add_btn = intro.Button(window, text='Add A Restaurant', height=1, width=15, bg='bisque', fg='black',activebackground='black',activeforeground='white', command=add_res).pack(pady=5)

window.mainloop()
