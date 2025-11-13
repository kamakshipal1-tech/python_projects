questions={"capital of india?":"delhi","5+7":"12","python is":"language"}
score=0
for q,a in questions.items():
    if input(q).lower()==a:
        score += 1
        
        print(score)