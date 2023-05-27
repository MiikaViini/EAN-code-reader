from PIL import Image
from pyzbar.pyzbar import decode


class EANReader():
    def __init__(self):
        # Load the image using PIL
        self.ean_codes = []
        image = Image.open('ean.jpg')
        rotated_image = image.rotate(90)

        # Convert the image to grayscale
        gray = image.convert('L')

        # Decode the barcode
        barcodes = decode(gray)

        # Extract the EAN code from the barcode
        for barcode in barcodes:
            ean = barcode.data.decode('utf-8')
            self.ean_codes.append(ean)