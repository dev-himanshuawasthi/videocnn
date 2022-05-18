# Importing all necessary libraries
import cv2
import os

currentframe = 0
for i in range(25):
    for j in range(4):
        # Read the video from specified path
        path = r"C:\Users\himaw\Desktop\videocnn\Actions\train\boxing\person"+str(i+1)+"_boxing_d"+str(j+1)+"_uncomp.avi"
        vid = cv2.VideoCapture(path)

        try:

            # creating a folder named data
            if not os.path.exists('boxingimages'):
                os.makedirs('boxingimages')

        # if not created then raise error
        except OSError:
            print('Error: Creating directory of data')

        # frame
        

        while (True):

            # reading from frame
            success, frame = vid.read()

            if success:
                # continue creating images until video remains
                name = './boxingimages/frame' + str(currentframe) +'_'+str(i)+'_'+str(j)+ '.jpg'
                print('Creating...' + name)

                # writing the extracted images
                if currentframe%3==0:
                    cv2.imwrite(name, frame)

                # increasing counter so that it will
                # show how many frames are created
                currentframe += 1
            else:
                break

        # Release all space and windows once done
        vid.release()
        cv2.destroyAllWindows()


