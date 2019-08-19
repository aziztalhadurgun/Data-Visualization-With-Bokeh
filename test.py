from bokeh.plotting import figure, output_file, show

x = [1,2,3,4,5]
y = [3,5,1,3,2]

output_file('index.html')

#add plot
p = figure(
    title = 'Simple Test',
    x_axis_label = 'X',
    y_axis_label = 'Y'
)
#render glyph
p.line(x,y, legend="Test", line_width=2)

show(p)