"""
好友大乱斗 v0.1

-实现基本功能
-2019.1.17
"""


# 定义角色类
class P:
    # 生命值
    hp = 100
    # 魔法值
    mp = 100
    # 幸运值
    lucky = 0
    # 招式
    attack = []
    # 武器
    weapon = None


# 定义招式类
class Attack:
    # 招式修饰词
    attack_head = ""
    # 招式部位
    attack_body = ""
    # 招式伤害
    attack_power = 0
    # 招式攻击部位
    attack_aim = ""
