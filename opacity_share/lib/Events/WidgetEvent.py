from Events import Event
class WidgetEvent(Event):

    def __init__(self,widget,event,replace=False):
        super().__init__()
        widget.bind(event,self.happened,not replace)

    def happened(self,e):
         
