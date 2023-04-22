score=[74,85,69,77,81]
print("テストの点数は",score,"です。")
highscore=[n for n in score if n>=80]
print("80点以上は",highscore,"です。")
print("80点以上の人数は",len(highscore),"です。")#リストの長さはlen(length)で表す。