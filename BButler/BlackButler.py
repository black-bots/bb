#!/usr/bin/env python
__author__='Supreme ciento'
__copyright__='Copyright 2023, Cloud Bots™ BlackBots'
__credits__=['Supreme Ciento']
__license__='GPL'
__maintainer__='Cloud Bots™'
__email__='cloudbotsbiz@gmail.com'
__status__='Production'
__version__='8.12.21'


_M='Hello i am '
_L='You are a helpful assistant.'
_K='system'
_J='C:\\WINDOWS\\py.exe'
_I='ConsoleWindowClass'
_H=False
_G='BlackButler'
_F='\nUser said: '
_E='assistant'
_D='user'
_C=True
_B='content'
_A='role'
import os,sys,openai,speech_recognition as sr,datetime
from time import sleep
from pystray import Icon as picon,Menu as menu,MenuItem as item
from PIL import Image
from threading import Thread
import tkinter as tk
from tkinter import Label,Entry,ttk
import webbrowser,random,colorama
from colorama import init,Fore,Back,Style
init(convert=_C)
init(autoreset=_C)
def working_directory(directory):
        A=directory;B=os.getcwd()
        try:os.chdir(A);yield A
        finally:os.chdir(B)
os.environ['DISPLAY']=':0'
from platform import system
import win32com.client
if system()=='Windows'or'nt':import win32com.client as wincl
else:print('Sorry, TTS client is not supported on Linux or MacOS');exit()
import win32com
shell=win32com.client.Dispatch('WScript.Shell')
try:import winxpgui as win32gui
except ImportError:import win32gui
Minimize=win32gui.FindWindow(_I,_J)
Maximize=win32gui.FindWindow(_I,_J)
import win32con
try:win32gui.ShowWindow(Minimize,win32con.SW_MINIMIZE)
except:pass
spk=wincl.Dispatch('SAPI.SpVoice')
vcs=spk.GetVoices()
SVSFlag=11
human=[0,1]
Eh=random.choice(human)
spker_number=Eh
Humanoid=vcs.Item(spker_number).GetAttribute('Name')
spkr=Humanoid.replace('Microsoft','')
spkrr=spkr.replace('Desktop','')
spkrrr=spkrr.replace(' ','')
spk.Voice
spk.SetVoice(vcs.Item(spker_number))
voice=Eh
spk.Volume=100
spk.Rate=1
hour=int(datetime.datetime.now().hour)
with open('etc\\key.txt')as f:
        for line in f:tuo=line.strip()[48:];wun=line.strip()[:3];print('\n\nApi-Key Set: '+Back.BLACK+colorama.Fore.BLUE+wun+'*'*45+tuo)
        if len(line.strip())!=51:print('\n\nPlease provide Api-Key in key.text file');sleep(3);os._exit(0)
        else:0
api_line=line.strip()
api_key=str(api_line)
openai.api_key=api_key
def threading():
        win.withdraw()
        def A():
                C='ENABLED\n\n';B='yes'
                if entry.get()==B:print(_F+Back.BLACK+colorama.Fore.YELLOW+entry.get()+colorama.Style.RESET_ALL+' \nVoice Mode: '+Back.BLACK+colorama.Fore.GREEN+C);win32gui.ShowWindow(Maximize,win32con.SW_SHOWNORMAL);A=Thread(target=main);A.start();A.is_alive()
                elif entry.get()=='no':print(_F+Back.BLACK+colorama.Fore.YELLOW+entry.get()+colorama.Style.RESET_ALL+' \nText Mode: '+Back.BLACK+colorama.Fore.GREEN+C);win32gui.ShowWindow(Maximize,win32con.SW_SHOWNORMAL);A=Thread(target=main2);A.start();A.is_alive()
                else:print('User said: '+entry.get());print('Please type '+Back.BLACK+colorama.Fore.YELLOW+B+colorama.Style.RESET_ALL+' or '+Back.BLACK+colorama.Fore.YELLOW+'no');onEx()
        B=Image.open('etc\\-.ico');picon(_G,B,menu=menu(item('Start',A),menu.SEPARATOR,item('About',websi),item('Reload',reload),item('Quit',on_clicked),menu.SEPARATOR)).run()
def on_clicked(icon,item):
        if str(item)=='Quit':
                icon.stop()
                try:onEx()
                except:os._exit(0)
def reload():os.execl(sys.executable,sys.executable,*sys.argv)
def websi():webbrowser.open('https://black-bots.github.io/',new=2)
def onEx():
        import psutil as A;C=_G;D='BlackButler.exe'
        def E(app):
                for B in A.process_iter():
                        try:
                                if app.lower()in B.name().lower():return _C
                        except (A.NoSuchProcess,A.AccessDenied,A.ZombieProcess):pass
                return _H
        def F():
                try:os.system('TASKKILL /F /IM BlackButler.exe')
                except:pass
                try:os.system('TASKKILL /F /IM py.exe')
                except:pass
        def B():return os.startfile(D)
        try:
                B()
                while _C:
                        if E(C):F();sleep(5)
                        else:B()
        except Exception as G:
                try:os._exit(0)
                except:sys.exit(0)
def gb():
        print('Goodbye!')
        try:A=['Adios compadre','See you later','Until Next time','Sorry to see you go'];spk.Speak(random.choice(A))
        except:pass
        onEx()
def takeCommand():
        if 1:
                A=sr.Recognizer()
                with sr.Microphone()as C:print(Back.BLACK+colorama.Fore.MAGENTA+'Listening...');A.pause_threshold=1;D=A.listen(C)
                try:print(Back.BLACK+colorama.Fore.MAGENTA+'Recognizing...');B=A.recognize_google(D,language='en-in');print(Back.BLACK+colorama.Fore.GREEN+Style.BRIGHT+_F+Back.BLACK+colorama.Fore.CYAN+f"{B}\n")
                except Exception as E:print(Back.BLACK+colorama.Fore.RED+'Say that again please...');return'None'
                return B
def send_message(message_log):
        A=openai.ChatCompletion.create(model='gpt-3.5-turbo-0301',messages=message_log,max_tokens=3800,n=1,stop=None,temperature=0.7)
        for B in A.choices:
                if'text'in B:return B.text
        return A.choices[0].message.content
def f():A=[OSError('error 1'),SystemError('error 2')];raise Exception('There were problems',A)
def main():
        F='goodbye'
        try:
                B=[{_A:_K,_B:_L}]
                if hour>=0 and hour<12:spk.Speak('Good Morning!')
                elif hour>=12 and hour<18:spk.Speak('Good Afternoon!')
                else:spk.Speak('Good Evening!')
                spk.Speak(_M+spkrrr+', how can i assist u?');D=_C
                while _C:
                        E=takeCommand().lower()
                        if D:
                                C=E;B.append({_A:_D,_B:C});A=send_message(B);B.append({_A:_E,_B:A});print(Back.BLACK+colorama.Fore.CYAN+Style.BRIGHT+f"{spkrrr}: "+Back.BLACK+colorama.Fore.YELLOW+f"{A}");spk.Speak(A)
                                if C==F:gb()
                                D=_H
                        else:
                                if C==F:gb()
                                C=E;B.append({_A:_D,_B:C});A=send_message(B);B.append({_A:_E,_B:A});print(Back.BLACK+colorama.Fore.CYAN+Style.BRIGHT+f"{spkrrr}: "+Back.BLACK+colorama.Fore.YELLOW+f"{A}");spk.Speak(A)
        except Exception as G:print(f"Errors Happened O,..,O {type(G)}: e")
def main2():
        F='quit';E='\nYou: ';A=[{_A:_K,_B:_L}]
        if hour>=0 and hour<12:print(Back.BLACK+colorama.Fore.CYAN+'Good Morning!\n')
        elif hour>=12 and hour<18:print(Back.BLACK+colorama.Fore.CYAN+'Good Afternoon!\n')
        else:print(Back.BLACK+colorama.Fore.CYAN+'Good Evening!\n')
        print(_M+Back.BLACK+colorama.Fore.CYAN+Style.BRIGHT+f"{spkrrr}");print(colorama.Style.RESET_ALL);D=_C
        while _C:
                if D:
                        B=input(E);A.append({_A:_D,_B:B});print(Back.BLACK+colorama.Fore.GREEN+'\nAnalyzing...\n');C=send_message(A)
                        if B.lower()==F:gb()
                        A.append({_A:_E,_B:C});print(Back.BLACK+colorama.Fore.CYAN+Style.BRIGHT+f"{spkrrr}: "+Back.BLACK+colorama.Fore.YELLOW+f"{C}");D=_H
                else:
                        B=input(E)
                        if B.lower()==F:gb()
                        A.append({_A:_D,_B:B});C=send_message(A);A.append({_A:_E,_B:C});print(Back.BLACK+colorama.Fore.CYAN+Style.BRIGHT+f"{spkrrr}: "+Back.BLACK+colorama.Fore.YELLOW+f"{C}")
if __name__=='__main__':win=tk.Tk();win.title(_G);win.iconbitmap('etc\\\\-.ico');win.geometry('250x100');win.eval('tk::PlaceWindow . center');label=Label(win,text='',font='Courier 10 bold');label.configure(text="Type 'yes' if speaking \nType 'no' if typing");label.grid(row=1,column=3,pady=5);entry=Entry(win,width=40);entry.focus_set();entry.grid(row=2,column=3,pady=1);butt=ttk.Button(win,text='Load',width=8,command=threading);butt.grid(row=3,column=3,pady=5);win.mainloop()
