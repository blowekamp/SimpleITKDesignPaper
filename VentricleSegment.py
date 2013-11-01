import SimpleITK as sitk
from showimg import showimg, showimg3d

# Load the MRI volumes
img_T1 = sitk.ReadImage("Data/nac-brain-atlas-1.0/volumes/A1_grayT1.nrrd")
img_T2 = sitk.ReadImage("Data/nac-brain-atlas-1.0/volumes/A1_grayT2.nrrd")

# Convert the volumes to 8-bit grayscale
img_T1_255 = sitk.Cast(sitk.RescaleIntensity(img_T1), sitk.sitkUInt8)
img_T2_255 = sitk.Cast(sitk.RescaleIntensity(img_T2), sitk.sitkUInt8)

# Extract and display an axial slice from each volume
yslice_T1 = img_T1_255[:,115,:]
yslice_T2 = img_T2_255[:,115,:]
showimg(yslice_T1, dpi=30, title="t1image")
showimg(yslice_T2, dpi=30, title="t2image")

# Create a vector volume from T1 and T2
img_multi = sitk.Compose(img_T1, img_T2)

# Create 2 seed points for the region finding
seeds = [ [112,116,125], [110,120,132]  ]

# Create a seed point volume
seedimg = sitk.Image(img_T1.GetSize(), sitk.sitkUInt8)
seedimg.CopyInformation(img_T1)
seedimg[seeds[0]] = 1
seedimg[seeds[1]] = 1
seedimg = sitk.BinaryDilate(seedimg, 3)

# Display the seed point volume
showimg3d( sitk.LabelOverlay(img_T1_255, seedimg),
           zslices=range(seeds[0][2]-3, seeds[1][2]+3, 3),
           dpi=15, title="initialseed" )

# Perform the region based segmentation
seg = sitk.VectorConfidenceConnected(img_multi, seeds, numberOfIterations=2, multiplier=4.5)

# Apply a median filter to the segmentation
seg = sitk.BinaryMedian(seg, [3,3,3])

# Display an overlay image with a contour of the segmented ventricle
overlayed = sitk.LabelOverlay(img_T1_255, sitk.LabelContour(seg))
mysize = img_T1.GetSize()
showimg3d( overlayed, yslices=range(100,mysize[1]-100,15),
        zslices=range(100,mysize[2]-100,15), dpi=30, title="segmentation" )

