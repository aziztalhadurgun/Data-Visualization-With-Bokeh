from bokeh.plotting import figure, output_file, show, save, ColumnDataSource
from bokeh.models.tools import HoverTool
from bokeh.transform import factor_cmap
from bokeh.palettes import Category20c
import pandas

#read csv
df = pandas.read_csv('cars.csv')

source = ColumnDataSource(df)

car = df['Car']
hp = df['Horsepower']

output_file('index.html')

#car list
car_list = source.data['Car'].tolist()

p = figure(
    y_range = car_list,
    plot_width = 800,
    plot_height = 600,
    title = 'Cars With Top Horsepower',
    x_axis_label = 'Horsepower',
    tools="pan,box_select,zoom_in,zoom_out,save,reset"
)

#render glyph
p.hbar(
    y='Car',
    right='Horsepower',
    left=0,
    height=0.4,
    #color='orange',
    fill_color=factor_cmap(
        'Car',
        palette=Category20c[12],
        factors=car_list
    ),
    fill_alpha=0.9,
    source=source,
    legend = 'Car'
)

#add legend
p.legend.orientation = 'vertical'
p.legend.location = 'top_right'
p.legend.label_text_font_size = '10px'

#Add Tooltips hover
hover = HoverTool()
hover.tooltips = """
    <div>
        <h3>@Car</h3>
        <div><strong>Price: </strong>@Price</div>
        <div><strong>HP: </strong>@Horsepower</div>
        <div><img src="@Image" alt="" width=200 /></div>
    </div>
"""
p.add_tools(hover)

#show result
show(p)

#save file
#save(p)