import os
import re


def openAll(directory):
    if len(directory) < 2:
        return
    for root, dirs, files in os.walk(directory):
        for file in files:
            os.rename(os.path.join(root, file), directory + "\\" + file)
        if not os.listdir(root):
            os.rmdir(root)

def createFolder(directory,nameFormat,mkvFormat,mp4Format,aviFormat,srtFormat,zipFormat,yearInBracket,sameName,serialFiles,movieFiles,episodeFolders):
    for file in os.listdir(directory):
        if file.lower().endswith(".mkv") and mkvFormat:
            folder_name = file.replace(".mkv", "")
        elif file.lower().endswith(".mp4") and mp4Format:
            folder_name = file.replace(".mp4", "")
        elif file.lower().endswith(".avi") and aviFormat:
            folder_name = file.replace(".avi", "")
        elif file.lower().endswith(".srt") and srtFormat:
            folder_name = file.replace(".srt", "")
        elif file.lower().endswith(".zip") and zipFormat:
            folder_name = file.replace(".zip", "")
        else:
            continue
        folder_name = folder_name.replace(".", " ").replace("_", " ").replace("-", " ").replace("(", "").replace(")", "").replace("  ", " ")
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
        if serial and serialFiles:
            newDir = directory
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
            if episodeFolders:
                newDir = newDir + "\\" + episode
                try:
                    os.mkdir(newDir)
                except OSError:
                    print("Fucking Error")
                else:
                    print("Fucking Nice")
            os.rename(os.path.join(directory, file), newDir + "\\" + file)
        if (not serial) and movieFiles:
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
            folder_name = nameFormat
            if yearInBracket:
                folder_name = folder_name.replace('{year}', "(" + str(year) + ")")
            else:
                folder_name = folder_name.replace('{year}', str(year))
            folder_name = folder_name.replace('{name}', str(name))
            newDir = directory
            newDir = newDir + "\\" + folder_name
            try:
                os.mkdir(newDir)
            except OSError:
                print(OSError)

            os.rename(os.path.join(directory, file), newDir + "\\" + file)

    if sameName:
        folders = []
        for r, d, f in os.walk(directory):
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
