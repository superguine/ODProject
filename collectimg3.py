# import cv2
import os
import time
import subprocess
import sys
imp = 0

# Ensure OpenCV is installed
def install_opencv():
    try:
        # Check if OpenCV is installed by trying to import it
        import cv2
        print("OpenCV is already installed. Version:", cv2.__version__)
    except ImportError:
        print("OpenCV is not installed. Installing now...")
        try:
            # Install OpenCV using pip
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'opencv-python'])
            print("OpenCV has been installed successfully.")
            imp = 1
            # Attempt to import again after installation
            import cv2
            print("OpenCV is installed. Version:", cv2.__version__)
        except subprocess.CalledProcessError:
            print("Failed to install OpenCV. Please try installing it manually.")


if imp == 1:
    import cv2
else:
    install_opencv()
    import cv2
#############################################################################
'''
         You have to make changes below according to your requirement.
'''
##############################################################################
# Change the camera index if needed.  0 for default laptop webcam.
cam_index = 1


#-------------------------------------------------------------------
'''                                                                        
Sample image saving directory....                                          
        main_dir                                                           
            |                                                              
            |___ obj1                                                      
            |       |                                                      
            |       |____ obj1_img_1.jpg                                   
            |       |____ obj1_img_2.jpg                                   
            |       |____ ....                                             
            |                                                              
            |____ obj2                                                     
            |       |                                                      
            |       |____ obj2_img_1.jpg                                   
            |       |____ obj2_img_2.jpg                                   
            |       |____ ....                                             
            ⋮                                                              
'''
# ------------------------------------------------------------------
# Main directory for saving images (eg:testcollect)
main_dir = 'testcollect'
'''
            # NOTE: for single object/class, main_dir will be 'collected_imgs'
'''
# ------------------------------------------------------------------
# Labels / objets /class  (eg: ['obj1','obj2']  )
labels = ['mango_leaf_e']

# ------------------------------------------------------------------
# number of images per object /class
number_imgs = 3

##
##
##############################################################################



collected_imgs = 'collected_imgs'

if len(labels) > 1:
    # This will create the directory structure if it doesn't exist
    IMAGES_PATH = os.path.join(os.getcwd(), collected_imgs, main_dir)
else:
    main_dir = 'collected_imgs'
    # This will create the directory structure if it doesn't exist
    IMAGES_PATH = os.path.join(os.getcwd(), main_dir)


# Create the main directory if it doesn't exist
if not os.path.exists(IMAGES_PATH):
    os.makedirs(IMAGES_PATH)


print('\n Starting image collection ...\n')

first= True

# Loop through labels and create subdirectories
for label in labels:
    label_path = os.path.join(IMAGES_PATH, label)
    if not os.path.exists(label_path):
        os.makedirs(label_path)

    print('Collecting images for {}'.format(label))
    print('You will get 6 sec after taking each image for {}'.format(label))

    cap = cv2.VideoCapture(cam_index)
    time.sleep(6)
    counter = 1

    for imgnum in range(number_imgs):
        '''
        if first:
            print('Loading camera...')
            time.sleep(2)
            first=False
        '''
        time.sleep(6) # time between taking new image.
        print('Collecting image {}'.format(imgnum + 1))
        # cap = cv2.VideoCapture(0)  # 0 is usually the default camera index
        time.sleep(1)
        ret, frame = cap.read()  # Capture image from the camera

        if not ret:
            print("Failed to capture image")
            continue

        # time.sleep(1)
        cv2.imshow('frame', frame)

        # Save the image with a name
        imgname = os.path.join(IMAGES_PATH, label, '{}_img_{}.jpg'.format(label, counter))
        cv2.imwrite(imgname, frame)
        counter += 1
        print("DONE")
        # cap.release()
        #time.sleep(3)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
cv2.destroyAllWindows()

if len(labels) > 1:
    print(
        '\nAll images collected and the folders available at {}\\{}\\{}'.format(os.getcwd(), collected_imgs, main_dir))
else:
    print('\nAll images collected and the folder available at {}\\{}'.format(os.getcwd(), main_dir))

print('\nNow open "labelimg" in a virtual environment, & label those images')