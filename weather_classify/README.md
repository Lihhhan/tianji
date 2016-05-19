# weather_classify
天气分类
需要安装opencv-python库,numpy库

python2.7.6 运行正常
cmd: python app.py XXX.avi
检测结果会在视频左上角打出水印

*video.py*视频处理类（帧提取，平滑，提取前后帧diff获取特征）
*feature.py* 图片处理类（计算灰度共生矩阵以及相关特征）




