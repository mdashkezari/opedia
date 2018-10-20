from bokeh.plotting import figure, show
from bokeh.io import output_notebook


def inline():
    import __main__ as main
    if not hasattr(main, '__file__'):
        output_notebook() 
    return  
    
inline()    