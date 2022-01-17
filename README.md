# RTL
## Background & Introduction
　The detection and pose estimation of reflective and texture-less objects, which are common in industry, are of significant importance but challenging.However, there is no available large public dataset of reflective and texture-less objects, which makes the relevant researches inconvenient. Thus, we proposed Zju-rtl, a new public dataset for reflective and texture-less metal parts, which can be used for object detection and pose estimation.

　The dataset contains a total of 38 texture-less and reflective metal parts. Different parts demonstrate the symmetry and similarity of shape and size. The dataset contains 38392 RGB images and the same number of masks, including 25080 training images and 13312 testing images. And there are 32 different scenes in testing images.

![所有训练目标](https://user-images.githubusercontent.com/60084969/140649189-f40a40d9-f116-4f2b-8994-9b79855ed645.png)

![所有测试场景](https://user-images.githubusercontent.com/60084969/140649193-2bdd725e-41ff-47e0-adda-8fe482d78ffa.png)

## Download
　You can download RTL on this website[click here to download](http://www.zju-rtl.cn:8080/RTL/).

## Usage

* CAD models.zip: there are three types of CAD models('.ply', '.stl', '.sldrt')
* Testing images(n#n).zip: Testing images with a resolution of n*n
* Training images(n#n).zip: Testing images with a resolution of n*n
* utils.zip: Some visualization tools, you can also download from this repository
