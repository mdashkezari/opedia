from bokeh.plotting import figure, show
from bokeh.io import output_notebook


def jupytered():
    jup = False
    import __main__ as main
    if not hasattr(main, '__file__'):
        jup = True 
    return jup

def inline():
    res = False
    if jupytered():
        output_notebook()
        res = True
    return  res 
    
