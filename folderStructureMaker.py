import os

# This function make folder structure
def make_folder(user_handle,num):
    if num == 1:
        if not os.path.exists(os.getcwd() + '\\' + 'codeforces'):
            os.mkdir('codeforces')
        os.chdir(os.getcwd() + '\\' + 'codeforces')
    if not os.path.exists(os.getcwd() + '\\' + user_handle):
        os.makedirs(user_handle)
    os.chdir(os.getcwd() + '\\' + user_handle)

    return None