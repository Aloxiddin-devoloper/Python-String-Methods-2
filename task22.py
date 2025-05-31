#Task22: Elektron pochta domenini ajratib oling.
# Emaildan faqat domen qismini (ya’ni @ dan keyin) ajrating.
#input:  ali@gmail.com
#output: gmail.com

gmail = input("Gmailni kiriting :")

index = gmail.find("@")

found = gmail[index+1:]

print(found)