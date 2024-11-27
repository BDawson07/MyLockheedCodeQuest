

#fetches file
def get_inputs(filename:str) -> None:
    global inputs
    inputs = []
    with open(f"{filename}.txt","r") as file:
        for i in file.readlines():
            inputs.append(i)

#set up code
def init(filename:str) -> None:
    get_inputs(filename)

#Return the lines of the file
def input() -> str:
    i = str(inputs[0]).rstrip()
    inputs.remove(inputs[0])
    return i
