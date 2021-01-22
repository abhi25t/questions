color/grayscale images to videos with controllable frame rate

I am writing a function to create a video from images in a folder. 
I am able to do it seperately for grayscale or color but unable to generalize. 
Could you please help? 
Here is what I have written till now for grayscale images:

import cv2
import os

def images_to_video(images_folder, output_video_path, fps):
    images = [img for img in os.listdir(images_folder)]
    images.sort()
    frame = cv2.imread(os.path.join(images_folder, images[0]))
    height, width = frame.shape
    video = cv2.VideoWriter(output_video_path, 0, fps, (width,height))
    for image in images:
        video.write(cv2.imread(os.path.join(images_folder, image)))
    cv2.destroyAllWindows()
    video.release()

