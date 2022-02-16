# --- function.py ---

# fps取得
from moviepy.editor import *
def get_fps(file_path):
    clip = VideoFileClip(file_path)
    return clip.fps

# duration取得
def get_duration(file_path):
    clip = VideoFileClip(file_path)
    return int(clip.duration) 

# リセットフォルダ
import os
import shutil
def reset_folder(path):
    if os.path.isdir(path):
      shutil.rmtree(path)
    os.makedirs(path,exist_ok=True)

# フレームピックアップ
import cv2
import os
def save_frame(video_name):  
    # setting
    video_folder = 'video'
    pic_folder ='pic'
    frame_num = 10
    # content
    video_path = video_folder + '/' + video_name
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        return
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_num)
    ret, frame = cap.read()
    result_path = pic_folder + '/' + os.path.splitext(video_name)[0]+'.jpg'
    if ret:
        cv2.imwrite(result_path, frame)

# 画像表示（nameでファイル名指示）
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import os
def display_pic(folder, name):
    fig = plt.figure(figsize=(20, 45))
    files = sorted(os.listdir(folder))
    for i, file in enumerate(files):
        if file=='.ipynb_checkpoints':
           continue
        if file=='.DS_Store':
           continue
        img = Image.open(folder+'/'+file)    
        images = np.asarray(img)
        ax = fig.add_subplot(10, 3, i+1, xticks=[], yticks=[])
        image_plt = np.array(images)
        ax.imshow(image_plt)
        ax.set_xlabel(name[i], fontsize=30)
    fig.tight_layout()               
    plt.show()
    plt.close()

# 動画再生
from IPython.display import display, HTML
from IPython.display import HTML
def display_mp4(path):
    #print('prepere to play movie...')
    from base64 import b64encode
    mp4 = open(path,'rb').read()
    data_url = "data:video/mp4;base64," + b64encode(mp4).decode()
    display(HTML("""
    <video width=700 controls >
        <source src="%s" type="video/mp4">
    </video>
    """ % data_url))

# フォルダ作成
os.makedirs('download', exist_ok=True)