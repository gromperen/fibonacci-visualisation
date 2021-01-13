import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.collections import PatchCollection
from matplotlib.patches import Arc

def fibonacci(n=10):
    a = 0
    b = 1
    for i in range(n):
        c = a + b
        yield (c, b)
        a = b
        b = c

def rechtecke(max_n=10):
    nums = list(fibonacci(max_n))
    nums.reverse()  # Reverse die liste weil es einfacher ist von gross zu klein zu machen

    fig, axis = plt.subplots(1) # machen rechteckigen plot mit matplotlib
    last_x, last_y = nums[0]

    axis.set_xlim(0, last_x )
    axis.set_ylim(0, last_y)

    plt.axis('off')

    origin  = [0, 0]
    rechtecke = []

    for i, (cur_num, prev_num) in enumerate(nums):
        if (i - 1) % 4 == 0:                # Jedes vierte rechteck (ab i = 1) [1,5,9,13,...] ist auf der X - Achse um den ihren wert verschoben
            origin[0] = origin[0] + cur_num
        elif (i - 4) % 6 == 0:              # Jedes sechste rechteck (ab i = 4) [4, 10, 16, 20, ...] ist auf der Y Achse um ihren wert verschoben
            origin[1] = origin[1] + cur_num
        if i % 2 == 1:                      # Jedes zweite rechteck wird anstatt l*b zu b*l
            cur_num, prev_num = prev_num, cur_num
        rechteck = Rectangle(origin, cur_num, prev_num, angle=0.0, antialiased=True)
        rechtecke.append(rechteck)

    coll = PatchCollection(rechtecke, facecolor='yellow', alpha=0.4, edgecolor='black')
    axis.add_collection(coll)
    plt.show()


def spirale(max_n=10):
    nums = list(fibonacci(max_n))
    nums.reverse()  # Reverse die liste weil es einfacher ist von gross zu klein zu machen

    fig, axis = plt.subplots(1) # machen rechteckigen plot mit matplotlib
    last_x, last_y = nums[0]

    axis.set_xlim(0, last_x )
    axis.set_ylim(0, last_y)

    plt.axis('off')

    origin  = [0, 0]

    ecke = 0

    rechtecke = []

    winkel = 90

    for i, (cur_num, prev_num) in enumerate(nums):
        radius = cur_num

        if (i - 1) % 4 == 0:                # Jedes vierte rechteck (ab i = 1) [1,5,9,13,...] ist auf der X - Achse um den ihren wert verschoben
            origin[0] = origin[0] + cur_num
        elif (i - 4) % 6 == 0:              # Jedes sechste rechteck (ab i = 4) [4, 10, 16, 20, ...] ist auf der Y Achse um ihren wert verschoben
            origin[1] = origin[1] + cur_num
        if i % 2 == 1:                      # Jedes zweite rechteck wird anstatt l*b zu b*l
            cur_num, prev_num = prev_num, cur_num



        rechteck = Rectangle(origin, cur_num, prev_num, angle=0.0, antialiased=True)
        rechtecke.append(rechteck)

        axis.annotate(radius, xy=(origin[0] + 0.45 * radius, origin[1] + 0.45 * radius), fontsize=radius)       # richtig scuffed aber grad kein bock zu fixen


        if i == 0:          # KEINE AHNUNG WARUM ABER STACKEXCHANGE SAGT ES
            continue
        if i % 8 == 0:
            ecke += 1
            continue

        # cur_arc = Arc(tuple(origin), 2 * radius, 2 * radius, angle=winkel, theta1=0, theta2=90, edgecolor="black",antialiased=True)


        # Switcher um richtige ecke zu finden
        switcher =  [
                    rechteck.get_xy(),
                    [rechteck.get_x() + rechteck.get_width(), rechteck.get_y()],
                    [rechteck.get_x() + rechteck.get_width(), rechteck.get_y() + rechteck.get_height()],
                    [rechteck.get_x(), rechteck.get_y() + rechteck.get_height()]
                    ]

        centre = switcher[ecke % 4]


        cur_arc = Arc(centre, radius*2, radius * 2, angle=winkel, theta1=0, theta2=90, edgecolor="black",antialiased=True)
        axis.add_patch(cur_arc)


        winkel -= 90
        if winkel == -360:
            winkel = 0
        ecke += 3

    coll = PatchCollection(rechtecke, facecolor='blue', alpha=0.4, edgecolor='black')
    axis.add_collection(coll)
    plt.show()
    plt.savefig("img2.png")


#rechtecke(20)
spirale(10)
