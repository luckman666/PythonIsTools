#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Description: 抖音app刷评论
@Date       :2021/12/22
@Author     :xhunmon
@Mail       :xhunmon@gmail.com
"""
import random
import time

import uiautomator2 as u2

d = u2.connect()
d.implicitly_wait(80)


def review_douyin():  # 评论
    d.press("home")
    d.app_start('com.ss.android.ugc.aweme', stop=True)
    time.sleep(1)
    d(resourceId="com.ss.android.ugc.aweme:id/foj").click()  # 点击搜索
    time.sleep(1)
    d(resourceId="com.ss.android.ugc.aweme:id/et_search_kw").click()  # 点击输入框，预防键盘弹不起来
    keys = ['元宵节创意视频']  # , '情人节', '搞笑视频', '真人动漫特效'
    comments = ['[比心]', '[强壮]', '[击掌]', '[给力]', '[爱心]', '[派对]', '[不看]', '[炸弹]', '[憨笑]', '[悠闲]', '[嘿哈]', '[西瓜]', '[咖啡]',
                '[太阳]', '[月亮]', '[发]', '[红包]', '[拳头]', '[勾引]', '[胜利]', '[抱拳]', '[左边]', '[送心]', '[来看我]', '[来看我]',
                '[来看我]', '[灵机一动]', '[耶]', '[色]', '[震惊]', '[小鼓掌]', '[发呆]', '[偷笑]', '[石化]', '[思考]', '[笑哭]', '[奸笑]',
                '[坏笑]', '[得意]', '[钱]', '[亲亲]', '[愉快]', '[玫瑰]', '[赞]', '[鼓掌]', '[感谢]', '[666]', '[胡瓜]', '[啤酒]', '[飞吻]',
                '[紫薇别走]', '[听歌]', '[绝望的凝视]', '[不失礼貌的微笑]', '[吐舌]', '[呆无辜]', '[看]', '[熊吉]', '[黑脸]', '[吃瓜群众]', '[呲牙]',
                '[绿帽子]', '[摸头]', '[皱眉]', '[OK]', '[碰拳]', '[强壮]', '[比心]', '[吐彩虹]', '[奋斗]', '[敲打]', '[惊喜]', '[如花]', '[强]',
                '[做鬼脸]', '[尬笑]', '[红脸]', '牛啊', '牛啊牛', 'nb', '666', '赞一个', '赞', '棒', '学到了', '1', '已阅', '板凳',
                '插一楼：变戏法的亮手帕', '插一楼：狗吃豆腐脑', '插一楼：癞蛤蟆打伞', '插一楼：离了水晶宫的龙', '插一楼：盲人聊天', '插一楼：五百钱分两下', '插一楼：盲公戴眼镜',
                '插一楼：王八倒立', '插一楼：癞蛤蟆背小手', '插一楼：韩湘子吹笛', '插一楼：剥了皮的蛤蟆', '插一楼：马蜂蜇秃子', '插一楼：冷水烫鸡', '插一楼：老孔雀开屏', '插一楼：大姑娘养的',
                '插一楼：三角坟地', '插一楼：蜡人玩火', '插一楼：发了霉的葡萄', '插一楼：厥着看天', '插一楼：种地不出苗', '插一楼：老虎头上的苍蝇', '插一楼：雷婆找龙王谈心',
                '插一楼：菩萨的胸怀', '插一楼：牛屎虫搬家', '插一楼：变戏法的拿块布', '插一楼：老虎上吊', '插一楼：王八', '插一楼：老虎吃田螺', '插一楼：大肚子踩钢丝', '插一楼：耗子腰粗',
                '插一楼：乌龟的', '插一楼：神仙放屁', '插一楼：麻油煎豆腐', '插一楼：汽车坏了方向盘', '插一楼：病床上摘牡丹', '插一楼：芝麻地里撒黄豆', '插一楼：打开棺材喊捉贼',
                '插一楼：卤煮寒鸭子', '插一楼：鲤鱼找鲤鱼，鲫鱼找鲫鱼', '插一楼：癞蛤蟆插羽毛', '插一楼：烂伞遮日', '插一楼：老虎头上的苍蝇', '插一楼：三角坟地', '插一楼：卖布兼卖盐',
                '插一楼：耗子腰粗', '插一楼：老孔雀开屏', '插一楼：筐中捉鳖', '插一楼：拐子进医院', '插一楼：茅房里打灯笼', '插一楼：癞蛤蟆背小手', '插一楼：肉骨头吹喇叭',
                '插一楼：老鼠进棺材', '插一楼：种地不出苗', '插一楼：病床上摘牡丹', '插一楼：裤裆里摸黄泥巴', '插一楼：狗拿耗子', '插一楼：铁匠铺的料', '插一楼：高梁撒在粟地里',
                '插一楼：茅厕里题诗', '插一楼：痰盂里放屁', '插一楼：老母猪打喷嚏', '插一楼：厕所里点灯', '插一楼：棺材铺的买卖', '插一楼：老公鸡着火', '插一楼：乌龟翻筋斗',
                '插一楼：被窝里的跳蚤', '插一楼：赶着牛车拉大粪', '插一楼：老太婆上鸡窝', '插一楼：狗背上贴膏药', '插一楼：狗咬瓦片', '插一楼：哪吒下凡', '插一楼：二十一天不出鸡',
                '插一楼：鞭炮两头点', '插一楼：抱黄连敲门', '插一楼：猫儿踏破油瓶盖', '插一楼：和尚念经', '插一楼：裁缝不带尺', '插一楼：上山钓鱼', '插一楼：狗长犄角',
                '插一楼：带着存折进棺材', '插一楼：豁子拜师', '插一楼：宁来看棋', '插一楼：盲公戴眼镜', '插一楼：南来的燕，北来的风', '插一楼：杯水车薪', '插一楼：玉皇大帝放屁',
                '插一楼：给刺儿头理发', '插一楼：九月的甘蔗', '插一楼：两只公牛打架', '插一楼：百川归海', '插一楼：挨打的乌龟', '插一楼：和尚挖墙洞', '插一楼：八月十五蒸年糕',
                '插一楼：毒蛇钻进竹筒里', '插一楼：苍蝇叮菩萨', '插一楼：白布进染缸', '插一楼：粪堆上开花', '插一楼：癞蛤蟆上蒸笼',
                '插楼：沙漠里钓鱼', '插楼：青㭎树雕菩萨', '插楼：看鸭勿上棚', '插楼：下大雨前刮大风', '插楼：在看羊的狗', '插楼：耍大刀里唱小生', '插楼：罗锅上山', '插楼：大车不拉',
                '插楼：瞎子白瞪眼', '插楼：铁拐的葫芦', '插楼：苣荬菜炖鲇鱼', '插楼：旅馆里的蚊子', '插楼：石刻底下的冰瘤子', '插楼：吃稀饭摆脑壳', '插楼：叫化子背不起', '插楼：火车拉大粪',
                '插楼：寿星玩琵琶', '插楼：六月的腊肉', '插楼：夜叉骂街', '插楼：孩儿的脊梁', '插楼：长了个钱串子脑袋', '插楼：现场看乒乓球比赛', '插楼：寡妇梦丈夫', '插楼：马背上放屁',
                '插楼：落雨出太阳', '插楼：猴子捡生姜', '插楼：啄木鸟屙薄屎', '插楼：鸡毛扔火里', '插楼：油火腿子被蛇咬', '插楼：属秦椒的', '插楼：千亩地里一棵草', '插楼：药铺倒了',
                '插楼：黄连水做饭', '插楼：卸架的黄烟叶儿', '插楼：螺蛳壳里赛跑', '插楼：躲了和尚躲不了庙', '插楼：驴槽子里面伸出一颗头来', '插楼：老妈妈吃火锅', '插楼：阎王的脸',
                '插楼：吃粮勿管事', '插楼：脚跟拴石头', '插楼：麻秸秆儿打狼', '插楼：阎王7粑子', '插楼：画上的美女', '插楼：团鱼下滚汤', '插楼：孔夫子的脸', '插楼：曹操贪慕小乔',
                '插楼：蒙住眼睛走路', '插楼：炒菜不放盐', '插楼：三月里的桃花', '插楼：老鼠吃面饽', '插楼：粥锅里煮铁球', '插楼：戴起眼镜喝滚茶', '插楼：吃香油唱曲子', '插楼：过冬的咸菜缸',
                '插楼：三个小鬼没抓住', '插楼：对着坛子放屁', '插楼：赤骨肋受棒', '插楼：百灵鸟唱歌', '插楼：雨过天晴放干雷', '插楼：拄着拐棍上炭窑', '插楼：搁着料吃草', '插楼：王八碰桥桩',
                '插楼：水上油', '插楼：偷鸡不得摸了一只鸭子', '插楼：黄瓜熬白瓜', '插楼：海瑞的棺材', '插楼：蛤蟆翻田坎', '插楼：乌龟进砂锅', '插楼：夜壶出烟', '插楼：李逵骂宋江',
                '插楼：小孩买个花棒槌', '插楼：漏网之虾', '插楼：一口吹灭火焰山', '插楼：冷水调浆']
    for key in keys:
        # 不能搜索search
        d(resourceId="com.ss.android.ugc.aweme:id/et_search_kw").clear_text()  # 清除历史
        d(resourceId="com.ss.android.ugc.aweme:id/et_search_kw").set_text(key)  # 输入
        time.sleep(1)
        d(text='搜索', className='android.widget.TextView').click()  # 点击搜索
        # d(resourceId="	com.ss.android.ugc.aweme:id/d0t").click()  # 点击搜索
        time.sleep(1)
        d(text='视频', className='android.widget.Button').click()  # 点击视频，然后点击第一条
        d.xpath(
            '//*[@resource-id="com.ss.android.ugc.aweme:id/gw1"]/android.widget.FrameLayout[1]').click()
        stop, index = random.randint(15, 30), 0
        while index < stop:  # 随机刷几十条
            print('总共有：{}条 | 现在到：{}条'.format(stop, index))
            try:
                time.sleep(random.randint(3, 12))  # 随机停顿1~5秒
                d(resourceId="com.ss.android.ugc.aweme:id/b2b").click()  # 点击评论按钮
            except Exception as e:
                print(e)
            try:
                time.sleep(random.randint(1, 2))  # 随机停顿1~2秒
                d(resourceId="com.ss.android.ugc.aweme:id/b1y").click()  # 点击弹出键盘
            except Exception as e:
                print(e)
            time.sleep(random.randint(1, 2))  # 随机停顿1~2秒
            try:
                d(resourceId="com.ss.android.ugc.aweme:id/b1y").set_text(
                    comments[random.randint(0, len(comments) - 1)])  # 输入
            except Exception as e:
                print(e)
            try:
                time.sleep(random.randint(1, 2))  # 随机停顿1~2秒
                d(resourceId="com.ss.android.ugc.aweme:id/b1r").click()  # 发送
            except Exception as e:
                print(e)
            try:
                time.sleep(random.randint(1, 2))  # 随机停顿1~2秒
                d(resourceId="com.ss.android.ugc.aweme:id/back_btn").click()  # 关闭
            except Exception as e:
                print(e)
            try:
                time.sleep(random.randint(5, 15))  # 随机停顿1~5秒
                d.swipe_ext("up")  # 上划，下一个视频
            except Exception as e:
                print(e)
            index += 1
        d(resourceId="com.ss.android.ugc.aweme:id/back_btn").click()  # 返回搜索


'''
教程：
1. 使用 weditor 来查看元素
2. 当找不到resourceId时，先用d(text='画动漫人物', className='android.widget.EditText').info找个resourceId，再使用。因为输入框内容会变化，所有不能直接用。
'''

if __name__ == "__main__":
    review_douyin()
