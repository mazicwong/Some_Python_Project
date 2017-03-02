#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#教程https://www.shiyanlou.com/courses/running
import curses
from random import randrange,choice
from collections import defaultdict


##用户行为
actions = ['Up','Left','Down','Right','Restart','Exit']
#考虑到大写开启,要获得有效键值列表
letter_codes=[ord(ch) for ch in 'WASDRQwasdrq']
#输入与行为进行关联
actions_dict=dict(zip(letter_codes,actions*2))

##状态机



def main(strscr):
    def init():
        #init the game
        return 'Game'
    def not_game(state):
        #wirte down the iterface of GAMEOVER/WIN
        #get what user's input,judge restart a game or close it
        responses=defaultdict(lambda:state)
        responses['Restart'],responses['Exit']='Init','Exit'
        return responses[action]
    def game():
        #wirte down the chess tatus
        #get the user's input about 'action'
        if action=='Restart':
            return 'Init'
        if action=='Exit':
            return 'Exit'
        #if 成功移动一步
            if ying:
                return 'Win'
            if shibai:
                return 'Gameover'
        return 'Game'
    state_actions={
        'Init':init,
        'Win':lambda:not_game('Win')
        'Gamevoer':lambda:not_game('Gameover')
        'Game':game
    }
    state='Init'
    while state != 'Exit':
        state=state_actions[state]()
