import sys
from Base import create_folders
from Host import generate_files,Change_the_files
from Template import convert_to_django_html, djangotemp
from Designer.BackGroundColor import *
from Designer.ForeGroundColor import *

if "--base" in sys.argv:
    create_folders()
elif "--vercelhost" in sys.argv:
    generate_files()
    Change_the_files()
elif "--inphtml" in sys.argv:
    convert_to_django_html(sys.argv[2],sys.argv[2])
elif "--djhtml" in sys.argv:
    djangotemp()
elif "--version" in sys.argv or "--V" in sys.argv or "--v" in sys.argv:
    print("-"*50)
    print("Version : "+green("0.0.1"))
    print("-"*50)