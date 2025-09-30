#-----------UTILITY-----------#
import textwrap



#----------INPUTS-----------------#
name = input("Enter your name: ").strip().title()
profession = input("Enter your profession: ").strip().title()
passion = input("Enter your passion in one line: ").strip()
emoji = input("Enter your favourite emoji: ").strip()
website = input("Enter your webiste: ").strip()


#-----------OPTIONS-------------#
print("\nChoose your style: ")
print("1. Simple lines ")
print("2. Vertical flair ")
print("3. Emoji snadwich ")


style = int(input("\nEnter 1, 2 or 3: "))



#--------PURE FUNCTION-------#
def generate_bio(style):
    
    if style == 1:
        return f"{emoji} {name} | {profession} \n💡{passion}\n{website}" 
    
    elif style == 2:
        return f"{emoji} {name}\n{profession}🔥\n{passion}\n{website}🔥"
    elif style ==3:
        return f"{emoji*3}\n{name} - {profession}\n{passion}\n{website}\n{emoji*3}"
    
    else:
        print("Enter the number only from the options provided.")



bio = generate_bio(style = style)



print("\nYour stylish bio:\n")
print("*" * 50)
print(textwrap.dedent(bio))
print("*" * 50)



#-----------SAVE IF THEY WANT------------#
save = input("Do you want to save this bio to a text file?(y/n):").lower()

if save =='y':
    filename = f"{name.lower().replace(' ','_')}_bio.txt"
    with open(filename,'w',encoding='utf-8') as f:
        f.write(bio)
    print("file saved!")    