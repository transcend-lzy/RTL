# zju-rtm
## Background
  The detection and pose estimation of reflective and texture-less objects, which are common in industry, are of significant importance but challenging.
It has attracted more and more attention in academia and industry. However, there is no available large public dataset of reflective and texture-less objects, which makes the relevant researches inconvenient. Thus, we proposed Zju-rtl, a new public dataset for reflective and texture-less metal parts, which can be used for object detection and pose estimation. In the prior art, many approaches use a combination of depth images and RGB images to estimate pose, and many RGB-D public datasets were issued. However, for reflective objects, it is difficult to acquire accurate depth information. It is more applicable to use only RGB information to estimate poses, so Zju-rtl is a RGB dataset. The dataset contains a total of 38 texture-less and reflective metal parts. Different parts demonstrate the symmetry and similarity of shape and size. The dataset contains 38392 RGB images and the same number of masks, including 25080 training images and 13312 testing images. And there are 32 different scenes in testing images. At the same time, we provided accurate ground truth poses and bounding-box annotations for each image. 

## Download
你可以通过多种方法在windows系统和linux系统上下载zju-rtm这一数据集
首先如果你使用的浏览器不是Microsoft Edge或者google或者FireFox，你可以尝试在浏览器上输入以下网址
> ftp://userftp:1234@10.11.122.13:21
如果在你的浏览器上显示以下界面，你可以点击zju-rtm文件夹下载文件

### Download in Windows(Win 10)
>* 方式一

>* 方式二



### Download in Linux(Ubuntu 18.04)
  
  >* 方式一

## Usage
>* CAD models: there are three types of CAD models('.ply', '.stl', '.sldrt')

>* Testing images(n#n): Testing images with a resolution of n*n

>* Training images(n#n): Testing images with a resolution of n*n
