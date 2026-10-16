from pyscript import document

grade7={"La, Lo, Woo, Ha"}
grade8 = {"Anikka Lin", "Archi Pantalone", "Marry Sterling", "Lovlie Hertsz"}
grade9 ={"Cutie Lance", "Pretty Maise", }
grade10= {"Lily", "Mia", "Ava", "Sophia"}

def addmembers(event):
    grade = document.getElementById("grade").value
    name = document.getElementById("name").value

    if grade == "7":
        grade7.add(name)
        document.getElementById("output").innerHTML = f"Added {name} to Grade 7"
    elif grade == "8":
        grade8.add(name)
        document.getElementById("output").innerHTML = f"Added {name} to Grade 8"
    elif grade == "9":
        grade9.add(name)
        document.getElementById("output").innerHTML = f"Added {name} to Grade 9"
    elif grade == "10":
        grade10.add(name)
        document.getElementById("output").innerHTML = f"Added {name} to Grade 10"
    else:
        document.getElementById("output").innerHTML = "Invalid grade level"

        display(grade7|grade8|grade9|grade10, target='output')