import base64
import os
from io import BytesIO
from flask import Flask, request, render_template, redirect, url_for, jsonify
from idCard_generator2 import generate_id_card  # Import your function



app = Flask(__name__)
UPLOAD_FOLDER = "uploads/"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('form.html')

@app.route("/generate", methods=["GET", "POST"])
def generate():
    print(app.url_map)
    if request.method == "POST":
        # Collect form data
        nik = request.form.get("nik")
        nama = request.form.get("nama")
        place_of_birth = request.form.get("birthplace")
        date_of_birth = request.form.get("dob")
        gender = request.form.get("kelamin")
        address = request.form.get("alamat")
        rt = request.form.get("rt")
        rw = request.form.get("rw")
        rtrw = f"{rt}/{rw}".strip("/") if rt or rw else None
        village = request.form.get("keldes")
        district = request.form.get("kecamatan")
        religion = request.form.get("agama")
        marital_status = request.form.get("status")
        occupation = request.form.get("pekerjaan")
        nationality = request.form.get("kewarganegaraan")
        photo = request.files.get("foto")

        # Save the uploaded photo
        photo_path = None
        if photo:
            photo_path = os.path.join(app.config["UPLOAD_FOLDER"], photo.filename)
            photo.save(photo_path)

        # Prepare data dictionary
        data = {
            "nik": nik,
            "name": nama,
            "place_of_birth": place_of_birth,
            "date_of_birth": date_of_birth,
            "gender": gender,
            "address": address,
            "rt": rt,
            "rw": rw,
            "village": village,
            "district": district,
            "religion": religion,
            "marital_status": marital_status,
            "occupation": occupation,
            "nationality": nationality,
            "photo_path": photo_path,
        }

        # Call the generate_id_card function to generate the ID card
        generated_image = generate_id_card(data)
        
        # Convert the image to base64 for easy embedding in HTML
        buffered = BytesIO()
        generated_image.save(buffered, format="JPEG")
        img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')

        # Return the base64-encoded image to the client
        return jsonify({'image': img_str})
    
        #? return redirect(url_for("success"))

#? Success page (optional)
'''@app.route("/success")
def success():
    return "ID card generated successfully!"'''


if __name__ == "__main__":
    app.run(debug=True)