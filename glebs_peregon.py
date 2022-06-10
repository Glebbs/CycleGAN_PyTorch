import cv2
import glob

folders = glob.glob('/media/vlad/20127138-1a35-451b-85c0-a84dbc12ae79/storage/gta5_2_real/cityscapes_images/val/*')
paths = []
for folder in folders:
    paths += glob.glob(folder + '/*')

print(len(paths))
for path in paths:
    img = cv2.imread(path)
    cv2.imwrite(path.replace('frankfurt', 'new').replace('lindau', 'new').replace('munster', 'new'), img)