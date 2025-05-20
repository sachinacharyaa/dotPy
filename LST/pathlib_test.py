# from pathlib import Path

# path = Path("emails")
# print(path.mkdir())          # it create directory
# print(path.rmdir())          # it remove directory




from pathlib import Path

path = Path()

for file in  path.glob('*.py'):   #it find .py file in current directory
 print(file) 
