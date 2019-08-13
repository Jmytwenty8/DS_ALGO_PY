from stack import Stack



def is_matched(top, rn):
    if top == "{" and rn =="}":
        return True
    elif top == "[" and rn == "]":
        return True
    elif top == "(" and rn == ")":
        return True
    else:
        return False

def is_paren_balanced(paren_string):
    s = Stack()
    is_balanced = True
    index = 0
    


    while index < len(paren_string) and is_balanced:
        paren = paren_string[index]
        if paren in "({[" and is_balanced:
            s.push(paren)
        
        else :
            if s.is_empty():
                is_balanced = False
            else:
                top = s.pop()
                if not is_matched(top, paren):
                    is_balanced = False
        
        index +=1
    if s.is_empty and is_balanced:
        return True
    else:
        return False

print(is_paren_balanced("{}}"))
