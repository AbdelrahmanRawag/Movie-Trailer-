import webbrowser
class Movie() :
    def __init__ (self,title,youtube,story_info,photo):
        self.title =title
        self.youtube =youtube
        self.story_info =story_info
        self.photo =photo
    def show_trailer(self):
        webbrowser.open(self.youtube)
    
