CMAKE_MINIMUM_REQUIRED(VERSION 2.6)

PROJECT(SimpleITKDesign NONE)

INCLUDE(UseLATEX.cmake)

file(COPY filter.h itkGaussianExample.cxx DESTINATION ${CMAKE_BINARY_DIR})

ADD_LATEX_DOCUMENT(frontiers.tex
  IMAGES logo1.jpg logo2.eps
  BIBFILES SimpleITKDesign.bib
  DEPENDS itkGaussianExample.cxx
  DEFAULT_PDF
  )
