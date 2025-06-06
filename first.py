import streamlit as st   #导入streamlit 库
import pandas as pd    #导入pandas 库
import time           #导入time库

st.title("🕶学生 小晶-数字档案")   #使用title()函数设置标题

st.header("🔑基础信息")    #使用header()函数设置章节
st.text("学生ID：ZSY-2023-13")    #用text()函数写学生ID
st.write("注册时间`2023-9-1 08：00：00`|精神状态：✅正常")  #用write()函数写注册时间
st.write("当前教室`实验楼301`|安全等级：`绝密`")     #用write()函数教室和安全等级

st.header("📊技能矩阵")    #使用header()函数设置章节
c1, c2 ,c3= st.columns(3)    #使用column()定义列3列布局 
c1.metric(label="C语言:revolving_hearts:", value="95%", delta="2%")   #使用metric()函数书写第一列内容
c2.metric(label="Python", value="87%", delta="-1%")    #使用metric()函数书写第一列内容
c3.metric(label="C语言:revolving_hearts:", value="68%", delta="-10%")   #使用metric()函数书写第一列内容

st.subheader("streamlit课程进度")    #使用header()函数设置子章节
st.progress(80) 
progress_text_1="streamlit课程进度"    #创建一个progress_text_1
my_bar=st.progress(28,progress_text_1)   #使用st.progress()函数初始化进度条的进度值和文本
time.sleep(0.5)    #使用sleep()函数设置时间间隔
for percent in range(30):  #循环
     time.sleep(0.1)    #使用sleep()函数设置时间间隔      my_bar. progress(percent+1,text=f'{progress_text_1}')   #使用sprogress()函数设置进度条的进度值和文本

st.header("📝任务日志")    #使用header()函数设置章节
data = {
    '日期':['2023-10-01', '2023-10-02', '2023-10-03'],
    '任务':['学生数字档案', '数据管理系统','课程管理系统'],
    '状态':['✅完成', '🕒进行时', '❌未完成' ],
    '难度':['★★☆☆☆', '★☆☆☆☆', '★★★☆☆' ]
}      # 创建data写数据
index = pd.Series(['0', '1', '2'], name='')    # 定义数据框所用的索引
df = pd.DataFrame(data, index=index)    #使用DataFrame()函数根据上面创建的data和index，创建数据框
st.dataframe(df)     #使用dataframe()函数生成数据框

st.subheader("🔐最新代码成果")    #使用header()函数设置子章节
st.code('''
def matrix_breach():
      while True:
            if detect_vulnerability():
               exploit()
               reyurn"ACCESS GRANTED"
            else:
                stealth_evade()
''', line_numbers=True)     #使用code()函数创建一个代码块并展示代码

st.markdown('***')      #使用markdown()函数分割线

st.write("`>>SYSTEM MESSAGE:`下一个目标已解锁...")   #使用write()函数展示方法写信息
st.write("`>>SYSTEM MESSAGE:`课程管理系统")       #使用write()函数展示方法写信息#写信息
st.write("`>>SYSTEM MESSAGE:`2025-06-04 17:39:58")      #使用write()函数展示方法写信息
st.write("系统状态：在线 连接状态：已加密")         #使用write()函数展示方法写信息
 