import json,random
from pyecharts import Bar,Map,Page,Style,Geo,Pie,WordCloud


with open("item.json",'r',encoding='utf-8') as f:
    data=json.load(f)

city_all = {}
money_all = {}
profession_all = {}
experience_all = {}
welfare_all = {}

for index ,result in enumerate(data):
    #统计地区
    city_all[result['city']]=city_all.get(result['city'], 0) + 1

    #工资区间
    money_all[result['salary']]=money_all.get(result['salary'],0)+1

    #学历统计
    profession_all[result['profession']]=profession_all.get(result['profession'],0)+1

    #工作经验
    experience_all[result['experience']]=experience_all.get(result['experience'],0)+1

    #福利情况 随机选20个
    welfare_all[result['welfare']]=random.randint(1,30)


def geo_map(data,title):
    page =Page()
    style = Style(
        title_color="#fff",
        title_pos="center",
        width=800,
        height=400,
        background_color='#c4ccd3'
    )
    kwargs = dict(
        maptype='china',
        is_visualmap=True,
        type="effectScatter",
        is_legend_show=False,
        geo_emphasis_color='c4ccd3',
        visual_text_color='#2f4554'

    )
    # 创建地图模型
    chart = Geo(title, "", **style.init_style)
    attr, value = chart.cast(data)
    # 添加数据
    chart.add("", attr, value, **kwargs)
    page.add_chart(chart)
    return page

'''
 create by: lxl
 description: 工作经验 分布
 create time: 2019-03-26 16:45  
 @:paramter:
 @:return 
 '''
def create_experience(data,title):
    page = Page()
    style = Style(
        width=800,
        title_pos="center",
        height=400,
        background_color='#c4ccd3'

    )
    kwargs = dict(
        radius=(40, 75),
        label_text_color=None,
        is_label_show=True,
        legend_orient='her',
        legend_pos='left'

    )
    experience_chart = Pie(title, **style.init_style)
    attr, value = experience_chart.cast(data)
    experience_chart.add("", attr, value, **kwargs)
    page.add(experience_chart)
    return page
'''
 create by: lxl
 description: 学历要求
 create time: 2019-03-26 16:47  
 @:paramter:
 @:return 
 '''
def create_profession(data,title):
    page = Page()
    style = Style(
        width=900,
        height=400,
        title_pos="center",
        background_color='#c4ccd3'
    )
    kwargs = dict(
        radius=(40, 75),
        label_text_color=None,
        is_label_show=True,
        legend_orient='her',
        legend_pos='left'

    )
    profession_chart = Pie(title, **style.init_style)
    attr, value = profession_chart.cast(data)
    profession_chart.add("", attr, value, **kwargs)
    page.add(profession_chart)
    return page

'''
 create by: lxl
 description: 福利词云
 create time: 2019-03-26 16:49  
 @:paramter:
 @:return 
 '''
def create_welfare(data,title):
    page = Page()
    style = Style(
        width=1000,
        height=500,
        background_color='#c4ccd3'
    )
    kwargs = dict(
        shape='circle',
        title_pos="center"

    )
    welfare_chart = WordCloud(title, **style.init_style)
    attr, value = welfare_chart.cast(data)
    welfare_chart.add("", attr, value,**kwargs)
    page.add(welfare_chart)
    return page

def create_money(data,title):
    page = Page()
    style = Style(
        width=1000,
        height=500,
        background_color='#c4ccd3'
    )
    money_chart = Bar(title, **style.init_style)
    attr, value = money_chart.cast(data)
    money_chart.add("", attr, value, is_label_show=True)
    page.add(money_chart)
    return page

if __name__ == '__main__':
    geo_map(city_all,"城市分布").render("city.html")
    create_experience(experience_all,"经验要求").render("experience.html")
    create_profession(profession_all,"学历要求").render("profession.html")
    create_welfare(welfare_all,"福利").render("welfare.html")
    create_money(money_all,"工资区分分布").render("money.html")