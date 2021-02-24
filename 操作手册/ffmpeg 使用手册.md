# ffmpeg 操作手册

## 下载 ffmpeg

百度网盘：[**点击下载**](https://pan.baidu.com/s/1TPE8JvDdfRxOaswIZJUKJg)

提取码：**8cjl**

### ffmpeg 简单用法

```
ffmpeg -i out.ogv -vcodec h264 out.mp4
ffmpeg -i out.ogv -vcodec mpeg4 out.mp4
ffmpeg -i out.ogv -vcodec libxvid out.mp4
ffmpeg -i out.mp4 -vcodec wmv1 out.wmv
ffmpeg -i out.mp4 -vcodec wmv2 out.wmv
```
-i 后面是输入文件名。

-vcodec 后面是编码格式，h264 最佳，但 Windows 系统默认不安装。

如果是要插入 ppt 的视频，选择 wmv1 或 wmv2 基本上万无一失。

附加选项：-r 指定帧率，-s 指定分辨率，-b 指定比特率；于此同时可以对声道进行转码，-acodec 指定音频编码，-ab 指定音频比特率，-ac 指定声道数，例如

```
ffmpeg -i out.ogv -s 640x480 -b 500k -vcodec h264 -r 29.97 -acodec libfaac -ab 48k -ac 2 out.mp4
```
### 批量转换
```
for %i in (*.flv) do ffmpeg -i %i -c copy "newfiles\%~nv.mp4"
for %i in (*.mov) do ffmpeg -i %i -c copy "newfiles\%~nv.mp4"

//批量转换视频格式
ffmpeg -i xxx.avi -vcodec copy -f mp4 xxx.mp4

//批量转换视频格式 --设定分辨率 --设置新文件位置
for /R %v IN (*.mp4) do ( ffmpeg -i %v -vcodec h264 -vf scale=720:-2 -threads 4  "newfiles\%~nv.mp4")
```


### 剪切
用 -ss 和 -t 选项， 从第 30 秒开始，向后截取 10 秒的视频，并保存：
```
ffmpeg -i input.wmv -ss 00:00:30.0 -c copy -t 00:00:10.0 output.wmv
ffmpeg -i input.wmv -ss 30 -c copy -t 10 output.wmv
```
达成相同效果，也可以用 -ss 和 -to 选项， 从第 30 秒截取到第 40 秒：
```
ffmpeg -i input.wmv -ss 30 -c copy -to 40 output.wmv
```
值得注意的是，ffmpeg 为了加速，会使用关键帧技术， 所以有时剪切出来的结果在起止时间上未必准确。 

通常来说，把 -ss 选项放在 -i 之前，会使用关键帧技术； 把 -ss 选项放在 -i 之后，则不使用关键帧技术。 

如果要使用关键帧技术又要保留时间戳，可以加上 -copyts 选项：

```
ffmpeg -ss 00:01:00 -i video.mp4 -to 00:02:00 -c copy -copyts cut.mp4
```
截取视频段：输入"input.mp4"从3分钟开始截取视频段60s并保存输出为"output.mp4"
```
ffmpeg -ss 00:03:00 -i input.mp4 -t 60 -c:v copy -c:a copy output.mp4
```
### 合并
把两个视频文件合并成一个。
简单地使用 concat demuxer，示例：
```
$ cat mylist.txt
file '/path/to/file1'
file '/path/to/file2'
file '/path/to/file3'
 
$ ffmpeg -f concat -i mylist.txt -c copy output
```
更多时候，由于输入文件的多样性，需要转成中间格式再合成：


```
ffmpeg -i input1.avi -qscale:v 1 intermediate1.mpg
ffmpeg -i input2.avi -qscale:v 1 intermediate2.mpg
cat intermediate1.mpg intermediate2.mpg > intermediate_all.mpg
ffmpeg -i intermediate_all.mpg -qscale:v 2 output.avi
```
合并视频及音频文件
```
ffmpeg -i 0.mp4 -i 1.mp3 -c:v copy -c:a aac -strict experimental -map 0:v:0 -map 1:a:0 output.mp4
```
### 帧率设置
使用-r选项
语法是：
```
ffmpeg -i input -r fps output
```
例如：
```
ffmpeg -i input.avi -r 30 output.mp4
```
### 比特率设置
比特率也是一个决定音视频总体质量的参数。他决定每个时间单位处理的bit数。

设置比特率：比特率决定处理1s的编码流需要多少bits，设置用-b选项。区分音视频用-b:a和-b:v

例如：设置整体1.5Mbit每秒

```
ffmpeg -i file.avi -b 8M file.mp4

ffmpeg -i input.avi -b:v 1500K output.mp4
```
### 去除水印
设置: delogo=

水印位置：x=1000:y=15

水印大小：:w=250:h=160

显示绿框：:show=1（成品去除参数）

```
测试：
ffmpeg -i logo.mp4 -filter_complex "delogo=x=1000:y=15:w=250:h=160:show=1" delogo.mp4

水印：
ffmpeg -i logo.mp4 -filter_complex "delogo=x=1000:y=15:w=250:h=160" delogo.mp4
```


