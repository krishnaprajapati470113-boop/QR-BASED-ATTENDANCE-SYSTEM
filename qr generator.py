import qrcode
import os

def generate_bulk_qr():
    # Students List (We Can add more students in this list)
    students = ["BTCS001,Ravi", "BTCS002,Sneha", "BTCS003,Sachin", "BTCS004,Rajesh"]
    
    # QR codes (folder fo save all QR )
    if not os.path.exists('student_qrs'):
        os.makedirs('student_qrs')

    for student in students:
        # QR Code generator
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(student)
        qr.make(fit=True)

        # Image making
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Save in system
        img.save(f"student_qrs/{student}.png")
        print(f"Generated: {student}.png")

if __name__ == "__main__":
    generate_bulk_qr()