import cv2

my_list = {}

# Enter the address of the image you are going to attach. If your python file and the image are in the same location, you can only enter the name.(e.g images.jpg)
im = cv2.imread("images.jpg") 
    
count=int(input("how many squares will you take"))
    
for _ in range(count):
    name=input("Enter the name of the section you will square")
    r = cv2.selectROI(im)   
    my_list[name] = r

print(my_list)
cv2.waitKey(0)
