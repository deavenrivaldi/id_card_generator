from PIL import Image, ImageDraw, ImageFont
import os


def generate_id_card(data):
    # Extract and preprocess inputs
    nik = data.get("nik")
    nama = data.get("name").upper()
    place_of_birth = data.get("place_of_birth").upper()
    date_of_birth = data.get("date_of_birth")
    ttl = f"{place_of_birth}, {date_of_birth}".strip(", ") if place_of_birth and date_of_birth else None

    gender = data.get("gender").upper()
    alamat = data.get("address").upper()
    rt = data.get("rt")
    rw = data.get("rw")
    rtrw = f"{rt}/{rw}".strip("/") if rt or rw else None

    keldes = data.get("village").upper()
    kecamatan = data.get("district").upper()
    agama = data.get("religion")
    status = data.get("marital_status")
    pekerjaan = data.get("occupation").upper()
    kewarganegaraan = data.get("nationality").upper()

    photo_path = data.get("photo_path")

    # Load the ID card template
    template_path = os.path.join(os.getcwd(), "image_asset", "KTP_Template.jpg")  # Adjust path as needed
    template = Image.open(template_path)
    draw = ImageDraw.Draw(template)

    # Define font and size (adjust the font path for your system)
    font_NIK = ImageFont.truetype("font_asset/arialbd.ttf", size=30)
    font = ImageFont.truetype("font_asset/arial.ttf", size=20)

    # Define positions for text areas
    positions = {
        "nik": (330, 197),
        "nama": (348, 242),
        "ttl": (348, 269),
        "gender": (348, 294),
        "alamat": (348, 320),
        "rtrw": (348, 345),
        "keldes": (348, 371),
        "kecamatan": (348, 396),
        "agama": (348, 422),
        "status": (348, 448),
        "pekerjaan": (348, 473),
        "kewarganegaraan": (348, 499),
    }

    # Text area dimensions
    text_area_width = 310
    text_area_height = 20
    gender_area_width = 175
    bg_color = (180, 208, 219)

    # Draw text only if value is provided
    for key, position in positions.items():
        if key == "ttl" and (not place_of_birth or not date_of_birth):
            continue  # Skip drawing for "ttl" if either place_of_birth or date_of_birth is missing

        value = eval(key)  # Dynamically get the variable by its key name
        if value:  # Only draw if the value is not None or empty
            width = gender_area_width if key == "gender" else text_area_width
            height = 30 if key == "nik" else text_area_height
            draw.rectangle([position, (position[0] + width, position[1] + height)], fill=bg_color)
            draw.text(position, value, font=font if key != "nik" else font_NIK, fill="black")

    # Insert photo only if provided
    if photo_path:
        photo = Image.open(photo_path)
        photo = photo.resize((210, 280))
        photo_position = (735, 204)
        template.paste(photo, photo_position)

    # Display the updated image
    #? template.show()
    return template

#? Example usage
'''web_data = {
    "nik": "3173062806020087",
    "name": "Cicila Margaretha",
    "place_of_birth": "Tangerang",
    "date_of_birth": "20-12-1990",
    "gender": "perempuan",
    "address": "Foresta BE 33/1",
    "rt": "003",
    "rw": "020",
    "village": "Poris Indah",
    "district": "Cipondoh",
    "religion": "Katholik",
    "marital_status": "Belum Kawin",
    "occupation": "Pegawai Swasta",
    "nationality": "WNI",
    "photo_path": "idCard Generator/image_asset/cicil.jpg"
}

generate_id_card(web_data)'''
