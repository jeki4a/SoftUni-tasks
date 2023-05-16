import pyqrcode
import png
from pyqrcode import QRCode

address = 'https://iplogger.com/21Ka93'
url = pyqrcode.create(address)
url.png('hacked.png', scale=8)





