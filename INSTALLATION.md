Installation
--------------

openCV 3.0 is indeed compatible with Python 3+.
However, the install instructions are slightly different
between Python 2.7+ and Python 3+.


Install OpenCV 3 on Ubuntu 16.04 with either Python 2.7 or Python 3.5 bindings.
http://www.pyimagesearch.com/2016/10/24/ubuntu-16-04-how-to-install-opencv/



# Install OpenCV 3.2 and Python 2.7+ on Ubuntu 14.04 x64
http://www.pyimagesearch.com/2015/06/22/install-opencv-3-0-and-python-2-7-on-ubuntu/




[OpenCV3.2.0](https://github.com/opencv/opencv/releases/tag/3.2.0)


# Upgrate Python 2.7

```
sudo apt-get install build-essential checkinstall  
sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev  
```


```
cd /usr/src
sudo su
wget https://www.python.org/ftp/python/2.7.13/Python-2.7.13.tgz
tar xzf Python-2.7.13.tgz
rm -rf Python-2.7.13.tgz
cd Python-2.7.13
./configure
#make altinstall #make altinstall is used to prevent replacing the default python binary file /usr/bin/python.
make install
```

```
# python2.7 -V
Python 2.7.13
```
[REF](https://tecadmin.net/install-python-2-7-on-centos-rhel/)




#### Step 1: Update and Upgrade
```
sudo apt-get update
sudo apt-get upgrade
```

#### Step 2:  Now we need to install our developer tools:
```
sudo apt-get install build-essential cmake git pkg-config
```

#### Step 3: image I/O packages:
```
sudo apt-get install libjpeg8-dev libtiff4-dev libjasper-dev libpng12-dev
```
#### Step4 : GTK development library
```
sudo apt-get install libgtk2.0-dev
```
#### Step 5: processing video streams and accessing individual frames
```
sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
```
#### Step 6: Optimize various routines inside of OpenCV
```
sudo apt-get install libatlas-base-dev gfortran
```
#### Step 7: pip Python package manager
```
wget https://bootstrap.pypa.io/get-pip.py
sudo python get-pip.py
```
#### Step 8: Install virtualenv and virtualenvwrapper.
```
sudo pip install virtualenv virtualenvwrapper
sudo rm -rf ~/.cache/pip
```
```
vim ~/.bashrc
```

```
# virtualenv and virtualenvwrapper
export WORKON_HOME=$HOME/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh
```

```
source ~/.bashrc
```

#### Step 9:

$ sudo apt-get install python2.7-dev
$ pip install numpy


#### Step 10:



[OpenCV3.2.0](https://github.com/opencv/opencv/releases/tag/3.2.0)
cd ~
git clone https://github.com/Itseez/opencv.git
cd opencv
git checkout 3.2.0


cd ~
git clone https://github.com/Itseez/opencv_contrib.git
cd opencv_contrib
git checkout 3.2.0




cd ~/opencv
mkdir build && cd build
cmake -D CMAKE_BUILD_TYPE=RELEASE \
	-D CMAKE_INSTALL_PREFIX=/usr/local \
	-D INSTALL_C_EXAMPLES=ON \
	-D INSTALL_PYTHON_EXAMPLES=ON \
	-D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules \
	-D WITH_JPEG=OFF \
	-D BUILD_EXAMPLES=OFF ..


-D WITH_JPEG=OFF  to get rid of "Corrupt JPEG data: 1 extraneous bytes before marker 0xd6"
in OpenFace
http://privateblog.info/linux/opencv-i-corrupt-jpeg-data-na-linux/
http://stackoverflow.com/questions/15533338/opencv-error-on-ubuntu-webcam-logitech-c270-capture-highgui-error-v4l-v4l2





```
-- General configuration for OpenCV 3.2.0 =====================================
--   Version control:               3.2.0
--
--   Extra modules:
--     Location (extra):            /home/map479-admin/opencv_contrib/modules
--     Version control (extra):     3.2.0
--
--   Platform:
--     Timestamp:                   2017-04-19T15:31:13Z
--     Host:                        Linux 3.13.0-116-generic x86_64
--     CMake:                       2.8.12.2
--     CMake generator:             Unix Makefiles
--     CMake build tool:            /usr/bin/make
--     Configuration:               RELEASE
--
--   C/C++:
--     Built as dynamic libs?:      YES
--     C++ Compiler:                /usr/bin/c++  (ver 4.8.4)
--     C++ flags (Release):         -fsigned-char -W -Wall -Werror=return-type -Werror=non-virtual-dtor -Werror=address -Werror=sequence-point -Wformat -Werror=format-security -Wmissing-declarations -Wundef -Winit-self -Wpointer-arith -Wshadow -Wsign-promo -Wno-narrowing -Wno-delete-non-virtual-dtor -Wno-comment -fdiagnostics-show-option -Wno-long-long -pthread -fomit-frame-pointer -msse -msse2 -mno-avx -msse3 -mno-ssse3 -mno-sse4.1 -mno-sse4.2 -ffunction-sections -fvisibility=hidden -fvisibility-inlines-hidden -O3 -DNDEBUG  -DNDEBUG
--     C++ flags (Debug):           -fsigned-char -W -Wall -Werror=return-type -Werror=non-virtual-dtor -Werror=address -Werror=sequence-point -Wformat -Werror=format-security -Wmissing-declarations -Wundef -Winit-self -Wpointer-arith -Wshadow -Wsign-promo -Wno-narrowing -Wno-delete-non-virtual-dtor -Wno-comment -fdiagnostics-show-option -Wno-long-long -pthread -fomit-frame-pointer -msse -msse2 -mno-avx -msse3 -mno-ssse3 -mno-sse4.1 -mno-sse4.2 -ffunction-sections -fvisibility=hidden -fvisibility-inlines-hidden -g  -O0 -DDEBUG -D_DEBUG
--     C Compiler:                  /usr/bin/cc
--     C flags (Release):           -fsigned-char -W -Wall -Werror=return-type -Werror=non-virtual-dtor -Werror=address -Werror=sequence-point -Wformat -Werror=format-security -Wmissing-declarations -Wmissing-prototypes -Wstrict-prototypes -Wundef -Winit-self -Wpointer-arith -Wshadow -Wno-narrowing -Wno-comment -fdiagnostics-show-option -Wno-long-long -pthread -fomit-frame-pointer -msse -msse2 -mno-avx -msse3 -mno-ssse3 -mno-sse4.1 -mno-sse4.2 -ffunction-sections -fvisibility=hidden -O3 -DNDEBUG  -DNDEBUG
--     C flags (Debug):             -fsigned-char -W -Wall -Werror=return-type -Werror=non-virtual-dtor -Werror=address -Werror=sequence-point -Wformat -Werror=format-security -Wmissing-declarations -Wmissing-prototypes -Wstrict-prototypes -Wundef -Winit-self -Wpointer-arith -Wshadow -Wno-narrowing -Wno-comment -fdiagnostics-show-option -Wno-long-long -pthread -fomit-frame-pointer -msse -msse2 -mno-avx -msse3 -mno-ssse3 -mno-sse4.1 -mno-sse4.2 -ffunction-sections -fvisibility=hidden -g  -O0 -DDEBUG -D_DEBUG
--     Linker flags (Release):      
--     Linker flags (Debug):        
--     ccache:                      NO
--     Precompiled headers:         YES
--     Extra dependencies:          /usr/lib/x86_64-linux-gnu/libpng.so /usr/lib/x86_64-linux-gnu/libz.so /usr/lib/x86_64-linux-gnu/libtiff.so /usr/lib/x86_64-linux-gnu/libjasper.so /usr/lib/x86_64-linux-gnu/libjpeg.so /usr/lib/x86_64-linux-gnu/libImath.so /usr/lib/x86_64-linux-gnu/libIlmImf.so /usr/lib/x86_64-linux-gnu/libIex.so /usr/lib/x86_64-linux-gnu/libHalf.so /usr/lib/x86_64-linux-gnu/libIlmThread.so gtk-3 gdk-3 atk-1.0 gio-2.0 pangocairo-1.0 gdk_pixbuf-2.0 cairo-gobject pango-1.0 cairo gobject-2.0 glib-2.0 gthread-2.0 gstbase-1.0 gstreamer-1.0 dc1394 avcodec avformat avutil swscale vtkCommon vtkFiltering vtkImaging vtkGraphics vtkGenericFiltering vtkIO vtkRendering vtkVolumeRendering vtkHybrid vtkWidgets vtkParallel vtkInfovis vtkGeovis vtkViews vtkCharts dl m pthread rt
--     3rdparty dependencies:       libwebp libprotobuf
--
--   OpenCV modules:
--     To be built:                 core flann imgproc ml photo reg surface_matching video viz dnn freetype fuzzy imgcodecs shape videoio highgui objdetect plot superres ts xobjdetect xphoto bgsegm bioinspired dpm face features2d line_descriptor saliency text calib3d ccalib datasets rgbd stereo tracking videostab xfeatures2d ximgproc aruco optflow phase_unwrapping stitching structured_light python2
--     Disabled:                    world contrib_world
--     Disabled by dependency:      -
--     Unavailable:                 cudaarithm cudabgsegm cudacodec cudafeatures2d cudafilters cudaimgproc cudalegacy cudaobjdetect cudaoptflow cudastereo cudawarping cudev java python3 cnn_3dobj cvv hdf matlab sfm
--
--   GUI:
--     QT:                          NO
--     GTK+ 3.x:                    YES (ver 3.10.8)
--     GThread :                    YES (ver 2.40.2)
--     GtkGlExt:                    NO
--     OpenGL support:              NO
--     VTK support:                 YES (ver 5.8.0)
--
--   Media I/O:
--     ZLib:                        /usr/lib/x86_64-linux-gnu/libz.so (ver 1.2.8)
--     JPEG:                        /usr/lib/x86_64-linux-gnu/libjpeg.so (ver )
--     WEBP:                        build (ver 0.3.1)
--     PNG:                         /usr/lib/x86_64-linux-gnu/libpng.so (ver 1.2.50)
--     TIFF:                        /usr/lib/x86_64-linux-gnu/libtiff.so (ver 42 - 4.0.3)
--     JPEG 2000:                   /usr/lib/x86_64-linux-gnu/libjasper.so (ver 1.900.1)
--     OpenEXR:                     /usr/lib/x86_64-linux-gnu/libImath.so /usr/lib/x86_64-linux-gnu/libIlmImf.so /usr/lib/x86_64-linux-gnu/libIex.so /usr/lib/x86_64-linux-gnu/libHalf.so /usr/lib/x86_64-linux-gnu/libIlmThread.so (ver 1.6.1)
--     GDAL:                        NO
--     GDCM:                        NO
--
--   Video I/O:
--     DC1394 1.x:                  NO
--     DC1394 2.x:                  YES (ver 2.2.1)
--     FFMPEG:                      YES
--       avcodec:                   YES (ver 54.35.1)
--       avformat:                  YES (ver 54.20.4)
--       avutil:                    YES (ver 52.3.0)
--       swscale:                   YES (ver 2.1.1)
--       avresample:                NO
--     GStreamer:                   NO
--     OpenNI:                      NO
--     OpenNI PrimeSensor Modules:  NO
--     OpenNI2:                     NO
--     PvAPI:                       NO
--     GigEVisionSDK:               NO
--     Aravis SDK:                  NO
--     UniCap:                      NO
--     UniCap ucil:                 NO
--     V4L/V4L2:                    NO/YES
--     XIMEA:                       NO
--     Xine:                        NO
--     gPhoto2:                     NO
--
--   Parallel framework:            pthreads
--
--   Other third-party libraries:
--     Use IPP:                     9.0.1 [9.0.1]
--          at:                     /home/map479-admin/opencv/build/3rdparty/ippicv/ippicv_lnx
--     Use IPP Async:               NO
--     Use VA:                      NO
--     Use Intel VA-API/OpenCL:     NO
--     Use Lapack:                  NO
--     Use Eigen:                   YES (ver 3.2.0)
--     Use Cuda:                    NO
--     Use OpenCL:                  YES
--     Use OpenVX:                  NO
--     Use custom HAL:              NO
--
--   OpenCL:                        <Dynamic loading of OpenCL library>
--     Include path:                /home/map479-admin/opencv/3rdparty/include/opencl/1.2
--     Use AMDFFT:                  NO
--     Use AMDBLAS:                 NO
--
--   Python 2:
--     Interpreter:                 /home/map479-admin/.virtualenvs/cv/bin/python2.7 (ver 2.7.13)
--     Libraries:                   /usr/local/lib/libpython2.7.a (ver 2.7.13)
--     numpy:                       /home/map479-admin/.virtualenvs/cv/lib/python2.7/site-packages/numpy/core/include (ver 1.12.1)
--     packages path:               lib/python2.7/site-packages
--
--   Python 3:
--     Interpreter:                 /usr/bin/python3.4 (ver 3.4.3)
--
--   Python (for build):            /home/map479-admin/.virtualenvs/cv/bin/python2.7
--
--   Java:
--     ant:                         NO
--     JNI:                         /usr/lib/jvm/default-java/include /usr/lib/jvm/default-java/include /usr/lib/jvm/default-java/include
--     Java wrappers:               NO
--     Java tests:                  NO
--
--   Matlab:                        Matlab not found or implicitly disabled
--
--   Documentation:
--     Doxygen:                     NO
--
--   Tests and samples:
--     Tests:                       YES
--     Performance tests:           YES
--     C/C++ Examples:              NO
--
--   Install path:                  /usr/local
--
--   cvconfig.h is in:              /home/map479-admin/opencv/build
-- -----------------------------------------------------------------
--
-- Configuring done
-- Generating done
-- Build files have been written to: /home/map479-admin/opencv/build
-- General configuration for OpenCV 3.2.0 =====================================
--   Version control:               3.2.0
--
--   Extra modules:
--     Location (extra):            /home/map479-admin/opencv_contrib/modules
--     Version control (extra):     3.2.0
--
--   Platform:
--     Timestamp:                   2017-04-19T15:31:13Z
--     Host:                        Linux 3.13.0-116-generic x86_64
--     CMake:                       2.8.12.2
--     CMake generator:             Unix Makefiles
--     CMake build tool:            /usr/bin/make
--     Configuration:               RELEASE
--
--   C/C++:
--     Built as dynamic libs?:      YES
--     C++ Compiler:                /usr/bin/c++  (ver 4.8.4)
--     C++ flags (Release):         -fsigned-char -W -Wall -Werror=return-type -Werror=non-virtual-dtor -Werror=address -Werror=sequence-point -Wformat -Werror=format-security -Wmissing-declarations -Wundef -Winit-self -Wpointer-arith -Wshadow -Wsign-promo -Wno-narrowing -Wno-delete-non-virtual-dtor -Wno-comment -fdiagnostics-show-option -Wno-long-long -pthread -fomit-frame-pointer -msse -msse2 -mno-avx -msse3 -mno-ssse3 -mno-sse4.1 -mno-sse4.2 -ffunction-sections -fvisibility=hidden -fvisibility-inlines-hidden -O3 -DNDEBUG  -DNDEBUG
--     C++ flags (Debug):           -fsigned-char -W -Wall -Werror=return-type -Werror=non-virtual-dtor -Werror=address -Werror=sequence-point -Wformat -Werror=format-security -Wmissing-declarations -Wundef -Winit-self -Wpointer-arith -Wshadow -Wsign-promo -Wno-narrowing -Wno-delete-non-virtual-dtor -Wno-comment -fdiagnostics-show-option -Wno-long-long -pthread -fomit-frame-pointer -msse -msse2 -mno-avx -msse3 -mno-ssse3 -mno-sse4.1 -mno-sse4.2 -ffunction-sections -fvisibility=hidden -fvisibility-inlines-hidden -g  -O0 -DDEBUG -D_DEBUG
--     C Compiler:                  /usr/bin/cc
--     C flags (Release):           -fsigned-char -W -Wall -Werror=return-type -Werror=non-virtual-dtor -Werror=address -Werror=sequence-point -Wformat -Werror=format-security -Wmissing-declarations -Wmissing-prototypes -Wstrict-prototypes -Wundef -Winit-self -Wpointer-arith -Wshadow -Wno-narrowing -Wno-comment -fdiagnostics-show-option -Wno-long-long -pthread -fomit-frame-pointer -msse -msse2 -mno-avx -msse3 -mno-ssse3 -mno-sse4.1 -mno-sse4.2 -ffunction-sections -fvisibility=hidden -O3 -DNDEBUG  -DNDEBUG
--     C flags (Debug):             -fsigned-char -W -Wall -Werror=return-type -Werror=non-virtual-dtor -Werror=address -Werror=sequence-point -Wformat -Werror=format-security -Wmissing-declarations -Wmissing-prototypes -Wstrict-prototypes -Wundef -Winit-self -Wpointer-arith -Wshadow -Wno-narrowing -Wno-comment -fdiagnostics-show-option -Wno-long-long -pthread -fomit-frame-pointer -msse -msse2 -mno-avx -msse3 -mno-ssse3 -mno-sse4.1 -mno-sse4.2 -ffunction-sections -fvisibility=hidden -g  -O0 -DDEBUG -D_DEBUG
--     Linker flags (Release):      
--     Linker flags (Debug):        
--     ccache:                      NO
--     Precompiled headers:         YES
--     Extra dependencies:          /usr/lib/x86_64-linux-gnu/libpng.so /usr/lib/x86_64-linux-gnu/libz.so /usr/lib/x86_64-linux-gnu/libtiff.so /usr/lib/x86_64-linux-gnu/libjasper.so /usr/lib/x86_64-linux-gnu/libjpeg.so /usr/lib/x86_64-linux-gnu/libImath.so /usr/lib/x86_64-linux-gnu/libIlmImf.so /usr/lib/x86_64-linux-gnu/libIex.so /usr/lib/x86_64-linux-gnu/libHalf.so /usr/lib/x86_64-linux-gnu/libIlmThread.so gtk-3 gdk-3 atk-1.0 gio-2.0 pangocairo-1.0 gdk_pixbuf-2.0 cairo-gobject pango-1.0 cairo gobject-2.0 glib-2.0 gthread-2.0 gstbase-1.0 gstreamer-1.0 dc1394 avcodec avformat avutil swscale vtkCommon vtkFiltering vtkImaging vtkGraphics vtkGenericFiltering vtkIO vtkRendering vtkVolumeRendering vtkHybrid vtkWidgets vtkParallel vtkInfovis vtkGeovis vtkViews vtkCharts dl m pthread rt
--     3rdparty dependencies:       libwebp libprotobuf
--
--   OpenCV modules:
--     To be built:                 core flann imgproc ml photo reg surface_matching video viz dnn freetype fuzzy imgcodecs shape videoio highgui objdetect plot superres ts xobjdetect xphoto bgsegm bioinspired dpm face features2d line_descriptor saliency text calib3d ccalib datasets rgbd stereo tracking videostab xfeatures2d ximgproc aruco optflow phase_unwrapping stitching structured_light python2
--     Disabled:                    world contrib_world
--     Disabled by dependency:      -
--     Unavailable:                 cudaarithm cudabgsegm cudacodec cudafeatures2d cudafilters cudaimgproc cudalegacy cudaobjdetect cudaoptflow cudastereo cudawarping cudev java python3 cnn_3dobj cvv hdf matlab sfm
--
--   GUI:
--     QT:                          NO
--     GTK+ 3.x:                    YES (ver 3.10.8)
--     GThread :                    YES (ver 2.40.2)
--     GtkGlExt:                    NO
--     OpenGL support:              NO
--     VTK support:                 YES (ver 5.8.0)
--
--   Media I/O:
--     ZLib:                        /usr/lib/x86_64-linux-gnu/libz.so (ver 1.2.8)
--     JPEG:                        /usr/lib/x86_64-linux-gnu/libjpeg.so (ver )
--     WEBP:                        build (ver 0.3.1)
--     PNG:                         /usr/lib/x86_64-linux-gnu/libpng.so (ver 1.2.50)
--     TIFF:                        /usr/lib/x86_64-linux-gnu/libtiff.so (ver 42 - 4.0.3)
--     JPEG 2000:                   /usr/lib/x86_64-linux-gnu/libjasper.so (ver 1.900.1)
--     OpenEXR:                     /usr/lib/x86_64-linux-gnu/libImath.so /usr/lib/x86_64-linux-gnu/libIlmImf.so /usr/lib/x86_64-linux-gnu/libIex.so /usr/lib/x86_64-linux-gnu/libHalf.so /usr/lib/x86_64-linux-gnu/libIlmThread.so (ver 1.6.1)
--     GDAL:                        NO
--     GDCM:                        NO
--
--   Video I/O:
--     DC1394 1.x:                  NO
--     DC1394 2.x:                  YES (ver 2.2.1)
--     FFMPEG:                      YES
--       avcodec:                   YES (ver 54.35.1)
--       avformat:                  YES (ver 54.20.4)
--       avutil:                    YES (ver 52.3.0)
--       swscale:                   YES (ver 2.1.1)
--       avresample:                NO
--     GStreamer:                   NO
--     OpenNI:                      NO
--     OpenNI PrimeSensor Modules:  NO
--     OpenNI2:                     NO
--     PvAPI:                       NO
--     GigEVisionSDK:               NO
--     Aravis SDK:                  NO
--     UniCap:                      NO
--     UniCap ucil:                 NO
--     V4L/V4L2:                    NO/YES
--     XIMEA:                       NO
--     Xine:                        NO
--     gPhoto2:                     NO
--
--   Parallel framework:            pthreads
--
--   Other third-party libraries:
--     Use IPP:                     9.0.1 [9.0.1]
--          at:                     /home/map479-admin/opencv/build/3rdparty/ippicv/ippicv_lnx
--     Use IPP Async:               NO
--     Use VA:                      NO
--     Use Intel VA-API/OpenCL:     NO
--     Use Lapack:                  NO
--     Use Eigen:                   YES (ver 3.2.0)
--     Use Cuda:                    NO
--     Use OpenCL:                  YES
--     Use OpenVX:                  NO
--     Use custom HAL:              NO
--
--   OpenCL:                        <Dynamic loading of OpenCL library>
--     Include path:                /home/map479-admin/opencv/3rdparty/include/opencl/1.2
--     Use AMDFFT:                  NO
--     Use AMDBLAS:                 NO
--
--   Python 2:
--     Interpreter:                 /home/map479-admin/.virtualenvs/cv/bin/python2.7 (ver 2.7.13)
--     Libraries:                   /usr/local/lib/libpython2.7.a (ver 2.7.13)
--     numpy:                       /home/map479-admin/.virtualenvs/cv/lib/python2.7/site-packages/numpy/core/include (ver 1.12.1)
--     packages path:               lib/python2.7/site-packages
--
--   Python 3:
--     Interpreter:                 /usr/bin/python3.4 (ver 3.4.3)
--
--   Python (for build):            /home/map479-admin/.virtualenvs/cv/bin/python2.7
--
--   Java:
--     ant:                         NO
--     JNI:                         /usr/lib/jvm/default-java/include /usr/lib/jvm/default-java/include /usr/lib/jvm/default-java/include
--     Java wrappers:               NO
--     Java tests:                  NO
--
--   Matlab:                        Matlab not found or implicitly disabled
--
--   Documentation:
--     Doxygen:                     NO
--
--   Tests and samples:
--     Tests:                       YES
--     Performance tests:           YES
--     C/C++ Examples:              NO
--
--   Install path:                  /usr/local
--
--   cvconfig.h is in:              /home/map479-admin/opencv/build
-- -----------------------------------------------------------------
--
-- Configuring done
-- Generating done
-- Build files have been written to: /home/map479-admin/opencv/build


```




Now we can finally compile OpenCV:

```
make
```

Assuming that OpenCV compiled without error, you can now install it on your Ubuntu system:

```
sudo make install
sudo ldconfig
```



#### Step 11:


cd ~/.virtualenvs/cv/lib/python2.7/site-packages/
ln -s /usr/local/lib/python2.7/site-packages/cv2.so cv2.so


#### Step 12:

```
$ workon cv
$ python
>>> import cv2
>>> cv2.__version__
'3.2.0'
```
