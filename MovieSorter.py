import os
import sys
import re
from tkinter import *
from tkinter import messagebox,filedialog

from load_language import *


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class CheckBar(Frame):
    def __init__(self, parent=None, picks=[], side=LEFT, anchor=getAncher, defaultcheck=False):
        Frame.__init__(self, parent)
        self.vars = []
        for pick in picks:
            var = IntVar()
            chk = Checkbutton(self, text=pick, variable=var)
            if defaultcheck:
                chk.select()
            chk.pack(side=side, anchor=anchor, expand=YES)
            self.vars.append(var)

    def state(self):
        return map((lambda var: var.get()), self.vars)


if __name__ == '__main__':
    root = Tk()
    root.resizable(False, False)


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


    def about():
        ctypes.windll.user32.MessageBoxW(0, "An App By: Ahmad Reza Kamali & Mahdi Sabour", infoText, 0)


    def chooseDir():
        Tk().withdraw()
        options = {}
        options['title'] = chooseFileName
        global chooseDirString
        chooseDirString = filedialog.askdirectory(**options)
        if len(chooseDirString) < 57:
            chooseDirVar.set(chooseDirString)
        else:
            chooseDirVar.set(chooseDirString[0:10] + "..." + chooseDirString[-42:])
        if chooseDirString == "":
            chooseDirVar.set(chooseDirText)
        global numberOfFiles
        numberOfFiles = 0
        for file in os.listdir(chooseDirString):
            if file.lower().endswith(".mkv") and list(videoFiles.state())[2] == 1:
                numberOfFiles += 1
            elif file.lower().endswith(".mp4") and list(videoFiles.state())[3] == 1:
                numberOfFiles += 1
            elif file.lower().endswith(".avi") and list(videoFiles.state())[4] == 1:
                numberOfFiles += 1
            elif file.lower().endswith(".srt") and list(videoFiles.state())[5] == 1:
                numberOfFiles += 1
            elif file.lower().endswith(".zip") and list(videoFiles.state())[6] == 1:
                numberOfFiles += 1
        if getAncher == 'e':
            numberOfFilesVar.set("شروع دسته بندی" + str(numberOfFiles) + ' فایل')
        else:
            numberOfFilesVar.set('Start Grouping ' + str(numberOfFiles) + " Files")


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
    var = StringVar()
    Label(root, textvariable=var, anchor=getAncher).pack(side=TOP, fill='both')
    var.set(settingsText)
    willRemove = CheckBar(root, [folderForEpisodes, putYearInBrackets])
    willRename = CheckBar(root, [nameChange], defaultcheck=True)

    videoFiles = CheckBar(root, [moviesText, seriesText, '.mkv', '.mp4', '.avi', '.srt', '.zip'], defaultcheck=True)
    model = StringVar()
    model.set("{name} - {year}")
    modelCreator = Entry(root,textvariable= model,font="Calibri 15")
    modelCreator.pack(side=TOP, fill=X)
    willRemove.pack(side=TOP, fill=X)
    willRename.pack(side=TOP, fill=X)

    frame = Frame(root, width=1, height=1, highlightbackground="black", highlightcolor="black", highlightthickness=3,
                  bd=0).pack(side=TOP, fill=X)
    var1 = StringVar()
    Label(root, textvariable=var1, anchor=getAncher).pack(side=TOP, fill='both')
    var1.set(formatsText)
    videoFiles.pack(side=TOP, fill=X)
    Frame(root, width=1, height=1, highlightbackground="black", highlightcolor="black", highlightthickness=3,
          bd=0).pack(side=TOP, fill=X)
    chooseDirVar = StringVar()
    chooseDirString = ""
    numberOfFiles = 0
    numberOfFilesVar = StringVar()
    def openAll():
        if len(chooseDirString) < 2:
            return
        for root, dirs, files in os.walk(chooseDirString):
            for file in files:
                os.rename(os.path.join(root, file), chooseDirString + "\\" + file)
            if not os.listdir(root):
                os.rmdir(root)


    if getAncher == 'e':
        numberOfFilesVar.set('شروع دسته بندی')
    else:
        numberOfFilesVar.set('Start Grouping')



    def createFolder():
        list(videoFiles.state())[3]
        for file in os.listdir(chooseDirString):
            if file.lower().endswith(".mkv") and list(videoFiles.state())[2] == 1:
                folder_name = file.replace(".mkv", "")
            elif file.lower().endswith(".mp4") and list(videoFiles.state())[3] == 1:
                folder_name = file.replace(".mp4", "")
            elif file.lower().endswith(".avi") and list(videoFiles.state())[4] == 1:
                folder_name = file.replace(".avi", "")
            elif file.lower().endswith(".srt") and list(videoFiles.state())[5] == 1:
                folder_name = file.replace(".srt", "")
            elif file.lower().endswith(".zip") and list(videoFiles.state())[6] == 1:
                folder_name = file.replace(".zip", "")
            else:
                continue
            folder_name = folder_name.replace(".", " ")
            folder_name = folder_name.replace("_", " ")
            folder_name = folder_name.replace("-", " ")
            folder_name = folder_name.replace("(", "")
            folder_name = folder_name.replace(")", "")
            folder_name = folder_name.replace("  ", " ")
            folder_name = folder_name.replace("  ", " ")

            folderWords = re.split(r'\s', folder_name)
            # Serial or Movie? Let's Find out
            folder_name = ""
            serial = False
            season = '01'
            episode = '01'
            firstS = True
            for s in folderWords:
                if (firstS):
                    firstS = False
                    folder_name += str(s) + " "
                    continue
                if len(s) == 6:
                    if (s[0] == 'S' or s[0] == 's') and (s[3] == 'E' or s[3] == 'e') and (s[1].isdigit()):
                        serial = True
                        season = 'S' + str(s[1]) + str(s[2])
                        episode = 'E' + str(s[4]) + str(s[5])
                        if folder_name.endswith(" "):
                            folder_name = folder_name[:-1]
                        break
                folder_name += str(s) + " "

            #################################
            if serial and list(videoFiles.state())[1] == 1:
                newDir = chooseDirString
                newDir = newDir + "\\" + folder_name
                try:
                    os.mkdir(newDir)
                except OSError:
                    print("Fucking Error")
                else:
                    print("Fucking Nice")
                newDir = newDir + "\\" + season
                try:
                    os.mkdir(newDir)
                except OSError:
                    print("Fucking Error")
                else:
                    print("Fucking Nice")
                if list(willRemove.state())[0] == 1:
                    newDir = newDir + "\\" + episode
                    try:
                        os.mkdir(newDir)
                    except OSError:
                        print("Fucking Error")
                    else:
                        print("Fucking Nice")
                os.rename(os.path.join(chooseDirString, file), newDir + "\\" + file)
            if (not serial) and list(videoFiles.state())[0] == 1:
                folder_name = ""
                firstS = True
                year = 0000
                name = ""
                for s in folderWords:
                    if s.isdigit() and not firstS:
                        if 1900 < int(s) < 3000:
                            year = int(s)
                            break
                    else:
                        firstS = False
                        name += str(s) + ' '
                        continue
                if name.endswith(' '):
                    name = name[0:-1]
                folder_name = str(modelCreator.get())
                if list(willRemove.state())[1]:
                    folder_name = folder_name.replace('{year}', "(" + str(year) + ")")
                else:
                    folder_name = folder_name.replace('{year}', str(year))
                folder_name = folder_name.replace('{name}', str(name))
                newDir = chooseDirString
                newDir = newDir + "\\" + folder_name
                try:
                    os.mkdir(newDir)
                except OSError:
                    print(OSError)

                os.rename(os.path.join(chooseDirString, file), newDir + "\\" + file)

        if list(willRename.state())[0] == 1:
            folders = []
            for r, d, f in os.walk(chooseDirString):
                for folder in d:
                    folders.append(os.path.join(r, folder))
            for f in folders:
                mkvName = ""
                for file in os.listdir(f):
                    if file.lower().endswith(".mkv"):
                        mkvName = file.replace(".mkv", ".srt")
                        break
                    else:
                        continue
                for file in os.listdir(f):
                    if file.lower().endswith(".srt"):
                        try:
                            os.rename(os.path.join(f, file), f + "\\" + mkvName)
                        except FileExistsError:
                            print('Multiple subtitle')
                        break
                    else:
                        continue
        import ctypes
        ctypes.windll.user32.MessageBoxW(0, completeMessage, infoText, 0)


    import ctypes


    btn = Button(root, textvariable=chooseDirVar, command=chooseDir).pack(side=TOP, fill='both')
    Button(root , text=unfolderString, command=openAll).pack(side=TOP,fill=X)
    chooseDirVar.set(chooseDirText)
    Frame(root, width=10, height=1, bd=0).pack(side=LEFT)
    Frame(root, width=10, height=1, bd=0).pack(side=RIGHT)
    Frame(root, width=5, height=5, bd=0).pack(side=TOP, fill=X)
    Button(root, text=quitText, command=root.quit).pack(side=last)
    Button(root, textvariable=numberOfFilesVar, command=createFolder).pack(side=first)
    Frame(root, width=1, height=35, bd=0).pack(side=BOTTOM, fill=X)
    root.title(nameOfProgram)
    root.mainloop()
