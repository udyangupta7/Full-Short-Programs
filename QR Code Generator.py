try:
    import logging as lg
    lg.basicConfig(filename="logging.txt",
                   filemode='a',
                   format='%(asctime)s %(levelname)s -%(message)s',
                   datefmt='%Y-%m-%d %H:%M:%S')
    import pyqrcode
    import png
    from pyqrcode import QRCode
    QRstring = "https://www.youtube.com/watch?v=tcYodQoapMg"
    url = pyqrcode.create((QRstring))
    url.png('/Users/yudiudyan/Desktop/QR.png',scale = 4) #change scale for size change.
except (AttributeError, TypeError, ValueError, AssertionError, Exception, ArithmeticError) as e:
    print("Error is: \n", e)
    lg.error("Error found in the code. Pl rectify and try again.")