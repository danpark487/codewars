# You will create 2 string methods:

#     isAudio/is_audio, matching 1 or + uppercase/lowercase letter(s) (combination possible), with the extension .mp3, .flac, .alac, or .aac.

#     isImage/is_image, matching 1 or + uppercase/lowercase letter(s) (combination possible), with the extension .jpg, .jpeg, .png, .bmp, or .gif.

# Note that this is not a generic image/audio files checker. It's meant to be a test for Bill's files only. Bill doesn't like punctuation. He doesn't like numbers, neither. Thus, his filenames are letter-only

# Rules

#     It should return true or false, simply.
#     File extensions should consist of lowercase letters and numbers only.
#     File names should consist of letters only (uppercase, lowercase, or both)


def is_audio(file_name):
    audioExtensions = {"mp3" , "flac" , "alac" , "aac"}
    file_name = file_name.split(".") 
    if len(file_name) != 2: # returns False if input had multiple periods (e.g., abc.jpeg.jpeg)
        return False
    name = file_name[0]
    ext = file_name[1]
    return name.isalpha() and ext in audioExtensions

def is_img(file_name):
    imageExtensions = {"jpg" , "jpeg" , "png" , "bmp" , "gif"}
    file_name = file_name.split(".")
    if len(file_name) != 2:
        return False
    name = file_name[0]
    ext = file_name[1]
    return name.isalpha() and ext in imageExtensions