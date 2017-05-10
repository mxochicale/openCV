Installing [OpenCV 3.2.0](https://github.com/opencv/opencv/releases/tag/3.2.0) on Ubuntu 16.04 x64 with either Python 2.7 or Python 3.5 bindings.
----



#### Upgrating Python to 2.7 version on Ubuntu 16.04

[Source](https://tecadmin.net/install-python-2-7-on-centos-rhel/)


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



# Installation of OpenCV 3.2.0 



[Main Source](http://www.pyimagesearch.com/2016/10/24/ubuntu-16-04-how-to-install-opencv/)
[Source](http://withr.me/install-opencv-on-ubuntu-16/)


#### Step 1: Update and Upgrade
```
sudo apt-get update
sudo apt-get upgrade
```

#### Step 2:  Now we need to install our developer tools:
```
sudo apt-get install build-essential cmake pkg-config
```

#### Step 3: image I/O packages:
```
sudo apt-get install libjpeg8-dev libtiff5-dev libjasper-dev libpng12-dev
```


#### Step 4: processing video streams and accessing individual frames
```
sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
sudo apt-get install libxvidcore-dev libx264-dev
```


#### Step5 : GTK development library
```
sudo apt-get install libgtk-3-dev

```

#### Step 6: Optimize various routines inside of OpenCV
```
sudo apt-get install libatlas-base-dev gfortran
```


#### Step7 : installing the Python development headers and libraries
```
sudo apt-get install python2.7-dev python3.5-dev
```



# Step #2: Download the OpenCV source

```
cd && wget -O opencv.zip https://github.com/opencv/opencv/archive/3.2.0.zip && unzip opencv.zip && rm opencv.zip
cd && wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/3.2.0.zip && unzip opencv_contrib.zip && unzip opencv_contrib.zip && rm opencv_contrib.zip
```



# Step 3: Install & setup python virtual environment



#### Step 7: pip Python package manager
```
cd && wget https://bootstrap.pypa.io/get-pip.py
sudo python get-pip.py

```



#### Step 8: Install virtualenv and virtualenvwrapper.
```
sudo pip install virtualenv virtualenvwrapper
rm -rf ~/get-pip.py ~/.cache/pip
```


#### Step 10: Update ~/.bashrc file 


```
echo -e "\n# virtualenv and virtualenvwrapper" >> ~/.bashrc
echo "export WORKON_HOME=$HOME/.virtualenvs" >> ~/.bashrc
echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc
```

#### After editing our ~/.bashrc  file, we need to reload the changes:

```
source ~/.bashrc
```


#### Verifying that you are in the “cv” virtual environment

```
mkvirtualenv cv -p python
workon cv
```



you can leave the virtual environment by using: deactivate


# Step 3: Install numpy, configure, compile & install opencv



Ensure taht  you are in the cv virtual environment

```
workon cv
```

Install Numerical library NumPy 
```
pip install numpy

```


#### Step XX:  Configuring and compiling OpenCV on Ubuntu 16.04

```
cd ~/opencv-3.2.0/ && mkdir build && cd build
```

```
cmake -D CMAKE_BUILD_TYPE=RELEASE \
	-D CMAKE_INSTALL_PREFIX=/usr/local \
	-D INSTALL_C_EXAMPLES=OFF \
	-D INSTALL_PYTHON_EXAMPLES=ON \
	-D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib-3.2.0/modules \
	-D PYTHON_EXECUTABLE=~/.virtualenvs/cv/bin/python \
	-D WITH_JPEG=OFF \
	-D BUILD_EXAMPLES=OFF ..
```


"-D WITH_JPEG=OFF" is used  to get rid of "Corrupt JPEG data: 1 extraneous bytes before marker 0xd6" in OpenFace
[Source1](http://privateblog.info/linux/opencv-i-corrupt-jpeg-data-na-linux/)
[Source2](http://stackoverflow.com/questions/15533338/opencv-error-on-ubuntu-webcam-logitech-c270-capture-highgui-error-v4l-v4l2)




...terminal output   

```

-- General configuration for OpenCV 3.2.0 =====================================
--   Version control:               unknown
-- 
--   Extra modules:
--     Location (extra):            /home/map479/opencv_contrib-3.2.0/modules
--     Version control (extra):     unknown
-- 
--   Platform:
--     Timestamp:                   2017-05-10T20:29:27Z
--     Host:                        Linux 4.4.0-75-generic x86_64
--     CMake:                       3.5.1
--     CMake generator:             Unix Makefiles
--     CMake build tool:            /usr/bin/make
--     Configuration:               RELEASE
-- 
--   C/C++:
--     Built as dynamic libs?:      YES
--     C++ Compiler:                /usr/bin/c++  (ver 5.4.0)
--     C++ flags (Release):         -fsigned-char -W -Wall -Werror=return-type -Werror=non-virtual-dtor -Werror=address -Werror=sequence-point -Wformat -Werror=format-security -Wmissing-declarations -Wundef -Winit-self -Wpointer-arith -Wshadow -Wsign-promo -Wno-narrowing -Wno-delete-non-virtual-dtor -Wno-comment -fdiagnostics-show-option -Wno-long-long -pthread -fomit-frame-pointer -msse -msse2 -mno-avx -msse3 -mno-ssse3 -mno-sse4.1 -mno-sse4.2 -ffunction-sections -fvisibility=hidden -fvisibility-inlines-hidden -O3 -DNDEBUG  -DNDEBUG
--     C++ flags (Debug):           -fsigned-char -W -Wall -Werror=return-type -Werror=non-virtual-dtor -Werror=address -Werror=sequence-point -Wformat -Werror=format-security -Wmissing-declarations -Wundef -Winit-self -Wpointer-arith -Wshadow -Wsign-promo -Wno-narrowing -Wno-delete-non-virtual-dtor -Wno-comment -fdiagnostics-show-option -Wno-long-long -pthread -fomit-frame-pointer -msse -msse2 -mno-avx -msse3 -mno-ssse3 -mno-sse4.1 -mno-sse4.2 -ffunction-sections -fvisibility=hidden -fvisibility-inlines-hidden -g  -O0 -DDEBUG -D_DEBUG
--     C Compiler:                  /usr/bin/cc
--     C flags (Release):           -fsigned-char -W -Wall -Werror=return-type -Werror=non-virtual-dtor -Werror=address -Werror=sequence-point -Wformat -Werror=format-security -Wmissing-declarations -Wmissing-prototypes -Wstrict-prototypes -Wundef -Winit-self -Wpointer-arith -Wshadow -Wno-narrowing -Wno-comment -fdiagnostics-show-option -Wno-long-long -pthread -fomit-frame-pointer -msse -msse2 -mno-avx -msse3 -mno-ssse3 -mno-sse4.1 -mno-sse4.2 -ffunction-sections -fvisibility=hidden -O3 -DNDEBUG  -DNDEBUG
--     C flags (Debug):             -fsigned-char -W -Wall -Werror=return-type -Werror=non-virtual-dtor -Werror=address -Werror=sequence-point -Wformat -Werror=format-security -Wmissing-declarations -Wmissing-prototypes -Wstrict-prototypes -Wundef -Winit-self -Wpointer-arith -Wshadow -Wno-narrowing -Wno-comment -fdiagnostics-show-option -Wno-long-long -pthread -fomit-frame-pointer -msse -msse2 -mno-avx -msse3 -mno-ssse3 -mno-sse4.1 -mno-sse4.2 -ffunction-sections -fvisibility=hidden -g  -O0 -DDEBUG -D_DEBUG
--     Linker flags (Release):
--     Linker flags (Debug):
--     ccache:                      NO
--     Precompiled headers:         YES
--     Extra dependencies:          /usr/lib/x86_64-linux-gnu/libpng.so /usr/lib/x86_64-linux-gnu/libz.so /usr/lib/x86_64-linux-gnu/libtiff.so /usr/lib/x86_64-linux-gnu/libjasper.so /usr/lib/x86_64-linux-gnu/libjpeg.so gtk-3 gdk-3 pangocairo-1.0 pango-1.0 atk-1.0 cairo-gobject cairo gdk_pixbuf-2.0 gio-2.0 gobject-2.0 glib-2.0 gthread-2.0 avcodec-ffmpeg avformat-ffmpeg avutil-ffmpeg swscale-ffmpeg dl m pthread rt
--     3rdparty dependencies:       libwebp IlmImf libprotobuf
-- 
--   OpenCV modules:
--     To be built:                 core flann imgproc ml photo reg surface_matching video dnn freetype fuzzy imgcodecs shape videoio highgui objdetect plot superres ts xobjdetect xphoto bgsegm bioinspired dpm face features2d line_descriptor saliency text calib3d ccalib datasets rgbd stereo tracking videostab xfeatures2d ximgproc aruco optflow phase_unwrapping stitching structured_light python2
--     Disabled:                    world contrib_world
--     Disabled by dependency:      -
--     Unavailable:                 cudaarithm cudabgsegm cudacodec cudafeatures2d cudafilters cudaimgproc cudalegacy cudaobjdetect cudaoptflow cudastereo cudawarping cudev java python3 viz cnn_3dobj cvv hdf matlab sfm
-- 
--   GUI: 
--     QT:                          NO
--     GTK+ 3.x:                    YES (ver 3.18.9)
--     GThread :                    YES (ver 2.48.2)
--     GtkGlExt:                    NO
--     OpenGL support:              NO
--     VTK support:                 NO
-- 
--   Media I/O: 
--     ZLib:                        /usr/lib/x86_64-linux-gnu/libz.so (ver 1.2.8)
--     JPEG:                        NO
--     WEBP:                        build (ver 0.3.1)
--     PNG:                         /usr/lib/x86_64-linux-gnu/libpng.so (ver 1.2.54)
--     TIFF:                        /usr/lib/x86_64-linux-gnu/libtiff.so (ver 42 - 4.0.6)
--     JPEG 2000:                   /usr/lib/x86_64-linux-gnu/libjasper.so (ver 1.900.1)
--     OpenEXR:                     build (ver 1.7.1)
--     GDAL:                        NO
--     GDCM:                        NO
-- 
--   Video I/O:
--     DC1394 1.x:                  NO
--     DC1394 2.x:                  NO
--     FFMPEG:                      YES
--       avcodec:                   YES (ver 56.60.100)
--       avformat:                  YES (ver 56.40.101)
--       avutil:                    YES (ver 54.31.100)
--       swscale:                   YES (ver 3.1.101)
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
--          at:                     /home/map479/opencv-3.2.0/build/3rdparty/ippicv/ippicv_lnx
--     Use IPP Async:               NO
--     Use VA:                      NO
--     Use Intel VA-API/OpenCL:     NO
--     Use Lapack:                  NO
--     Use Eigen:                   NO
--     Use Cuda:                    NO
--     Use OpenCL:                  YES
--     Use OpenVX:                  NO
--     Use custom HAL:              NO
-- 
--   OpenCL:                        <Dynamic loading of OpenCL library>
--     Include path:                /home/map479/opencv-3.2.0/3rdparty/include/opencl/1.2
--     Use AMDFFT:                  NO
--     Use AMDBLAS:                 NO
-- 
--   Python 2:
--     Interpreter:                 /home/map479/.virtualenvs/cv/bin/python (ver 2.7.13)
--     Libraries:                   /usr/local/lib/libpython2.7.a (ver 2.7.13)
--     numpy:                       /home/map479/.virtualenvs/cv/lib/python2.7/site-packages/numpy/core/include (ver 1.12.1)
--     packages path:               lib/python2.7/site-packages
-- 
--   Python 3:
--     Interpreter:                 /usr/bin/python3 (ver 3.5.2)
-- 
--   Python (for build):            /home/map479/.virtualenvs/cv/bin/python
-- 
--   Java:
--     ant:                         NO
--     JNI:                         NO
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
--   cvconfig.h is in:              /home/map479/opencv-3.2.0/build
-- -----------------------------------------------------------------
-- 
-- Configuring done
-- Generating done
-- Build files have been written to: /home/map479/opencv-3.2.0/build



```




Now we can finally compile OpenCV:

```
make -j4
```

Assuming that OpenCV compiled without error, you can now install it on your Ubuntu system:

```
sudo make install
sudo ldconfig
```


your Python 2.7 bindings for OpenCV 3 should now be located in 
/usr/local/lib/python-2.7/site-packages/.
You can verify this using the ls  command:


```
ls -l /usr/local/lib/python2.7/site-packages/
```


The final step is to sym-link our OpenCV cv2.so  
bindings into our cv  virtual environment for Python 2.7:

```
cd ~/.virtualenvs/cv/lib/python2.7/site-packages/
ln -s /usr/local/lib/python2.7/site-packages/cv2.so cv2.so
```

#### Step 12:

```
$ workon cv
$ python
>>> import cv2
>>> cv2.__version__
'3.2.0'
```

:) on Wed 10 May 21:44:50 BST 2017 Bham,UK


