# zju-rtl
## Background & Introduction
　The detection and pose estimation of reflective and texture-less objects, which are common in industry, are of significant importance but challenging.However, there is no available large public dataset of reflective and texture-less objects, which makes the relevant researches inconvenient. Thus, we proposed Zju-rtl, a new public dataset for reflective and texture-less metal parts, which can be used for object detection and pose estimation.

　The dataset contains a total of 38 texture-less and reflective metal parts. Different parts demonstrate the symmetry and similarity of shape and size. The dataset contains 38392 RGB images and the same number of masks, including 25080 training images and 13312 testing images. And there are 32 different scenes in testing images.

![所有训练目标](https://user-images.githubusercontent.com/60084969/140649189-f40a40d9-f116-4f2b-8994-9b79855ed645.png)

![所有测试场景](https://user-images.githubusercontent.com/60084969/140649193-2bdd725e-41ff-47e0-adda-8fe482d78ffa.png)

## Download
　You can download zju-rtl on windows and linux in many ways.

### Download in browser
　First of all, if the browser you are using is not Microsoft Edge, Google or FireFox, you can try to enter the following address on the browser

> ftp://userftp:1234@10.11.122.13:21

　If the following page is displayed on your browser(the username is "userftp" and password is "1234" if you are asked to provide them), you can click on the zju-rtl folder to download, if this method does not work, please try other methods.

![image](https://user-images.githubusercontent.com/60084969/140631663-623f69e7-339f-42f5-9897-c3670dcea610.png)

### Download in Windows(Win 10)
　Enter the following address in the address bar of the windows file explorer.

> ftp://userftp:1234@10.11.122.13:21

　If you can see the following page, it means success. The zju-rtl folder contains all the contents of the data set.

![image](https://user-images.githubusercontent.com/60084969/140631787-593cb14c-97af-4f7b-b1d6-b19f22e45bad.png)

### Download in Linux(Ubuntu 18.04)
#### Step 1: establish an FTP connection
　Open the terminal and enter the following command

> ftp 10.11.122.13
#### Step 2: Login with username and password
> name is userftp
> 
> password is 1234
#### Step 3: Directory operations
　You can use "ls", "cd" and other commands to display the directory list and change the directory

#### Step 4: Use FTP to download files
　Before downloading a file, we first need to use the "lcd" command to set the location of the local acceptance directory, like this

> lcd /opt/ftpDir

　If you do not specify a download directory, the file will be downloaded to the working directory when you log in to FTP.
Now, we can use the command get to download the file, and the file will be downloaded to the directory you set with "lcd".
> get zju-rtl/xxx.zip
## Usage

* CAD models.zip: there are three types of CAD models('.ply', '.stl', '.sldrt')
* Testing images(n#n).zip: Testing images with a resolution of n*n
* Training images(n#n).zip: Testing images with a resolution of n*n
* utils.zip: Some visualization tools, you can also download from this repository
