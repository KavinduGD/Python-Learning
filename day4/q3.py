line1=[" "," "," "]
line2=[" "," "," "]
line3=[" "," "," "]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")

position = input()

verticle=0
if position[0]=="A":
    verticle=0
elif position[0]=="B":
    verticle=1
else:
    verticle=2
    
map[int(position[1])-1][verticle]="x"

print(f"{line1}\n{line2}\n{line3}")
    
