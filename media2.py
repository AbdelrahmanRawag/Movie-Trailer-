# this import the webbrowser function to open the site
import webbrowser
# this is the movie class who contains the constructor init and the webbrowser function
class Movie() :
# this is constructor init and it called once for every instance of the class I create 
    def __init__ (self,title,youtube,story_info,photo):
        self.title =title
        self.youtube =youtube
        self.story_info =story_info
        self.photo =photo
# this is the fuction which open the website 
    def show_trailer(self):
        webbrowser.open(self.youtube)
    
