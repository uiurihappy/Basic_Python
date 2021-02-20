# 모듈 : 필요한 것들이 부품처럼 잘 만들어진 파일

# import theater_module
# theater_module.price(3) #3명이서 영화를 보러 갔을 때 가격
# theater_module.price_moring(4) #4명이서 조조 할인 영화를 보러 갔을 때
# theater_module.price_soldier(5) #5명의 군인이 영화 보러갔을 때

# import theater_module as mv

# mv.price(3)
# mv.price_moring(4)
# mv.price_soldier(5)

# from theater_module import *
# price(3)
# price_moring(4)
# price_soldier(5)

# from theater_module import price, price_moring
# price(5)
# price_moring(6)

# from theater_module import price_soldier as price
# price(5) #price_soldier의 내용이 출력

# pakage : 모듈들을 모아놓은 하나의 집합
#import travel.thailand
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel.thailand import ThailandPackage
# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

# __all__

from travel import * 
# trip_to = vietnam.VietnamPackage()
trip_to  = thailand.ThailandPackage()
trip_to.detail()

import inspect
import random
print(inspect.getfile(random)) # C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python37_64\lib\random.py
print(inspect.getfile(thailand)) # c:\Users\차윤범\Desktop\Python\travel\thailand.py