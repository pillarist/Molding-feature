import cv2
import numpy as np


class template_handler:

    def __init__(self,cam) -> None:
        self.main_loop = True
        self.cam = cam
        self.drawing = False
        self.templates = []
        self.storage = []
        cv2.namedWindow("Display",cv2.WINDOW_GUI_EXPANDED)
        cv2.add
        cv2.setMouseCallback("Display",self.box_draw)
        button = cv2.createButton('Printer', self.on_button_click, True, cv2.QT_PUSH_BUTTON)
        pic = np.zeros((100,100))
        cv2.rectangle(pic,[0,0],[640,20],(255,255,0),cv2.LINE_AA)
        print(button)


    def on_button_click(self,state,state2):
        print(int((len(self.templates))/2))


    def box_draw(self,event, x, y, flags, param):

        if event == cv2.EVENT_LBUTTONDOWN or self.drawing:
            if self.drawing == False:
                self.templates.append((x,y))
                self.templates.append((x,y))
                self.drawing = True
                #print("drawing enabled",len(self.templates)-1)
            
            if self.drawing == True:
                self.templates[len(self.templates) -1] = (x,y)
                #print("second value changed",self.templates[-1])

        if event == cv2.EVENT_LBUTTONUP:
            self.drawing = False
            #print("drawing Disabled")

    def pre_processing(self,image,store = 10):
        image = cv2.equalizeHist(cv2.cvtColor(image,
                                             cv2.COLOR_BGR2GRAY))
        
        self.storage.append(image)
        if len(self.storage) >= store:
            self.storage.pop(0) 

        return np.uint8((np.sum(self.storage,axis=0))/len(self.storage))
    
    
    def destriction(self):
        self.cam.release()
        cv2.destroyAllWindows()



    def main(self):
        
        while( self.main_loop):
            _,frame = self.cam.read()

            if _ == True:
                frame = self.pre_processing(image=frame)
                for count,template in  enumerate (self.templates):
                    #print("loop enterned")
                   
                    if template != self.templates[-1] and count%2 == 0:
                
                    
                        cv2.rectangle(frame, template, self.templates[count+1], (0, 255, 0), 2)
                        #print("rectangle drawn")

                cv2.imshow("Display",frame)

            if cv2.waitKey(1) & 0xff == ord("q"):
                self.main_loop = False

        


if __name__  == "__main__":

    obj = template_handler(cv2.VideoCapture(2))
    obj.main()



