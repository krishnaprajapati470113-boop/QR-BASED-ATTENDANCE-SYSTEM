import barcode
from barcode.writer import ImageWriter

student_id = "STU001"
code = barcode.get('code128', student_id, writer=ImageWriter())
code.save(f"barcodes/{student_id}")

print("Barcode Generated")
