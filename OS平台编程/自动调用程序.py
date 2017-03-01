#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import sched, time


# sched的函数不超过10个,但都很好用
def print_time(msg='default'):
    print("当前时间", time.time(), msg)


# sched.scheduler() 用来创建一个调度任务
s = sched.scheduler(time.time, time.sleep)
print(time.time())
s.enter(5, 1, print_time, argument=('延迟5秒,优先级1',))  # 时间间隔,执行优先级,调用的函数,函数参数
s.enter(3, 2, print_time, argument=('延迟3秒,优先级2',))
s.enter(3, 1, print_time, argument=('延迟3秒,优先级1',))
s.run()  # 执行调度事件
print(time.time())
