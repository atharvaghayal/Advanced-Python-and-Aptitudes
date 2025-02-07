i=0
sem=int(input("Enter no.of semester: "))
for i in range(sem):
    sub=int(input(f"Enter no.of subjects in {i+1} semester: "))
mark= input("Marks obtained in semseter :").split()
marks=map(int,mark)
print("Marks for sem 1:", marks)
