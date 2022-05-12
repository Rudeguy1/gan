import cv2
import os 

# read images
original = cv2.imread('orig.png')
translated = cv2.imread('trans.png')
reconstructed = cv2.imread('recon.png')

# resize images
dim = (512, 512)
og_r = cv2.resize(original, dim)
trans_r = cv2.resize(translated, dim)
recon_r = cv2.resize(reconstructed, dim)

# subtract images
trans_og_diff = cv2.subtract(trans_r, og_r)
trans_recon_diff = cv2.subtract(trans_r, recon_r)
og_recon_diff = cv2.subtract(og_r, recon_r)

# save images
directory = '/cvib2/apps/personal/swelland/sandbox/gan/cyclegan-ct-abdomen/img_samples'
path_1 = os.path.join(directory, 'trans_og_diff.png')
path_2 = os.path.join(directory, 'trans_recon_diff.png')
path_3 = os.path.join(directory, 'og_recon_diff.png')

if not os.path.isfile(path_1) or os.path.isfile(path_2) or os.path.isfile(path_3):
    cv2.imwrite(path_1, trans_og_diff)
    cv2.imwrite(path_2, trans_recon_diff)
    cv2.imwrite(path_3, og_recon_diff)

# show grayscale image # not working
# gray = cv2.cvtColor(og_r, cv2.COLOR_BGR2GRAY)
# cv2.imshow('og_trans_diff', gray)