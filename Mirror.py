#Program to Solve Physics Problems related to mirror formula

def mirror():
    whatToDerive=input("What value do you want to find? ")
    

    if whatToDerive=="v":
        f=float(input("Focal Lenght (Please ensure proper sign): "))
        u=float(input("Object distance (Please ensure proper sign): "))
        v=(f*u)/(u-f)
        if v>0:
            state="Virtual and Erect"
            m=(-v)/u
        elif v<0:
            state="Real and inverted"
            m=-v/u
        return f"Object Distance= {v} \nState=  {state} \nMagnification= {m}"
    
    elif whatToDerive=="u":
        f=float(input("Focal Lenght (Please ensure proper sign): "))
        v=float(input("Image distance (Please ensure proper sign): "))
        u=(f*v)/(v-f)
        m=(-v)/u
        return f"Object Distance= {u} \nMagnification= {m}"
    
    elif whatToDerive=="f":
        v=float(input("Image distance (Please ensure proper sign): "))
        u=float(input("Object distance (Please ensure proper sign): "))
        f=(u*v)/(u+v)
        m=(-v)/u
        return f"Object Distance= {f} \nMagnification= {m}"
    
    else:
        print("Please enter correctly. The options are v/u/f")
        mirror()

print(mirror())