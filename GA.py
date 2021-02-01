p_list = ["01101", "11000", "01000", "10011"]
c_list = []
f_list = []
prob_list = []
def dec_conversion(p_list):
    for x in range(len(p_list)):
        str_length = len(p_list[x])
        num = int(p_list[x])
        sum = 0
        for i in range(str_length):
            p = pow(2, i) * (num % 10)
            num = round(num / 10)
            sum += p
        c_list.append(sum)

def fitness(c_list):
    for x in range(len(c_list)):
        f = pow(c_list[x], 2)
        f_list.append(x)

total = 0
for i in range(len(c_list)):
    total += c_list[i]

def prob(f_list):
    for n in range(len(f_list)):
        prob = f_list[n] / total
        prob_list.append(prob)

print(prob_list)
