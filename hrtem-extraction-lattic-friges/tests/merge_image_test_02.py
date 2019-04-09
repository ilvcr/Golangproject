"""

输入：图片路径(path+filename)，裁剪所的图片的列的数量、行的数量
输出：无
"""
def merge_picture(merge_path,num_of_cols,num_of_rows):
    filename=file_name(merge_path,".tif")
    shape=cv2.imread(filename[0],-1).shape    #三通道的影像需把-1改成1
    cols=shape[1]
    rows=shape[0]
    channels=shape[2]
    dst=np.zeros((rows*num_of_rows,cols*num_of_cols,channels),np.uint8)
    for i in range(len(filename)):
        img=cv2.imread(filename[i],-1)
        cols_th=int(filename[i].split("_")[-1].split('.')[0])
        rows_th=int(filename[i].split("_")[-2])
        roi=img[0:rows,0:cols,:]
        dst[rows_th*rows:(rows_th+1)*rows,cols_th*cols:(cols_th+1)*cols,:]=roi
    cv2.imwrite(merge_path+"merge.tif",dst)


#调用切割
path='.\\input\\origin\\test\\'   #要裁剪的图片所在的文件夹
filename='2015_rgbn.tif'    #要裁剪的图片名
cols=1024        #小图片的宽度（列数）
rows=1024        #小图片的高度（行数）
crop_one_picture(path,filename,1024,1024)

#调用合并
merge_path=".\\input\\origin\\test\\crop1024_1024\\"   #要合并的小图片所在的文件夹
num_of_cols=13    #列数
num_of_rows=9     #行数
merge_picture(merge_path,num_of_cols,num_of_rows)
