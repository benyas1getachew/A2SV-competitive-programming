n=int(input())
phb={}
for i in range(n):
    inp = list(input().split())
    name=inp[0]
    num=inp[1]
    phb[name]=num

arr=""
try:
    # Read the first input
    inp_name = input()

    # Continue looping as long as there is input
    while inp_name:
        if inp_name in phb.keys():
            arr += inp_name + "=" + phb[inp_name] + "\n"
        else:
            arr += "Not found\n"
        
        # Read the next input
        inp_name = input()

    print(arr)

except EOFError:
    # Handle the end of input gracefully
    print(arr)
    pass
