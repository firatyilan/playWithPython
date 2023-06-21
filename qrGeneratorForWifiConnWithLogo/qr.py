import qrcode
from PIL import Image

def generate_wifi_qrcode_with_logo(ssid, password, logo_path, output_path):
    wifi_data = f"WIFI:S:{ssid};T:WPA;P:{password};;"
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=80, border=1)
    qr.add_data(wifi_data)
    qr.make(fit=True)
    qr_image = qr.make_image(fill_color="black", back_color="white")

    # Logo görüntüsünü aç
    logo_image = Image.open(logo_path)
    logo_width, logo_height = logo_image.size

    # Logo boyutunu ayarla
    logo_max_size = min(qr_image.size) // 4
    if logo_width > logo_max_size or logo_height > logo_max_size:
        logo_image = logo_image.resize((logo_max_size, logo_max_size), Image.LANCZOS)

    # Logo görüntüsünü QR kodunun ortasına yerleştir
    qr_width, qr_height = qr_image.size
    logo_position = ((qr_width - logo_image.width) // 2, (qr_height - logo_image.height) // 2)
    qr_image.paste(logo_image, logo_position)

    # QR kodunu kaydet
    qr_image.save(output_path)

# WiFi bilgilerini ve logo dosya yolunu burada değiştirin
ssid = "Misafir"
password = "Msfr123654mM!*"
logo_path = "karacaLogo.png"
output_path = "karacaQR.png"


generate_wifi_qrcode_with_logo(ssid, password, logo_path, output_path)
