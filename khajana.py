
from extension import *
from folderStructureMaker import *
from fileName import *
from codeforces import *
from atcoder import *

print(
    """\n\n    Welcome to Tetul-Monta Terminal Version:

    [ Available extensions for python,Java,Kotlin,C/C++.For other language it makes text file only. ]

    """)



flag = True
while flag:
    print("""Available Online judges are:
    1. Codeforces
    2. Atcoder( *It is no available now.)""")
    selection_no = int(input("\nEnter online judge no (press 0 to exit) : "))
    if selection_no > 0 and selection_no < 3:
        if selection_no == 1:
            codeforces()
        if selection_no == 2:
            atcoder()
    elif selection_no == 0:
        flag = False
    else:
        print("\nYou Enter a wrong input.\nEnter again ........\n")
