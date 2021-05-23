# 目录结构
## page
- base_page.py: driver驱动与原生API的二次封装；    
- page对象: 继承 base_page 后，完成对各页面的封装；   
## testcase
文件夹内统一存放所有的测试用例，调用 page 对象实现业务并断言；  
## common
文件夹内存放对其他功能封装，改进原生框架不足；  
## data
文件夹数据构造与测试用例的数据封装；  

# 复用浏览器，获取cookie
- 配置Chrome浏览器环境变量
- 进入Chrome浏览器安装目录下，打开终端
- 执行：chrome --remote-debugging-port=9222
- 运行在common_fun文件中运行write_data("cookie.yaml", get_cookie())，将cookies信息存到对应的文件中