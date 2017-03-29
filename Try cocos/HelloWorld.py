#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/29 15:04
# @Author  : mazicwong
# @File    : HelloWorld.py

import cocos

class HelloWorld(cocos.layer.Layer):
    def __init__(self):
        super(HelloWorld,self).__init__()

        #新建文字标签用于显示helloworld
        label = cocos.text.Label('Hello,world',
                                 font_name  = 'Times New Roman',
                                 font_size = 32,
                                 anchor_x='center',
                                 anchor_y='center'
                                 )
        label.position = 320,240
        self.add(label)

cocos.director.director.init() #新建一个窗口
main_scene = cocos.scene.Scene(HelloWorld())#新建场景，场景里只有一个层hello_layer
cocos.director.director.run(main_scene) #开始工作

# class PPX(cocos.sprite.Sprite):
#     def __init__(self):
#         super(PPX,self).__init__('ppx.png')
