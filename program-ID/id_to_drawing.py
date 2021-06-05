def sample_random_pts(): #sample random x, y points
    pts = []
    for n in range(5):
        pts.append(random.sample(range(1, 10), 2))

    return pts

def select_point(list_of_pts):
    return random.choice(list_of_pts)

def make_move(start_pt, angle, relation): # draw a 5 unit long line from start_pt
    x, y = start_pt
    length = 5

    # find the end point
    endy = length * math.sin(math.radians(angle))
    endx = length * math.cos(math.radians(angle))

    # plot the points
    plt.plot([x, endx], [y, endy], c = 'b')

def get_angle(*args): # choose angle corresponding to max probability
    if args:
        for dict_probabilities in args:
            # take the first list from angles and calculate corresponding probabilities
            best_angle = max(dict_probabilities, key=dict_probabilities.get)
            return best_angle

    else:
        return 45

def select_relation():
    return random.choice(['start', 'end', 'mid', 'ind'])

def prob_for_angle(list_angles):
    dict_probabilities = dict()
    lambda_constt = 0.5
    for angle in list_angles:
        prob = math.exp(-(lambda_constt * angle))
        dict_probabilities[angle] = prob

    return dict_probabilities

  
# DRIVER
df = pd.read_excel('skeletonID.xlsx')
allitems = list(df.columns.values) # get names of all items
# del(allitems[0])

for item in allitems:
    plt.figure(frameon = False)
    fig = plt.figure()
    ax = plt.Axes(fig, [0.,0.,1.,1.])
    ax.set_axis_off()
    fig.add_axes(ax)
    
    ids = [id for id in pd.Series.tolist(df.loc[:, item]) if id == id]
    pattern = re.compile('\[\d+\.?\d*e?-?\+?\d*\]')
    pattern2 = re.compile('(\[\d+\.?\d+)(\])(e+?-?\d\d)')
    chosen_id = random.choice(ids)
    chosen_id = pattern2.sub(r'\1\3\2', chosen_id)
    transtab = str.maketrans({'[': None, ']': None})
    # extract angles from strings
    angles = [float(angle.translate(transtab)) for angle in re.findall(pattern, chosen_id)]
    for idx in range(0, len(angles)): # add random angles sampled from a uniform distribution
        angles[idx] = [angles[idx], float(np.random.uniform(0.0, 360, 1)), float(np.random.uniform(0.0, 360, 1))]

    chosen_id = pattern.sub('', chosen_id)
    dict_probabilities = dict()

    for foo in chosen_id:
        if foo == '1':
            random_pts = sample_random_pts()
        elif foo == '2':
            try:
                start_pt = select_point(random_pts)
            except:
                start_pt = [1, 1]

        elif foo == '3':
            try:
                make_move(start_pt, angle, relation)

            except: # angle or relation not defined yet
                make_move(start_pt, 45, 'ind')

        elif foo == '4':
            relation = select_relation()

        elif foo == '5':
            if dict_probabilities:
                angle = get_angle(dict_probabilities)
            else:
                angle = get_angle()

        elif foo == '6':
            try:
                list_angles = angles.pop(0)
                dict_probabilities = prob_for_angle(list_angles)
            except:
                pass

        else:
            print('something\'s wrong')

    # plt.show()
    im_name = item + 'sketch.png'
    plt.savefig(im_name)
    plt.close()
