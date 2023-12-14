from PIL import Image
import os

def convert_heic_to_jpg(heic_input_folder, jpg_output_folder):
    
    #Create output folder if doesn't exist
    if not os.path.exists(jpg_output_folder):
        os.makedirs(jpg_output_folder)
    
    for heic_file in heic_input_folder:
        if heic_file.endswith('.heic'):
            
            #Open HEIC image
            heic_image = Image.open(heic_file)
            
            #Convert and save as JPG
            jpg_output_path = os.path.join(jpg_output_folder, os.path.splitext(os.path.basename(heic_file))[0] + ".jpg")
            heic_image.convert("RGB").save(jpg_output_path, "JPEG")
            
            print(f"Conversion succesful, saved as {jpg_output_path}")

heic_input_folder = "path"
jpg_output_folder = "path"

convert_heic_to_jpg(heic_input_folder, jpg_output_folder)