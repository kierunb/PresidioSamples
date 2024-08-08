from presidio_image_redactor import ImageRedactorEngine
from PIL import Image

image = Image.open("./img/excel-phone-numbers.png")

redactor = ImageRedactorEngine()
redacted_image = redactor.redact(image=image)

redacted_image.save("./img/redacted-excel-phone-numbers.png")

print("Done.")
