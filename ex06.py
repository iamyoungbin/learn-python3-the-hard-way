사람의_종류 = 10
x = f"세상에는 {사람의_종류} 종류의 사람이 있어요."

이진수 = "'이진수'"
모르는 = "모르는"

y = f"{이진수}를 아는 사람과 {모르는} 사람."

print(x)
print(y)

print(f"'{x}'라고 했어요.")
print(f"'{y}'이라고도 했죠.")

웃김 = False
농담_평가 = "웃기는 농담 아니에요?! {}"

print(농담_평가.format(웃김))

w = "이 문자열의 왼쪽 ->"
e = "<- 이 문자열의 오른쪽"

print(w + e)
