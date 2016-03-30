from elaphe import barcode
def get_code39(info):
    bc = barcode('code39', info, options=dict(includetext=True), scale=3, margin=10)
    bc.save('code39.png', quality=95)
def get_QRcode(info):
    bc = barcode('QRcode', info, options=dict(version=9, eclevel='M'), margin=10, scale=5)
    bc.save('QRcode.png', quality=95)

choice = raw_input('''Choose what kind of code you want to generate(input a number):
1.Code39
2.QRcode
''')
info = raw_input("Input a string that you want to generate: ")
if int(choice)==1:
    try:
        get_code39(info)
        print "Done!"
    except:
        print "Error occurred!"
else:
    try:
        get_QRcode(info)
        print "Done!"
    except:
        print "Error occurred!"
