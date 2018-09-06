import pandas as pd
#import pandas.DataFrame.plot.line as Line
import sys
from pyecharts import Bar, Line, Pie, Overlap

city_dict = {'bj':'北京','sh':'上海','hz':'杭州','sz':'深圳'}

city_init = 'bj' if len(sys.argv) == 1 else sys.argv[1]
city = city_dict[city_init]

fileName = 'rent_lianjia_{}.txt'.format(city_init)
print(fileName)
f = open(fileName,'r')

df = pd.read_csv(f, sep=',', header=None, encoding='utf-8',
                 names=['area', 'title', 'type', 'square', 'orient', 'detail_place', 'floor', 'total_floor', 'price', 'year', 'unit_price'])

#df = df.round(2)

print(df.describe().round(2))   #list the statistic table of all the numerical columns
print(type(df.describe()))




def render_num_price(x): 
    #detail_place = df.groupby(['detail_place']) 
    detail_place = df.groupby([x[0]]) 
    house_com = detail_place['price'].agg(['mean','count']) 
    house_com.reset_index(inplace=True) 
    detail_place_main = house_com.sort_values('count',ascending=False)[0:20] 
     
    attr = detail_place_main[x[0]] 
    v1 = detail_place_main['count'].round(2)
    v2 = detail_place_main['mean'].round(2) 
     
    bar = Bar("{}主要{}房屋数量&月租均价".format(city, x[1]), "data from Lianjia.com")  
    #bar.use_theme("chalk")
    bar.add("数量",attr,v1,is_stack=True,xaxis_rotate=30,yaxix_min=4.2, 
        xaxis_interval=0,is_splitline_show=False) 
     
    line = Line("{}主要月租均价".format(city, x[1]), "data from Lianjia.com") 
    line.add("月租",attr,v2,is_stack=True,xaxis_rotate=30,yaxix_min=4.2, 
        mark_point=['min','max'],xaxis_interval=0,line_color='lightblue', 
        line_width=4,mark_point_textcolor='lightblue',mark_point_color='lightblue', 
        is_splitline_show=False) 
     
    overlap = Overlap() 
    overlap.add(bar) 
    overlap.add(line,yaxis_index=1,is_add_yaxis=True) 
    overlap.render('{}{}_数量月租分布.html'.format(city, x[1])) 



#城市x轴_房屋数量、均价分布图 
#xKey, xName
x_axis = [('detail_place','路段'),('area','区域'),('title','楼盘')]
for x in x_axis:
    render_num_price(x)


#房源价格区间分布图

price_info = df[['area', 'price']]

#对价格分区
bins = [0,1000,1500,2000,2500,3000,4000,5000,6000,8000,10000]
level = ['0-1000','1000-1500', '1500-2000', '2000-3000', '3000-4000', '4000-5000', '5000-6000', '6000-8000', '8000-1000','10000以上']
price_stage = pd.cut(price_info['price'], bins = bins,labels = level).value_counts().sort_index()

attr = price_stage.index
v1 = price_stage.values

theme = "{}价格区间&房源数量分布".format(city)
bar = Bar(theme)

bar.add("",attr,v1,is_stack=True,xaxis_rotate=30,yaxix_min=4.2,
    xaxis_interval=0,is_splitline_show=False)

overlap = Overlap()
overlap.add(bar)
overlap.render(theme+'.html')



#房屋面积分布

bins =[0,30,60,90,120,150,200,300,400,700]

level = ['0-30', '30-60', '60-90', '90-120', '120-150', '150-200', '200-300','300-400','400+']

df['square_level'] = pd.cut(df['square'],bins = bins,labels = level)

df_digit= df[['area', 'type', 'square', 'orient', 'total_floor', 'floor', 'year', 'price', 'square_level']]

s = df_digit['square_level'].value_counts()

attr = s.index
v1 = s.values

theme = "{}房屋面积分布".format(city)
pie = Pie(theme,title_pos='center')

pie.add(
    "",
    attr,
    v1,
    radius=[40, 75],
    label_text_color=None,
    is_label_show=True,
    legend_orient="vertical",
    legend_pos="left",
)
overlap = Overlap()
overlap.add(pie)
overlap.render(theme+'.html')


#房屋面积&价位分布
bins =[0,30,60,90,120,150,200,300,400,700]
level = ['0-30', '30-60', '60-90', '90-120', '120-150', '150-200', '200-300','300-400','400+']
df['square_level'] = pd.cut(df['square'],bins = bins,labels = level)

df_digit= df[['area', 'type', 'square', 'orient', 'total_floor', 'floor', 'year', 'price', 'square_level']]

square = df_digit[['square_level','price']]
prices = square.groupby('square_level').mean().reset_index()
amount = square.groupby('square_level').count().reset_index()

attr = prices['square_level']
v1 = prices['price']

theme = "{}房屋面积&价位分布".format(city)
pie = Bar(theme)
pie.add("", attr, v1, is_label_show=True)
pie.render(theme+'0.html')

bar = Bar(theme)
bar.add("",attr,v1,is_stack=True,xaxis_rotate=30,yaxix_min=4.2,
    xaxis_interval=0,is_splitline_show=False)

overlap = Overlap()
overlap.add(bar)
overlap.render(theme+'.html')
