import kivy     
from kivy.app import App    
from kivy.uix.widget import Widget   
from kivy.uix.label import Label    
from kivy.uix.gridlayout import GridLayout   
from kivy.uix.checkbox import CheckBox    
      
class checkboxDemo(GridLayout):   
    def __init__(self, **kwargs):   
    
        super().__init__()   
        
        self.cols = 2  
        
           
        self.add_widget(Label(text ='Python')) #add checkbox  
        self.check = CheckBox(active = True)   
        self.add_widget(self.check)   
        
        self.add_widget(Label(text ='C'))   
        self.check = CheckBox(active = False)   
        self.add_widget(self.check)   
        
        self.add_widget(Label(text ='C++'))   
        self.check= CheckBox(active = False)   
        self.add_widget(self.check)  
                    
        self.add_widget(Label(text ='Java'))   
        self.check = CheckBox(active = True)   
        self.add_widget(self.check)   
        
        self.add_widget(Label(text ='Other'))   
        self.check = CheckBox(active = False)   
        self.add_widget(self.check)  
       
class CheckBox_App(App):   
    def build(self):         
        return checkboxDemo()  
              
root= CheckBox_App()  
root.run()  
