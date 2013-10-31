import SimpleITK as sitk

img = sitk.ReadImage("Gold3nmInLensA.mrc")
sitk.Show(img)

median_img = sitk.Median(img, [1,1,1])
sitk.Show(median_img, "In-Median1")

m =  median_img > 160
# Grayscale is more efficient for this case, and produce the same results
m = sitk.GrayscaleErode(m, 6)
m = sitk.GrayscaleDilate(m, 2)

sitk.Show(sitk.LabelOverlay(img,m), "Mask")

markers = sitk.ConnectedComponent(m, fullyConnected=False)
del m

# increment all initial makers and add bg marker
markers += sitk.Cast(markers!=0, markers.GetPixelID())
# make a bg maker with 1 value
markers += sitk.Cast(median_img<50, markers.GetPixelID())
sitk.Show(sitk.LabelOverlay(img,markers), "Markers")

grad = sitk.GradientMagnitudeRecursiveGaussian(median_img, median_img.GetSpacing()[0])
ws = sitk.MorphologicalWatershedFromMarkers(grad, markers,
                                            markWatershedLine=False, fullyConnected=False)
ws -= sitk.Cast(ws==1, ws.GetPixelID())

sitk.Show(sitk.LabelOverlay(img,ws), "Segmentation")
sitk.WriteImage(ws,"gold_seg.mha")
slice=150
sitk.WriteImage(sitk.LabelOverlay(img,ws)[:,:,slice], "gold_seg.tiff")
sitk.WriteImage(img[:,:,slice], "gold.tiff")
