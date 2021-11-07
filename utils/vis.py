import pygame
from pygame.locals import *
import cv2
import scipy.misc
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
import os
from ruamel import yaml
from read_stl import stl_model
import random

def creatC2m(rM2c,tM2c): #输入为r 3*3   t为 1*3
    R = rM2c
    T = np.dot(-rM2c.T,tM2c.reshape(3,1)).reshape(1,3)
    return R,T

def T2vec(R):  #矩阵分解为旋转矩阵和平移向量
    r=R[:3,:3]
    t=R[:3,3]
    return r,t

def vec2T(r,t):  #将旋转和平移向量转换为rt矩阵  r和t都是3*1
    t= t.reshape(3,1)
    R=cv2.Rodrigues(r)
    rtMatrix=np.c_[np.r_[R[0],np.array([[0,0,0]])],np.r_[t,np.array([[1]])]]
    return rtMatrix

def cube(tri):  #提取一堆点
	glBegin(GL_TRIANGLES) #绘制多个三角形
	for Tri in tri: 
		glColor3fv(Tri['colors'])
		glVertex3fv(
			(Tri['p0'][0], Tri['p0'][1], Tri['p0'][2]))
		glVertex3fv(
			(Tri['p1'][0], Tri['p1'][1], Tri['p1'][2]))
		glVertex3fv(
			(Tri['p2'][0], Tri['p2'][1], Tri['p2'][2]))

	glEnd()  #实际上以三角面片的形式保存

def draw_cube_test( worldOrientation, worldLocation,tri,window,display):
	glPushMatrix()
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

	pos = worldLocation[0]

	rm = worldOrientation.T

	rm[:,0] = -rm[:,0]
	rm[:,1] = -rm[:,1]

	xx = np.array([rm[0,0], rm[1,0], rm[2,0]])
	yy = np.array([rm[0,1], rm[1,1], rm[2,1]])
	zz = np.array([rm[0,2], rm[1,2], rm[2,2]])
	obj = pos + zz

	gluLookAt(pos[0],pos[1],pos[2],obj[0],obj[1],obj[2],yy[0],yy[1],yy[2])  
	cube(tri)
	glPopMatrix()
	pygame.display.flip()

	# Read the result
	string_image = pygame.image.tostring(window, 'RGB')
	temp_surf = pygame.image.fromstring(string_image, display, 'RGB')
	tmp_arr = pygame.surfarray.array3d(temp_surf)
	return (tmp_arr)  #得到最后的图



def readYaml(yaml_file):
    gt_dic = {}
    f = open(yaml_file , 'r', encoding='utf-8')
    cfg = f.read()
    d= yaml.safe_load(cfg)
    return d

def init(width, height, intrinsic):
    pygame.init()
    display = (width,height)  
    window = pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    scale = 0.0001
    fx = intrinsic[0][2] #相机标定矩阵的值
    fy = intrinsic[1][2]
    cx = intrinsic[0][0]
    cy = intrinsic[1][1]
    glFrustum(-fx*scale,(width-fx)*scale,-(height-fy)*scale,fy*scale,(cx+cy)/2*scale,20)#透视投影
    glClearDepth(1.0)  
    glDepthFunc(GL_LESS)  #设置深度测试函数
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_POINT_SMOOTH)
    glPolygonMode(GL_FRONT, GL_FILL)
    glPolygonMode(GL_BACK, GL_FILL)
    return display,window

def creatImg(info, stlPath, window, display, height,width) :
    W_Rm2c = info['m2c_R']
    W_Lm2c = info['m2c_T']
    W_Rm2c = cv2.Rodrigues(np.matrix(W_Rm2c))[0]
    W_Lm2c = np.array([[W_Lm2c[0][0],W_Lm2c[0][1],W_Lm2c[0][2]]]).reshape(3,1)
    rt = vec2T(W_Rm2c,W_Lm2c)
    W_Rm2c,W_Lm2c = T2vec(rt)
    W_Rc2m,W_Lc2m = creatC2m(W_Rm2c,W_Lm2c)
    tri = stl_model(os.path.join(stlPath, str(info['obj_id'])+'.stl')).tri
    im = draw_cube_test(W_Rc2m,W_Lc2m,tri,window,display)
    im2=np.zeros((height,width,3))
    for m in range(height):
        for n in range(width):
            im2[m,n] = im[n,m]#彩色的边缘面
    return im2

def creatBottom(width, height):   #生成要求大小的bottom图片
    img = np.zeros((height,width),dtype=np.uint8)
    bottom = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
    for i in range(3):
        bottom[:,:,i] = 0
    return bottom

def creatDir(path):
    if not os.path.exists(path): os.mkdir(path)

def show_photo(photo):   #展示照片
    if (photo.shape[0] > 1000):
        photo = cv2.resize(photo,(int(2448.0//2),int(2048.0//2)))  
    cv2.imshow("abc",photo)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


'''
path是要可视化的那个图片集的路径 eg: '/home/cy/zju-rtl/Testing images(2448#2048)/scene7' 建议使用绝对路径
isTrain 如果要可视化的是训练图片,则为true,测试图片为false,默认为true
hasBbox 如果为true,则会一同渲染bbox框在上面的图片
imgList 需要可视化的图片的列表
visPath 是可视化图片放置的文件夹的地址
stlPath stl文件所在路径 eg:'/home/cy/zju-rtl/CADmodels/stl'


代码运行后可视化结果的图片会保存在visPath下,不同类型文件由5个文件夹分别保存:
1. 文件夹'Gt':gt渲染结果图片
2. 文件夹'BboxAndGt': gt渲染结果和bbox框同在的图片
3. 文件夹'OffsetAndGt': 与2相比bbox框变为随机偏移和扩大的框(train不包含这个文件夹)
'''
def visImg(path, stlPath, imgIndex, visPath,isTrain = True, hasBbox = True ):
    imgPath = os.path.join(path,'rgb')
    gt = readYaml(os.path.join(path,'gt.yml'))
    bbox = readYaml(os.path.join(path,'bboxNew.yml'))
    intrinsic = readYaml(os.path.join(path,'Intrinsic.yml'))['Intrinsic']

    dstGt = os.path.join(visPath,'Gt')
    creatDir(dstGt)
    if hasBbox:
        dstBbox = os.path.join(visPath,'BboxAndGt')
        creatDir(dstBbox)
        if not isTrain: 
            dstOffset = os.path.join(visPath,'OffsetAndGt')
            creatDir(dstOffset)

    if os.path.exists(os.path.join(imgPath,str(imgIndex)+'.png')) :
        fileEnd = '.png'
        width, height = 512,512
    else : 
        width,height = 2448,2048
        fileEnd = '.jpg'

    if not isTrain : 
        bboxOff = readYaml(os.path.join(path,'bboxOffset.yml'))
        bottom = creatBottom(width, height)
    display,window = init(width, height, intrinsic)
    imgFilePath = os.path.join(imgPath,str(imgIndex)+fileEnd)
    if isTrain:
        img = cv2.imread(imgFilePath)
        info = gt[str(imgIndex)][0]
        im2 = creatImg(info,stlPath,window, display,height,width)
        imgVis = cv2.addWeighted(img.astype(np.uint8), 0.5, im2.astype(np.uint8), 1, 0)
        cv2.imwrite(os.path.join(dstGt,str(imgIndex)+'.png'),imgVis)
        if hasBbox:
            xywh = bbox[str(imgIndex)][0]['xywh']
            cv2.rectangle(img, (xywh[0], xywh[1]), (xywh[0] + xywh[2], xywh[1] + xywh[3]), (0, 0, 255), 2)
            imgVis = cv2.addWeighted(img.astype(np.uint8), 0.5, im2.astype(np.uint8), 1, 0)
            cv2.imwrite(os.path.join(dstBbox,str(imgIndex)+'.png'),imgVis)
    else:
        img = cv2.imread(imgFilePath)
        imgOffset = cv2.imread(imgFilePath)
        imgBbox = cv2.imread(imgFilePath)
        for index,info in enumerate(gt[str(imgIndex)]):
            im2 = creatImg(info,stlPath,window, display, height,width)
            bottom=cv2.addWeighted(bottom.astype(np.uint8), 1, im2.astype(np.uint8), 1, 0)
            if hasBbox:
                xywh = bbox[str(imgIndex)][index]['xywh']
                xywhOff = bboxOff[str(imgIndex)][index]['xywh']
                cv2.rectangle(imgBbox, (xywh[0], xywh[1]), (xywh[0] + xywh[2], xywh[1] + xywh[3]), (0, 0, 255), 2)
                cv2.rectangle(imgOffset, (xywhOff[0], xywhOff[1]), (xywhOff[0] + xywhOff[2], xywhOff[1] + xywhOff[3]), (0, 0, 255), 2)
        imgVis = cv2.addWeighted(img, 0.5, bottom, 1, 0)
        cv2.imwrite(os.path.join(dstGt,str(imgIndex)+'.png'),imgVis)
        if hasBbox:
            imgVis = cv2.addWeighted(imgBbox, 0.5, bottom, 1, 0)
            cv2.imwrite(os.path.join(dstBbox, str(imgIndex)+'.png'), imgVis)
            imgVis = cv2.addWeighted(imgOffset, 0.5, bottom, 1, 0)
            cv2.imwrite(os.path.join(dstOffset, str(imgIndex)+'.png'), imgVis)
    pygame.quit()
        

#某几张图片
def visImges(path, stlPath, imgList, isTrain = True, hasBbox = True, visPath = None):
    if visPath == None: visPath = os.path.join(path,'vis')
    print(os.path.exists(visPath))
    if not os.path.exists(visPath): os.mkdir(visPath)  #如果没有vis文件夹就取消
    for i in imgList:
        visImg(path, stlPath, i , visPath, isTrain)



#可视化path对应地址的所有图片
def visAll(path, stlPath, isTrain = True, hasBbox = True, visPath = None):
    if visPath == None: visPath = os.path.join(path,'vis')
    if not os.path.exists(visPath): os.mkdir(visPath)  #如果没有vis文件夹就取消


#随机挑选nums张图片做可视化
def visRandom(path, stlPath, nums, isTrain = True, hasBbox = True, visPath = None):
    if visPath == None: visPath = os.path.join(path,'vis')
    if not os.path.exists(visPath): os.mkdir(visPath)  #如果没有vis文件夹就取消
    list_I = []
    if isTrain: fileNum = 660
    else: fileNum = 416
    for j in range(nums):
        num = random.randint(1,fileNum)
        while num in list_I:
            num = random.randint(1,fileNum)
        list_I.append(num)   #生成随机图像代号列表

    for i in list_I:
        visImg(path, stlPath, i , visPath, isTrain)
stlPath = '/home/wzz/Desktop/chaoyue/zju-rtm/CADmodels/stl'
path = '/home/wzz/Desktop/chaoyue/zju-rtm/Training images(2448#2048)/obj5'

# visRandom(path, stlPath, 10)
visImges(path,stlPath,[659])
