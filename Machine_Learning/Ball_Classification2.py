#Rough -> 1
#Smooth -> 0
#Tennis -> 1
#Cricket -> 2

def main():
    print("Ball Classification CaseStudy")

#   Encoding

    Features = [[35,"Rough"],[47,"Rough"],[90,"Smooth"],[48,"Rough"],[90,"Rough"],[35,"Rough"],[92,"Rough"],[35,"Rough"],[35,"Rough"],[35,"Rough"],[35,"Rough"]] 


    Labels = [1,1,2,"Tennis","Tennis","Tennis","Tennis","Tennis","Tennis","Tennis"]

    print("Features are :",Features)
    
    print("Labels are :",Labels)


if __name__ == "__main__":
    main()