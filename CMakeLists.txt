CMAKE_MINIMUM_REQUIRED(VERSION 2.6)

PROJECT(SimpleITKDesign NONE)

INCLUDE(UseLATEX.cmake)

set(src_files
  filter.h
  itkGaussianExample.cxx
  GoldBeadsSegmentation.py
  )
file(COPY ${src_files} DESTINATION ${CMAKE_BINARY_DIR})

ADD_LATEX_DOCUMENT(frontiers.tex
  IMAGES logo1.jpg logo2.eps
  IMAGE_DIRS images
  BIBFILES SimpleITKDesign.bib
  DEPENDS ${src_files}
  DEFAULT_PDF
  )
