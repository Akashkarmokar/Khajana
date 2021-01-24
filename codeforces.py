import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
from folderStructureMaker import *
from extension import *
from fileName import *

# Codeforces code parser function
def codeforces():
    user_handle = input("\nEnter your handle:")
    print("\n\nYour All code will be save in OJ named directory! \n")
    user_handle = user_handle.lower().strip()

    user_info = requests.get("https://codeforces.com/api/" + str("/user.info?handles=" + str(user_handle))).json()
    # print(user_info)
    count = 0
    if user_info['status'] == 'OK':
        submission_response = requests.get(
            "https://codeforces.com/api/user.status?handle=" + str(user_handle) + "&from=1", timeout=10).json()
        # print(submission_response)
        all_submission_data = submission_response['result']
        total_submission = len(all_submission_data)
        # print("Total Submission : ", total_submission)
        print(
            "\nPlease wait some times.It take some moments.If it face some problem to parse your accepted code it will say - something is wrong\n\n")

        # making folder structure
        make_folder(user_handle, 1)

        # custom set for check duplicate problem
        my_set = set()
        ok = 0
        for each_submission in all_submission_data:
            if each_submission['verdict'] == "OK":
                ok += 1
                try:
                    title = str(each_submission['problem']['index'] + "_" + each_submission['problem']['name']).strip()
                    submission_id = each_submission['id']
                    contest_id = each_submission['contestId']

                    temp_problem_name = str(contest_id) + str(each_submission['problem']['index'])
                    if temp_problem_name not in my_set:
                        my_set.add(temp_problem_name)
                        try:
                            uClient = urlopen(
                                "https://codeforces.com/contest/" + str(contest_id) + "/submission/" + str(
                                    submission_id))
                            html_page = uClient.read()
                            uClient.close()
                            page_soup = BeautifulSoup(html_page, "html.parser")
                            submission_core_code = page_soup.find('pre', {'id': 'program-source-text'}).text

                            # File creating
                            if each_submission['programmingLanguage'] in extension:
                                code_extension = extension[each_submission['programmingLanguage']]
                            else:
                                code_extension = ".txt"

                            file_name = check_filename(title) + code_extension
                            new_file = open(file_name, 'w')
                            new_file.write(submission_core_code)
                            new_file.close()

                            print("---->: " + title + " _____________________________________________________Done.")

                            count = count + 1

                        except Exception as e:
                            print("---->: Something is wrong with " + title + "contest id->" + str(
                                contest_id) + "submission id->" + str(submission_id) + ".")

                except ConnectionError as e:
                    print("---->: Something is wrong with " + title + "contest id->" + str(
                        contest_id) + "submission id->" + str(submission_id) + ".")

        print("\n\nTotal Submission : ", total_submission)
        print("Total Accepted: ", ok)
        print("Total code back no :", count,
              " * For multiple submission of same problem we accept last one and don't count gym problem.")
        my_set.clear()

    else:
        print(str(user_info['comment']))

    return None
