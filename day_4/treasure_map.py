row1=['🥷🏻','🥷🏻','🥷🏻']
row2=['🥷🏻','🥷🏻','🥷🏻']
row3=['🥷🏻','🥷🏻','🥷🏻']
map=[row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
position=(input('where do you wanna enter the X'))
col=int(position[0])-1
row=int(position[1])-1
map[col][row]="X"

print(f"{row1}\n{row2}\n{row3}")
