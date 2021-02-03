import cv2
import numpy as np

# 高斯滤波
def GausBlur(src):
    dst = cv2.GaussianBlur(src, (5, 5), 1.5)
    cv2.namedWindow('GausBlur',0)
    cv2.imshow('GausBlur', dst)
#    cv2.waitKey(0)
    return dst

# 灰度处理
def Gray_img(src):
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    cv2.namedWindow('gray', 0)
    cv2.imshow('gray', gray)
 #   cv2.waitKey(0)
    return gray


# 二值化
def threshold_img(src):
    ret, binary = cv2.threshold(src, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_TRIANGLE)
    print("threshold value %s" % ret)
    cv2.namedWindow('threshold', 0)
    cv2.imshow('threshold', binary)
#    cv2.waitKey(0)
    return binary


# 开运算操作
def open_mor(src):
    kernel = np.ones((5, 5), np.uint8)
    opening = cv2.morphologyEx(src, cv2.MORPH_OPEN, kernel, iterations=3)  # iterations进行3次操作
    cv2.namedWindow('open', 0)
    cv2.imshow('open', opening)
    return opening


# 轮廓拟合
def draw_shape(open_img, gray_img):
    contours, hierarchy = cv2.findContours(open_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnt = contours[0]  # 得到第一个的轮廓

    rect = cv2.minAreaRect(cnt)
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    cv2.drawContours(src, [box], 0, (0, 0, 255), 3)  # 画矩形框

    # 图像轮廓及中心点坐标
    M = cv2.moments(cnt)  # 计算第一条轮廓的各阶矩,字典形式
    center_x = int(M['m10'] / M['m00'])
    center_y = int(M['m01'] / M['m00'])
    print('center_x:', center_x)
    print('center_y:', center_y)
    cv2.circle(src, (center_x, center_y), 7, 128, -1)  # 绘制中心点
    str1 = '(' + str(center_x) + ',' + str(center_y) + ')'  # 把坐标转化为字符串
    cv2.putText(src, str1, (center_x - 50, center_y + 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2,
                cv2.LINE_AA)  # 绘制坐标点位

    cv2.namedWindow('show', 0)
    cv2.imshow('show', src)
 #   cv2.waitKey(0)

src = cv2.imread('F:/graduate/EXP_data/EXP_data/test2-removed.png')
gaus_img = GausBlur(src)
gray_img = Gray_img(gaus_img)
thres_img = threshold_img(gray_img)
open_img = open_mor(thres_img)
draw_shape(open_img, src)

cv2.waitKey(0)