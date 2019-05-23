import PyPDF2 as pd

filename = input("Enter path of the pdf file: \n")
file = open(filename, 'rb')
pdfReader = pd.PdfFileReader(file)

tried = 0

if not pdfReader.isEncrypted:
    print("This pdf file is not Encrypted! You can successfully open it!")

else:
    wordListFile = open('dictionary.txt', 'r')
    body = wordListFile.read().lower()
    words = body.split('\n')

    for i in range(len(words)):
        word = words[i]
        print('Trying Dencryption by:  {}'.format(word))
        result = pdfReader.decrypt(word)
        if result == 1:
            print('Dencryption Success! The password is: ' + word)
            break

        elif result == 0:
            tried += 1
            print("Password tried:  " + str(tried))
            continue