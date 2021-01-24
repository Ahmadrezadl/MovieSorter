import locale
from easysettings import EasySettings

settings = EasySettings("settings.conf")
if not settings.has_option('Language'):
    if locale.getdefaultlocale() == "fa_IR":
        settings.set("Language", "Persian")
    else:
        settings.set("Language", "English")
    settings.save()
if settings.get('Language') == 'Persian':
    nameOfProgram = "Movie Sorter"
    chooseFileName = "انتخاب فایل"
    quitText = 'خروج'
    startText = 'شروع دسته بندی'
    folderForEpisodes = 'فولدر سازی برای قسمت ها'
    putYearInBrackets = 'قرار دادن سال ساخت داخل پرانتز'
    moviesText = 'فیلم ها'
    seriesText = 'سریال ها'
    unfolderString = 'درووردن فایل ها از فولدر ها'
    infoText = 'درباره ما'
    nameFormat = ':فرمت اسم فایل'
    settingsText = ':تنظیمات'
    formatsText = ':فرمت ها'
    getAncher = 'e'
    first = 'right'
    last = 'left'
    chooseDirText = 'انتخاب فولدر مورد نظر'
    completeMessage = "دسته بندی انجام شد"
    nameChange = "هم اسم کردن فیلم و زیرنویس"
    changeLanguage = "English"
    exitText = "خروج"
    openText = "باز کردن"

else:
    nameOfProgram = "Movie Sorter"
    chooseFileName = "Choose Directory"
    quitText = 'Quit'
    startText = 'Start Grouping'
    folderForEpisodes = 'Folder for Episodes'
    putYearInBrackets = 'Put Year of Release Date in Brackets '
    moviesText = 'Movies'
    seriesText = 'Series'
    infoText = 'About Us'
    settingsText = 'Settings:'
    nameFormat = 'Name Format:'
    formatsText = ' Formats:'
    getAncher = 'w'
    first = 'left'
    last = 'right'
    unfolderString='Unfolder all folders'
    chooseDirText = 'Choose Folder Directory'
    completeMessage = "Completed!"
    nameChange = "Same Name for Subtitle and Movie"
    changeLanguage = "فارسی"
    exitText = "Exit"
    openText = "Open"