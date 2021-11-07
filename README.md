# zju-rtl
## Background
  The detection and pose estimation of reflective and texture-less objects, which are common in industry, are of significant importance but challenging.
It has attracted more and more attention in academia and industry. However, there is no available large public dataset of reflective and texture-less objects, which makes the relevant researches inconvenient. Thus, we proposed Zju-rtl, a new public dataset for reflective and texture-less metal parts, which can be used for object detection and pose estimation. In the prior art, many approaches use a combination of depth images and RGB images to estimate pose, and many RGB-D public datasets were issued. However, for reflective objects, it is difficult to acquire accurate depth information. It is more applicable to use only RGB information to estimate poses, so Zju-rtl is a RGB dataset. The dataset contains a total of 38 texture-less and reflective metal parts. Different parts demonstrate the symmetry and similarity of shape and size. The dataset contains 38392 RGB images and the same number of masks, including 25080 training images and 13312 testing images. And there are 32 different scenes in testing images. At the same time, we provided accurate ground truth poses and bounding-box annotations for each image. 

## Download
你可以通过多种方法在windows系统和linux系统上下载zju-rtl这一数据集
首先如果你使用的浏览器不是Microsoft Edge或者google或者FireFox，你可以尝试在浏览器上输入以下地址
> ftp://userftp:1234@10.11.122.13:21
如果在你的浏览器上显示以下界面，恭喜你，你可以点击zju-rtl文件夹下载文件,如果该方法不奏效，请尝试下面的方法
![image](https://user-images.githubusercontent.com/60084969/140631663-623f69e7-339f-42f5-9897-c3670dcea610.png)
> ps：如果页面要求输入用户名和密码，用户名为userftp，密码为1234

### Download in Windows(Win 10)
在windows文件资源管理器地址栏输入以下地址
> ftp://userftp:1234@10.11.122.13:21
> 如果你能看到如下界面则代表成功，zju-rtl文件夹包含了该数据集的所有内容
![image](https://user-images.githubusercontent.com/60084969/140631787-593cb14c-97af-4f7b-b1d6-b19f22e45bad.png)

### Download in Linux(Ubuntu 18.04)
#### 步骤 1: 建立 FTP 连接
打开终端输入以下命令
> ftp 10.11.122.13
#### 步骤 2: 使用用户名密码登录
name is userftp
password is 1234
#### 步骤 3: 目录操作
你可以使用ls,cd等命令来显示目录列表和改变目录

#### 步骤 4: 使用 FTP 下载文件
在下载一个文件之前，我们首先需要使用lcd命令设定本地接受目录位置，像这样
> lcd /opt/ftpDir
如果你不指定下载目录，文件将会下载到你登录 FTP 时候的工作目录。
现在，我们可以使用命令 get 来下载文件,文件将会下载到你使用lcd设置的目录下

## Usage
>* CAD models: there are three types of CAD models('.ply', '.stl', '.sldrt')

>* Testing images(n#n): Testing images with a resolution of n*n

>* Training images(n#n): Testing images with a resolution of n*n
>* utils: 一些可视化工具 
