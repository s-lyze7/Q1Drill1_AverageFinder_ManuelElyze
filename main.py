from pyscript import document

def compute_average(e):
    scr1 = document.getElementById("scr1").value
    scr2 = document.getElementById("scr2").value

    if not scr1 or not scr2: #check if the scores are inputted
        document.getElementById("average").innerText = "Enter both scores"
        document.getElementById("sagot").innerText = "Incomplete"
        return #to end the function

    try: #to make the answer float
        scr1 = float(scr1)
        scr2 = float(scr2)
#compute the average
        avg = (scr1 + scr2) / 2
        document.getElementById("average").innerText = f"{avg:.2f}"

        if avg >= 75:
            document.getElementById("sagot").innerText = "Passed"
        else:
            document.getElementById("sagot").innerText = "Failed"

    except ValueError: #to show that there are invalid inputs 
        document.getElementById("average").innerText = "Invalid"
        document.getElementById("sagot").innerText = "Error"
