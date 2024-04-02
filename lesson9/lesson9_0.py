def calculate_bmi(height:int, weight:int) -> float:
    return bmi

def bmi_advice(bmi:float) -> str:
    # 提供建議
    if bmi < 18.5:
        return "體重過輕"
    elif 18.5 <= bmi < 24:
        return "正常範圍"
    elif 24 <= bmi < 27:
        return "過重"
    elif 27 <= bmi < 30:
        return "輕度肥胖"
    else:
        return "重度肥胖"

names:list[dict] = [
    {'name':'徐xx','height':178,'weight':78},
    {'name':'王xx','height':168,'weight':75},
    {'name':'張xx','height':183,'weight':78},
]

for person in names:
    bmi:float = calculate_bmi(person['height'], person['weight'])
    advice:str = bmi_advice(bmi)
    print(f"{person['name']}的 BMI 為：{bmi:.2f}，屬於'{advice}'範疇。")