# MC全版本(支持第三方客户端)锁输入法

> 有用请把右上角的Star点成黄色行吗,谢谢

## 更新内容

> 基岩版自带输入法修复,不需要使用本工具

1. 修复输入指令不会切换的bug
2. 增加对网易版的支持
3. 修复切换窗口触发输入法的bug
4. 修复不是使用esc返回游戏引发的输入法错误

## BuildCommand/生成指令

> 建议懂命令行再来弄, 不会弄这步请不要去提交错误报告

```bat
:: 安装依赖
python -m pip install PyInstaller
:: 执行生成
python -m PyInstaller -w -F lockmain.py
```

## 报错修复指南

> 如果此处没有你的错误, [点击此处](https://github.com/chenmy1903/MinecraftIMELock/issues/new)去提交一个错误报告

### 切换输入法失败

1. 尝试安装`英语(美国)`输入法
2. 修改文件中的`your_ime_id`, 参考[此处](https://msdn.microsoft.com/en-us/library/cc233982.aspx)修改为你的输入法id
3. 尝试使用Windows10/11系统
4. 如果上方解决方案都尝试了, 但是仍未修复: [点击此处](https://github.com/chenmy1903/MinecraftIMELock/issues/new)去提交错误报告(记得带输入法配置)

### 出现ModuleNotFoundError

1. 请下载本软件的最新版
2. 如果是手动运行(不是使用python运行), 请打开一个`管理员命令提示符`, 并在窗口中输入`pip install pywin32 PyQt5 pynput`
3. 如果上方解决方案都尝试了, 但是仍未修复: [点击此处](https://github.com/chenmy1903/MinecraftIMELock/issues/new)去提交错误报告(把程序代码放进去, 使用MD语言的代码块, 不是md语言代码块不接受, 因为可读性太差了)

### 开启软件后没有作用

1. 不要使用自定义的Minecraft标题去运行
2. 如果使用的是其他客户端, [点击此处](https://github.com/chenmy1903/MinecraftIMELock/issues/new)将客户端的名称提交给作者

## 已支持的客户端

> 已知问题: Lunar端使用本软件窗口会左右横跳, 加载时请勿开启此软件, 加载完成后打开即可

1. 原版
2. 坏狮子(BadLion)
3. LunarClient
4. Feather
5. LiquidBounce
6. 垃圾网易版(Java版)

## 使用方法

> 软件说明如题

1. 启动软件
2. 开启游戏
3. 正常的玩
4. 玩完关游戏
5. 按f12关软件
