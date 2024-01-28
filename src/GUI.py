import ctypes
import os
import sys
from tkinter import *
from tkinter import messagebox, filedialog
from load_language import *
from logic import create_folders_for_files, move_files_to_root_and_remove_empty_dirs


def choose_dir():
    Tk().withdraw()
    global choose_dir_string
    choose_dir_string = filedialog.askdirectory(title=chooseFileName)
    if len(choose_dir_string) < 57:
        choose_dir_var.set(choose_dir_string)
    else:
        choose_dir_var.set(choose_dir_string[0:10] + "..." + choose_dir_string[-42:])
    if choose_dir_string == "":
        choose_dir_var.set(chooseDirText)
    global number_of_files
    number_of_files = 0

    for file in os.listdir(choose_dir_string):
        if file.lower().endswith(".mkv") and var_mkvFormat:
            number_of_files += 1
        elif file.lower().endswith(".mp4") and var_mp4Format:
            number_of_files += 1
        elif file.lower().endswith(".avi") and var_aviFormat:
            number_of_files += 1
        elif file.lower().endswith(".srt") and var_srtFormat:
            number_of_files += 1
        elif file.lower().endswith(".zip") and var_zipFormat:
            number_of_files += 1


    number_of_files_var.set(startGrouping.replace("{0}",str(number_of_files)))


def about():
    ctypes.windll.user32.MessageBoxW(0, "An App By: Ahmadrezadl\nVersion 2.0.0", infoText, 0)


def change_language_event():
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
        base_path = os.path.abspath("..")
    return os.path.join(base_path, relative_path)

def un_folder_button_action(choose_dir_string):
    answer = messagebox.askyesno(unfolderString,
                                 areYouSureUnfolder)
    if answer:
        move_files_to_root_and_remove_empty_dirs(choose_dir_string)
        messagebox.showinfo(done,unfoldered)




if __name__ == '__main__':
    root = Tk()
    var_mkvFormat = BooleanVar()
    var_mp4Format= BooleanVar()
    var_aviFormat= BooleanVar()
    var_srtFormat= BooleanVar()
    var_zipFormat= BooleanVar()
    var_sameName= BooleanVar()
    var_serialFiles= BooleanVar()
    var_movieFiles= BooleanVar()
    var_episodeFolders =  BooleanVar()
    root.resizable(False, False)
    menubar = Menu(root)
    sub_menu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="File", menu=sub_menu)
    sub_menu.add_command(label=openText, command=choose_dir)
    sub_menu.add_command(label=exitText, command=root.quit)
    root.config(menu=menubar)

    sub_menu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Help", menu=sub_menu)
    sub_menu.add_command(label=infoText, command=about)
    sub_menu.add_command(label=changeLanguage, command=change_language_event)
    root.iconbitmap(resource_path('resources/Logo.ico'))

    Label(root, text=nameFormat, anchor=getAncher).pack(side=TOP, fill='both')
    format_string = StringVar()
    format_string.set("{name} ({year})")
    format_text_field = Entry(root, textvariable=format_string, font="Arial 15")
    format_text_field.pack(side=TOP, fill=X)

    Label(root, text=settingsText, anchor=getAncher).pack(side=TOP, fill='both')

    folder_episodes_check_button = Checkbutton(root, text=folderForEpisodes, anchor=getAncher, var=var_episodeFolders)
    folder_episodes_check_button.pack(side=TOP, fill=X)

    # putYearInBracketsCheckButton = Checkbutton(root, text=putYearInBrackets,anchor=getAncher,var=var_yearInBracket)
    # putYearInBracketsCheckButton.pack(side=TOP, fill=X)
    # putYearInBracketsCheckButton.select()

    same_name = Checkbutton(root, text=nameChange, anchor=getAncher, var=var_sameName)
    same_name.pack(side=TOP, fill=X)
    same_name.select()


    Frame(root, width=1, height=1, highlightbackground="black", highlightcolor="black", highlightthickness=3,
                  bd=0).pack(side=TOP, fill=X)

    Label(root, text=formatsText, anchor=getAncher).pack(side=TOP, fill='both')

    formats = Frame(root)
    movies_check_button = Checkbutton(formats, text=moviesText, anchor=getAncher, var=var_movieFiles)
    movies_check_button.pack(side=LEFT)
    movies_check_button.select()

    series_check_button = Checkbutton(formats, text=seriesText, anchor=getAncher, var=var_serialFiles)
    series_check_button.pack(side=LEFT)
    series_check_button.select()

    mkv_check_button = Checkbutton(formats, text="mkv", anchor=getAncher, var=var_mkvFormat)
    mkv_check_button.pack(side=LEFT)
    mkv_check_button.select()

    srt_check_button = Checkbutton(formats, text="srt", anchor=getAncher, var=var_srtFormat)
    srt_check_button.pack(side=LEFT)
    srt_check_button.select()

    mp4_check_button = Checkbutton(formats, text="mp4", anchor=getAncher, var=var_mp4Format)
    mp4_check_button.pack(side=LEFT)
    mp4_check_button.select()

    avi_check_button = Checkbutton(formats, text="avi", anchor=getAncher, var=var_aviFormat)
    avi_check_button.pack(side=LEFT)
    avi_check_button.select()

    zip_check_button = Checkbutton(formats, text="zip", anchor=getAncher, var=var_zipFormat)
    zip_check_button.pack(side=LEFT)

    formats.pack(side=TOP, fill=X,anchor=getAncher)


    Frame(root, width=1, height=1, highlightbackground="black", highlightcolor="black", highlightthickness=3,
          bd=0).pack(side=TOP, fill=X)
    choose_dir_var = StringVar()
    choose_dir_string = ""
    number_of_files = 0
    number_of_files_var = StringVar()
    number_of_files_var.set(startText)
    btn = Button(root, textvariable=choose_dir_var, command=choose_dir).pack(side=TOP, fill='both')
    Button(root, text=unfolderString, command=lambda: un_folder_button_action(choose_dir_string)).pack(side=TOP, fill=X)
    choose_dir_var.set(chooseDirText)
    Frame(root, width=10, height=1, bd=0).pack(side=LEFT)
    Frame(root, width=10, height=1, bd=0).pack(side=RIGHT)
    Frame(root, width=5, height=5, bd=0).pack(side=TOP, fill=X)
    Button(root, text=quitText, command=root.quit).pack(side=last)
    Button(root, textvariable=number_of_files_var, command=lambda :create_folders_for_files(choose_dir_string, format_string.get(), var_mkvFormat, var_mp4Format, var_aviFormat, var_srtFormat, var_zipFormat, var_sameName, var_serialFiles, var_movieFiles, var_episodeFolders)).pack(side=first)
    Frame(root, width=1, height=35, bd=0).pack(side=BOTTOM, fill=X)
    root.title(nameOfProgram)
    root.mainloop()

