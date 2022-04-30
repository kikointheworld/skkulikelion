from ast import ImportFrom
import random # random.choice([리스트]) 리스트 내 element 1개 임의로 나옴.
import time # time.sleep(1) : 1초에 한번씩쉰다.
# import pandas as pd


# menus = ["된장찌개", "피자", "치킨", "떡볶이", "라면", "감자튀김"]

# while(1):
#     lunch = random.choice([menus])
#     dinner = random.choice([menus])
#     pd.DataFrame(["123", "1231"])
#     print(pd)
#     time.sleep(1)




# information = {"고향":"수원", "취미":"영화관람", "좋아하는 음식":"국수"}
# foods = ["된장찌개", "피자", "제육볶음"]
# print(information.get("취미"))
# information["특기"] = "피아노"
# information["사는 곳"] = "서울"
# del information["좋아하는 음식"]
# print(information)
# information.clear()
# print(information)
# print(foods[2])
# foods.append("김밥")
# del foods[1]
# print(foods)


# information = {"고향":"수원", "취미":"영화관람", "좋아하는 음식":"국수"}

# for key, value in information.items():
#     print(key)
#     print(value)



# menu1 = set(["된장찌개", "피자", "제육볶음"])
# menu2 = set(["된장찌개", "떡국", "김밥"])
# menu3 = menu1 | menu2 # 합집합
# print(menu3)
# menu3 = menu1 & menu2 # 교집합
# print(menu3)
# menu3 = menu1 - menu2 # 차집합
# print(menu3)


# if 문..

# import random

# food = random.choice(["된장찌개","피자","제육볶음"])

# print(food)
# if(food == "제육볶음"):
#     print("곱배기 주세요")
# else:
#     print("그냥 주세요")
# print("종료")



lunch = ["된장찌개", "피자", "제육볶음", "짜장면"]

while True:
    print(lunch)
    item = input("음식을 추가 해주세요 : ")
    if(item == "q"):
        break
    else:
        lunch.append(item)
print(lunch)

set_lunch = set(lunch)

while True:
    print(set_lunch)
    item = input("음식을 삭제해 주세요. : ")
    if item == "q":
        break
    else:
        set_lunch -= set([item])

print(set_lunch, "중에서 선택합니다.")
print("5")
time.sleep(1)
print("4")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)


print(random.choice(list(set_lunch)))