import ctypes
import sys
import os
from tkinter import *
from tkinter import messagebox, filedialog
from load_language import *
from logic import createFolder, openAll


def chooseDir():
    Tk().withdraw()
    global chooseDirString
    chooseDirString = filedialog.askdirectory(title=chooseFileName)
    if len(chooseDirString) < 57:
        chooseDirVar.set(chooseDirString)
    else:
        chooseDirVar.set(chooseDirString[0:10] + "..." + chooseDirString[-42:])
    if chooseDirString == "":
        chooseDirVar.set(chooseDirText)
    global numberOfFiles
    numberOfFiles = 0

    for file in os.listdir(chooseDirString):
        if file.lower().endswith(".mkv") and var_mkvFormat:
            numberOfFiles += 1
        elif file.lower().endswith(".mp4") and var_mp4Format:
            numberOfFiles += 1
        elif file.lower().endswith(".avi") and var_aviFormat:
            numberOfFiles += 1
        elif file.lower().endswith(".srt") and var_srtFormat:
            numberOfFiles += 1
        elif file.lower().endswith(".zip") and var_zipFormat:
            numberOfFiles += 1
    if getAncher == 'e':
        numberOfFilesVar.set("شروع دسته بندی" + str(numberOfFiles) + ' فایل')
    else:
        numberOfFilesVar.set('Start Grouping ' + str(numberOfFiles) + " Files")


def about():
    ctypes.windll.user32.MessageBoxW(0, "An App By: Ahmad Reza Kamali & Mahdi Sabour", infoText, 0)


def changeLanguageEvent():
    if getAncher == 'e':
        settings.set('Language', 'English')
        settings.save()
        answer = messagebox.askyesno("Language Changed!",
                                     "For Apply changes you need to reopen the program.\nRestart now?")
        if answer:
            os.execl(sys.executable, *([sys.executable] + sys.argv))

    else:
        settings.set('Language', 'Persian')
        settings.save()
        answer = messagebox.askyesno("زبان برنامه تغییر کرد",
                                     "برای اعمال تغییرات باید برنامه از اول اجرا شود\nبارگذاری مجدد برنامه؟")
        if answer:
            os.execl(sys.executable, *([sys.executable] + sys.argv))


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


if __name__ == '__main__':
    root = Tk()
    var_mkvFormat = BooleanVar()
    var_mp4Format= BooleanVar()
    var_aviFormat= BooleanVar()
    var_srtFormat= BooleanVar()
    var_zipFormat= BooleanVar()
    var_yearInBracket= BooleanVar()
    var_sameName= BooleanVar()
    var_serialFiles= BooleanVar()
    var_movieFiles= BooleanVar()
    var_episodeFolders =  BooleanVar()
    root.resizable(False, False)
    menubar = Menu(root)
    subMenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="File", menu=subMenu)
    subMenu.add_command(label=openText, command=chooseDir)
    subMenu.add_command(label=exitText, command=root.quit)
    root.config(menu=menubar)

    subMenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Help", menu=subMenu)
    subMenu.add_command(label=infoText, command=about)
    subMenu.add_command(label=changeLanguage, command=changeLanguageEvent)
    root.iconbitmap(resource_path('Logo.ico'))

    Label(root, text=nameFormat, anchor=getAncher).pack(side=TOP, fill='both')
    formatString = StringVar()
    formatString.set("{name} {year}")
    formatTextField = Entry(root, textvariable=formatString, font="Arial 15")
    formatTextField.pack(side=TOP, fill=X)

    Label(root, text=settingsText, anchor=getAncher).pack(side=TOP, fill='both')

    folderEpisodesCheckButton = Checkbutton(root, text=folderForEpisodes,anchor=getAncher,var=var_episodeFolders)
    folderEpisodesCheckButton.pack(side=TOP, fill=X)

    putYearInBracketsCheckButton = Checkbutton(root, text=putYearInBrackets,anchor=getAncher,var=var_yearInBracket)
    putYearInBracketsCheckButton.pack(side=TOP, fill=X)
    putYearInBracketsCheckButton.select()

    sameName = Checkbutton(root, text=nameChange,anchor=getAncher,var=var_sameName)
    sameName.pack(side=TOP, fill=X)
    sameName.select()


    Frame(root, width=1, height=1, highlightbackground="black", highlightcolor="black", highlightthickness=3,
                  bd=0).pack(side=TOP, fill=X)

    Label(root, text=formatsText, anchor=getAncher).pack(side=TOP, fill='both')

    formats = Frame(root)
    moviesCheckButton = Checkbutton(formats, text=moviesText, anchor=getAncher,var=var_movieFiles)
    moviesCheckButton.pack(side=LEFT)
    moviesCheckButton.select()

    seriesCheckButton = Checkbutton(formats, text=seriesText, anchor=getAncher,var=var_serialFiles)
    seriesCheckButton.pack(side=LEFT)
    seriesCheckButton.select()

    mkvCheckButton = Checkbutton(formats, text="mkv", anchor=getAncher,var=var_mkvFormat)
    mkvCheckButton.pack(side=LEFT)
    mkvCheckButton.select()

    srtCheckButton = Checkbutton(formats, text="srt", anchor=getAncher,var=var_srtFormat)
    srtCheckButton.pack(side=LEFT)
    srtCheckButton.select()

    mp4CheckButton = Checkbutton(formats, text="mp4", anchor=getAncher,var=var_mp4Format)
    mp4CheckButton.pack(side=LEFT)
    mp4CheckButton.select()

    aviCheckButton = Checkbutton(formats, text="avi", anchor=getAncher,var=var_aviFormat)
    aviCheckButton.pack(side=LEFT)
    aviCheckButton.select()

    zipCheckButton = Checkbutton(formats, text="zip", anchor=getAncher, var=var_zipFormat)
    zipCheckButton.pack(side=LEFT)

    formats.pack(side=TOP, fill=X,anchor=getAncher)


    Frame(root, width=1, height=1, highlightbackground="black", highlightcolor="black", highlightthickness=3,
          bd=0).pack(side=TOP, fill=X)
    chooseDirVar = StringVar()
    chooseDirString = ""
    numberOfFiles = 0
    numberOfFilesVar = StringVar()
    numberOfFilesVar.set(startText)
    btn = Button(root, textvariable=chooseDirVar, command=chooseDir).pack(side=TOP, fill='both')
    Button(root, text=unfolderString,command=lambda :openAll(chooseDirString)).pack(side=TOP, fill=X)
    chooseDirVar.set(chooseDirText)
    Frame(root, width=10, height=1, bd=0).pack(side=LEFT)
    Frame(root, width=10, height=1, bd=0).pack(side=RIGHT)
    Frame(root, width=5, height=5, bd=0).pack(side=TOP, fill=X)
    Button(root, text=quitText, command=root.quit).pack(side=last)
    Button(root, textvariable=numberOfFilesVar,command=lambda :createFolder(chooseDirString,formatString.get(),var_mkvFormat,var_mp4Format,var_aviFormat,var_srtFormat,var_zipFormat,var_yearInBracket,var_sameName,var_serialFiles,var_movieFiles,var_episodeFolders)).pack(side=first)
    Frame(root, width=1, height=35, bd=0).pack(side=BOTTOM, fill=X)
    root.title(nameOfProgram)
    root.mainloop()
