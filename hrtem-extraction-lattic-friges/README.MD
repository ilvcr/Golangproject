1. `bin/`: 存放一些可执行文件。

2. `src/`: 存放项目的所有源代码。

   ​	(1) 源代码中的所有模块、包都放于此目录;

   ​	(2)不要置于顶层目录。

   ​	(3) 子目录`tests/`存放单元测试代码；

   ​	(4) 程序的入口为`main.py`。

3. `docs/`: 存放一些文档。

4. `setup.py`: 安装、部署、打包的脚本。

5. `requirements.txt`: 存放软件依赖的外部Python包列表。

6. `requirements_dev.txt` 比 `requirements.txt`文件增加了测试单元库

7. `README`: 项目说明文件。


##pip安装
#####获得requirements.txt文件
'''pip freeze > requirements.txt'''
#####安装requirements.txt文件
'''pip install -r requirements.txt'''

