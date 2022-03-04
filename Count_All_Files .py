import os

TotalFiles = 0
Errors = 0
Lines = []
FileAddress = []
for Root, _ , Files in os.walk(os.getcwd(), topdown=False):
    TotalFiles += len(Files)
    for FilesName in Files:
        try:
            with open(os.path.join(Root, FilesName), "r") as Line:
                Count = sum(1 for _ in Line)
                Lines.append(Count)
                FileAddress.append(f"{Root}\\{FilesName}".replace("\\", "/"))
        except:
            Errors += 1


print(f"\nTotal Files: {TotalFiles}")
print(f"Uncountable Files: {Errors}\n")

print(f"Total Line: {sum(Lines)}")
print(f"Biggest File Line: {max(Lines), FileAddress[Lines.index(max(Lines))]}")
print(f"Smallest File Line: {min(Lines), FileAddress[Lines.index(min(Lines))]}")

input("\nPress Enter to exit...")