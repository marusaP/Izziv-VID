import cv2 as cv
import numpy as np
import open3d as o3d
import matplotlib.pyplot as plt
from icecream import ic
import time

def createPointCloud(iDepth, cut=True):
    '''
    funkcija za pretvorbo globinske slike v oblak tock
    
    input:
        - iDepth: globinska slika
        - cut: True (vzame le spodnjo polovico globinske slike)
               False (vzame celo globinsko sliko)
    
    output:
        - oPointCloud: oblak tock
    '''
    focal_length_x = 608 # fx
    focal_length_y = 608 # fy
    optical_center_x = 325 # cx
    optical_center_y = 241 # cy
    height = iDepth.shape[0]
    width = iDepth.shape[1]
    if cut:
        height = int(height / 2)
    oPointCloud = []
    R = np.array([[1, 0, 0],
                  [0, -1, 0],
                  [0, 0, -1]]) # rotacija okrog x osi za 180 stopinj
    zeroNo = 0
    for v in range(height):
        for u in range(width):
            if cut:
                z = iDepth[v + height, u]
            else:
                z = iDepth[v, u]
            x = (u - optical_center_x) * z / focal_length_x
            y = (v - optical_center_y) * z / focal_length_y
            if z < 3000:
                R_xyz = R @ np.array([x, y, z])
                oPointCloud.append([R_xyz[0], R_xyz[1], R_xyz[2], 0, 0, 0])
            else:
                oPointCloud.append([0, 0, 0, 0, 0, 0])
                zeroNo += 1
    return np.array(oPointCloud)

def pointCloud2RGB_new(iPointCloud, oShape, cut=True):
    '''
    funkcija za pretvorbo oblaka tock v 2D sliko

    input:
        - iPointCloud: oblak tock
        - oShape: velikost izhodne 2D slike
        - cut: True (oblak tock je bil ustvarjen iz spodnje polovice globinske slike)
               False (oblak tock je bil ustvarjen iz cele globinske slike)
        
    output:
        - oImage: projekcija oblaka tock na ravnino
    '''
    height = oShape[0]
    if cut:
        height = int(height / 2)
    width = oShape[1]

    oImage = np.zeros([height, width, 3], dtype='uint8')

    idx = 0
    points = iPointCloud.points
    colors = iPointCloud.colors

    for v in range(height):
        for u in range(width):
            point = points[idx]
            if (np.mean(point) != 0):
                oImage[v, u, :] = colors[idx] * 255
            else:
                oImage[v, u, :] = [0, 0, 0]
            idx += 1

    return oImage

def showImage(image, iTitle='', cmap='viridis'):
    plt.figure()
    plt.imshow(image, cmap=cmap) #cmap = barvna skala prikaza 2D slike
    plt.title(iTitle)
    plt.show()

if __name__ == '__main__':

    input_path = './testni_podatki/'
    out_path = './rezultati/'

    for i in range(690, 691, 1):
        #ic(i)

        if i < 10:
            name = 'image_000' + str(i) + '.png'
        elif i < 100:
            name = 'image_00' + str(i) + '.png'
        elif i < 1000:
            name = 'image_0' + str(i) + '.png'
        else:
            name = 'image_' + str(i) + '.png'

        path_depth = input_path + 'depth/' + name
        path_color = input_path + 'rgb/' + name
        #ic (path_depth)
        #ic (path_color)

        #nalaganje globinske in barvne slike
        img_depth = np.array(cv.imread(path_depth, cv.IMREAD_UNCHANGED))
        #img_color = np.array(cv.imread(path_color, cv.IMREAD_UNCHANGED))
        img_color = np.array(cv.imread(path_color, cv.IMREAD_COLOR))
        #img_color = cv.cvtColor(img_color, cv.COLOR_BGR2RGB)
        #showImage(img_color, iTitle='color', cmap='viridis')
        #ic(img_depth.dtype)
        ic(img_depth.shape)
        ic(img_color.shape)
        #ic('frame received')

        #point cloud iz spodnje polovice globinske slike
        point_cloud = createPointCloud(img_depth)
        #point cloud iz cele globinske slike
        point_cloud_full = createPointCloud(img_depth, cut=False)

        #point cloud iz spodnje polovice globinske slike
        o3d_point_cloud = o3d.geometry.PointCloud()
        o3d_point_cloud.points = o3d.utility.Vector3dVector(point_cloud[:, :3])
        #o3d_point_cloud.colors = o3d.utility.Vector3dVector(point_cloud[:, 3:])

        #point cloud iz cele globinske slike
        o3d_point_cloud_full = o3d.geometry.PointCloud()
        o3d_point_cloud_full.points = o3d.utility.Vector3dVector(point_cloud_full[:, :3])  # Convert float64 numpy array of shape (n, 3) to Open3D format.
        #o3d_point_cloud_full.colors = o3d.utility.Vector3dVector(point_cloud_full[:, 3:])

        #ic('point cloud created')

        #prikaz point clouda
        o3d.visualization.draw_geometries([o3d_point_cloud_full], 'Point Cloud')
        #o3d.visualization.draw_geometries([o3d_point_cloud], 'Point Cloud - polovica')

        #dolocanje barv tock v point cloudu
        o3d_point_cloud.colors = o3d.utility.Vector3dVector(point_cloud[:, 3:])
        o3d_point_cloud_full.colors = o3d.utility.Vector3dVector(point_cloud_full[:, 3:])
        
        #segmentacija ravnine (tal)
        plane_model, inliers = o3d_point_cloud.segment_plane(distance_threshold=25, ransac_n=3, num_iterations=1000)

        colors = np.array(o3d_point_cloud.colors)
        colors_full = np.array(o3d_point_cloud_full.colors)

        selection = np.zeros(len(colors), dtype=bool)
        selection[inliers] = True
        selection = ~selection

        delta = np.full(len(selection), True, dtype=bool) # array napolnjen z True
        selection_full = np.concatenate((delta, selection))
        
        #spreminajnje barve tock, ki lezijo izven ravnine
        new_colors = np.array([1, 0.6, 0])
        o3d_point_cloud.colors = o3d.utility.Vector3dVector(np.where(selection[:, np.newaxis], new_colors, colors))
        o3d_point_cloud_full.colors = o3d.utility.Vector3dVector(np.where(selection_full[:, np.newaxis], new_colors, colors_full))

        #ic('plane segmentation done')

        o3d.visualization.draw_geometries([o3d_point_cloud_full], 'Plane segmentation')
        
        test_new = pointCloud2RGB_new(o3d_point_cloud_full, img_depth.shape, cut=False)
        showImage(test_new, iTitle='test_new')

        gray = cv.cvtColor(test_new, cv.COLOR_RGB2GRAY)
        showImage(gray, iTitle='gray', cmap='gray')

        #jedri za filtriranje in morfoloske operacije
        SE = cv.getStructuringElement(cv.MORPH_ELLIPSE, (13, 13))
        SE0 = cv.getStructuringElement(cv.MORPH_ELLIPSE, (7, 7))

        #filtriranje slike
        blur = cv.filter2D(gray, -1, SE0)
        showImage(blur, iTitle='blur', cmap='gray')

        #morfolosko odpiranje slike
        openImg = cv.morphologyEx(blur, cv.MORPH_OPEN, SE, iterations=1)
        showImage(openImg, iTitle='open', cmap='gray')

        #Cannyjev detektor robov
        edged = cv.Canny(openImg, 30, 200)
        showImage(edged, iTitle='edges', cmap='gray')

        #iskanje obrisov objektov na sliki
        contours, hierarchy = cv.findContours(edged, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)

        #contours = sorted(contours, key=cv.contourArea, reverse=True)

        for contour in contours:
            if len(contour) > 50:
                mask = np.zeros_like(test_new)
                cv.drawContours(test_new, [contour], -1, (0, 255, 0), 2)

                (x, y, w, h) = cv.boundingRect(np.array(contour))
                cv.rectangle(test_new, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv.rectangle(img_depth, (x, y), (x + w, y + h), (255, 255, 255), 2)

                x_c = int(x + (w / 2) - 2)
                y_c = int(y + (h / 2) - 2)
                center = img_depth[y_c:y_c+5, x_c:x_c+5]

                cv.putText(test_new, str(np.mean(center)), (x_c, y_c), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                cv.putText(img_depth, str(np.mean(center)), (x_c, y_c), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        showImage(test_new, iTitle='ovire')
        showImage(img_depth, iTitle='ovire')

        #shranjevanje rezultatov
        out_path_seg = out_path + 'seg_' + name
        out_path_dep = out_path + 'dep_' + name
        cv.imwrite(out_path_seg, cv.cvtColor(test_new, cv.COLOR_BGR2RGB))
        cv.imwrite(out_path_dep, img_depth)
        
        