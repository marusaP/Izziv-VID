import pyrealsense2 as rs
import numpy as np
import cv2 as cv



if __name__ == '__main__':
    # Initialize the RealSense pipeline
    pipeline = rs.pipeline()

    # Create a configuration object to specify which streams to enable
    config = rs.config()

    # Enable the color (RGB) stream
    config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 6)  # Resolution and frame rate

    # Enable the depth stream
    config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 6)  # Depth stream with 16-bit depth

    # Start the pipeline with the specified configuration
    pipeline.start(config)

    i = 0
    try:
        while True:
            i+=1
            # Wait for a coherent set of frames
            frames = pipeline.wait_for_frames()

            # Get the color frame
            color_frame = frames.get_color_frame()
            if not color_frame:
                continue

            # Convert the color frame to an OpenCV-compatible format
            color_image = np.asanyarray(color_frame.get_data())

            # Get the depth frame
            depth_frame = frames.get_depth_frame()
            if not depth_frame:
                continue

            # Visualize the color image
            cv.imshow('RealSense Color Stream', color_image)
            if i > 10: 
                # Save the color image
                name = './robolab/video10/color_image' + str(i-10) + '.png' 
                cv.imwrite(name, color_image)

                # Save the depth image
                depth_image = np.asanyarray(depth_frame.get_data())
                name = './robolab/video10/depth_image' + str(i-10) + '.png'
                cv.imwrite(name, depth_image.astype(np.uint16))

            # Break the loop if 'q' is pressed
            if cv.waitKey(1) & 0xFF == ord('q'):
                print(i)
                break

    finally:
        # Stop the pipeline
        pipeline.stop()

    # Release OpenCV resources
    cv.destroyAllWindows()
