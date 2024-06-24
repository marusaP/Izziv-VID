# https://github.com/ultralytics/ultralytics
# https://www.youtube.com/watch?v=Z-65nqxUdl4 

from ultralytics import YOLO

# Load a model
model = YOLO("C:\\Users\\Marusa\\Documents\\Faks MAG 1\\VID (Robotski vid)\\runs\\detect\\train4\\weights\\last.pt")  # build a new model from scratch

# Use the model
model.train(data="C:\\Users\\Marusa\\Documents\\Faks MAG 1\\VID (Robotski vid)\\Izziv_VID\\config.yaml", epochs=10)

results = model("C:\\Users\\Marusa\\Documents\\Faks MAG 1\\VID (Robotski vid)\\Izziv_VID\\test1\\20240503_214522_frame_112.jpg")  # predict on an image

#def main(input_folder_path, output_folder_path)
    # input: globinske in rgb slike 
    # output: kar hocemo, da pogleda
    # printe v txt file. 
    # lahko readme, da bo vedel, kaj naj naredi

    # uvod: pregled podrocja, problema (detekcija ovir v skladiscih je velik problem, 
    # mozne ovire so ... )
    # metodologija (podatki, algoritmi - v osnovi (arhitektura, parametri), metrike))
    # rezultati (suhoparni) model detektira to in to, na tej sliki je izpustil to in to
    # diskusija (zakaj je nas model najboljsi in smo resili svet)

print(results)  # print results to screen