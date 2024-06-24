# Program To Read video and Extract Frames 
  
import cv2 
  
# Function to extract frames 
def FrameCapture(path): 
    cam = cv2.VideoCapture(path)

    frameno = 0
    while(True):
        ret, frame = cam.read()
        if ret:
            # if video is still left continue creating images
            name = path[:-4] + '_frame_' + str(frameno) + '.jpg'
            print ('new frame captured...' + name)

            cv2.imwrite(name, frame)
            frameno += 1
        else:
            break

    cam.release()
    cv2.destroyAllWindows()

# Driver Code 
if __name__ == '__main__': 
  
    paths1 = ['C:\\Users\\Marusa\\Documents\\Faks MAG 1\\VID (Robotski vid)\\Izziv_VID\\Slike_skatle\\20240503_214522.mp4',
            'C:\\Users\\Marusa\\Documents\\Faks MAG 1\\VID (Robotski vid)\\Izziv_VID\\Slike_skatle\\20240503_214559.mp4',
            'C:\\Users\\Marusa\\Documents\\Faks MAG 1\\VID (Robotski vid)\\Izziv_VID\\Slike_skatle\\20240503_214631.mp4',
            'C:\\Users\\Marusa\\Documents\\Faks MAG 1\\VID (Robotski vid)\\Izziv_VID\\Slike_skatle\\20240503_214643.mp4',
            'C:\\Users\\Marusa\\Documents\\Faks MAG 1\\VID (Robotski vid)\\Izziv_VID\\Slike_skatle\\20240503_214726.mp4',
            'C:\\Users\\Marusa\\Documents\\Faks MAG 1\\VID (Robotski vid)\\Izziv_VID\\Slike_skatle\\20240503_214812.mp4',
            'C:\\Users\\Marusa\\Documents\\Faks MAG 1\\VID (Robotski vid)\\Izziv_VID\\Slike_skatle\\20240503_214842.mp4',
            'C:\\Users\\Marusa\\Documents\\Faks MAG 1\\VID (Robotski vid)\\Izziv_VID\\Slike_skatle\\20240503_214856.mp4',
            'C:\\Users\\Marusa\\Documents\\Faks MAG 1\\VID (Robotski vid)\\Izziv_VID\\Slike_skatle\\20240503_214907.mp4',
            'C:\\Users\\Marusa\\Documents\\Faks MAG 1\\VID (Robotski vid)\\Izziv_VID\\Slike_skatle\\20240503_215004.mp4',
            'C:\\Users\\Marusa\\Documents\\Faks MAG 1\\VID (Robotski vid)\\Izziv_VID\\Slike_skatle\\20240503_215024.mp4',
            'C:\\Users\\Marusa\\Documents\\Faks MAG 1\\VID (Robotski vid)\\Izziv_VID\\Slike_skatle\\20240503_215037.mp4',
            'C:\\Users\\Marusa\\Documents\\Faks MAG 1\\VID (Robotski vid)\\Izziv_VID\\Slike_skatle\\20240503_215050.mp4',
            'C:\\Users\\Marusa\\Documents\\Faks MAG 1\\VID (Robotski vid)\\Izziv_VID\\Slike_skatle\\20240503_215124.mp4',
            'C:\\Users\\Marusa\\Documents\\Faks MAG 1\\VID (Robotski vid)\\Izziv_VID\\Slike_skatle\\20240503_215142.mp4',
            'C:\\Users\\Marusa\\Documents\\Faks MAG 1\\VID (Robotski vid)\\Izziv_VID\\Slike_skatle\\20240503_215149.mp4',
            'C:\\Users\\Marusa\\Documents\\Faks MAG 1\\VID (Robotski vid)\\Izziv_VID\\Slike_skatle\\20240503_215220.mp4',
            'C:\\Users\\Marusa\\Documents\\Faks MAG 1\\VID (Robotski vid)\\Izziv_VID\\Slike_skatle\\20240503_215224.mp4',
            'C:\\Users\\Marusa\\Documents\\Faks MAG 1\\VID (Robotski vid)\\Izziv_VID\\Slike_skatle\\20240503_215329.mp4']
    

    paths2 = ['C:\\Users\\Marusa\\Documents\\Faks MAG 1\\VID (Robotski vid)\\Izziv_VID\\Slike_skatle\\20240503_215342.mp4',
            'C:\\Users\\Marusa\\Documents\\Faks MAG 1\\VID (Robotski vid)\\Izziv_VID\\Slike_skatle\\20240503_215446.mp4',
            'C:\\Users\\Marusa\\Documents\\Faks MAG 1\\VID (Robotski vid)\\Izziv_VID\\Slike_skatle\\20240503_215500.mp4',
            'C:\\Users\\Marusa\\Documents\\Faks MAG 1\\VID (Robotski vid)\\Izziv_VID\\Slike_skatle\\20240503_215510.mp4',
            'C:\\Users\\Marusa\\Documents\\Faks MAG 1\\VID (Robotski vid)\\Izziv_VID\\Slike_skatle\\20240503_215527.mp4',
            'C:\\Users\\Marusa\\Documents\\Faks MAG 1\\VID (Robotski vid)\\Izziv_VID\\Slike_skatle\\20240503_215601.mp4',
            'C:\\Users\\Marusa\\Documents\\Faks MAG 1\\VID (Robotski vid)\\Izziv_VID\\Slike_skatle\\20240503_215631.mp4',
            'C:\\Users\\Marusa\\Documents\\Faks MAG 1\\VID (Robotski vid)\\Izziv_VID\\Slike_skatle\\20240503_215642.mp4',
            'C:\\Users\\Marusa\\Documents\\Faks MAG 1\\VID (Robotski vid)\\Izziv_VID\\Slike_skatle\\20240503_215812.mp4',
            'C:\\Users\\Marusa\\Documents\\Faks MAG 1\\VID (Robotski vid)\\Izziv_VID\\Slike_skatle\\20240503_215822.mp4',
            'C:\\Users\\Marusa\\Documents\\Faks MAG 1\\VID (Robotski vid)\\Izziv_VID\\Slike_skatle\\20240503_215845.mp4',
            'C:\\Users\\Marusa\\Documents\\Faks MAG 1\\VID (Robotski vid)\\Izziv_VID\\Slike_skatle\\20240503_215857.mp4']

    # Calling the function 
    for path in paths1:
        FrameCapture(path)
