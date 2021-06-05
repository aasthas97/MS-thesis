import pandas as pd
import random
import matplotlib.pyplot as plt

sim_df = pd.read_csv('.\\turi_imskel.csv', sep=',', names=['query_label', 'reference_label', 'imagedistance', 'imagerank', 'drawingdistance', 'drawingrank'])
norm_df = pd.DataFrame()
for num in range(0, 500):
    object_chosen = sim_df[sim_df['query_label'] == num]
    imagedist = object_chosen['imagedistance']
    drawingdist = object_chosen['drawingdistance']
    image_min = min(imagedist)
    image_max = max(imagedist)
    sketch_min = min(drawingdist)
    sketch_max = max(drawingdist)
    normdist_im = [(dist-image_min)/image_max for dist in imagedist]
    normdist_sketch = [(dist-sketch_min)/sketch_max for dist in drawingdist]
    data = {'query_label': object_chosen['query_label'], 'reference_label': object_chosen['reference_label'],
       'normdist_im': normdist_im, 'normdist_sketch': normdist_sketch}
    norm_df = norm_df.append(pd.DataFrame(data))def newy_mid(n):
    list_1 = random.sample(range(0, n), 5) # sample 5 random numbers from below n
    list_2 = random.sample(range(n+10, 500), 5) # 5 random numbers from above n
    return list_1 + list_2

# diff_im = [] # (Inter-category im dist - intra-category im dist) for all categories
# diff_sk = [] # (Inter-category sketch dist - intra-category sk dist) for all categories
diff_3 = [] # Intra-category im dist - intra-category sk dist) for all categories
diff_4 = [] # Inter-category im dist - inter-category sk dist) for all categoriesfor n in range(0, 500, 10):
    plt.clf()
    object_number = n + random.randint(0,9)
    y = [n + foo for foo in range(0, 10)] # ref labels for same-category object

    if n >= 10 and n < 490:
        new_y = newy_mid(n)
    elif n < 10: # sample all numbers greater than n
        new_y = random.sample(range(10, 350), 10)
    elif n >= 490: # all numbers less than n
        new_y = random.sample(range(0, 340), 10)
    
    value1 = norm_df[norm_df['reference_label'].isin(y)].loc[norm_df['query_label'] == object_number, 'normdist_im'] # intra-category image distance
    value2 = norm_df[norm_df['reference_label'].isin(y)].loc[norm_df['query_label'] == object_number, 'normdist_sketch'] #intra-category sketch distance
    value3 = norm_df[norm_df['reference_label'].isin(new_y)].loc[norm_df['query_label'] == object_number, 'normdist_im'] #inter-category image distance
    value4 = norm_df[norm_df['reference_label'].isin(new_y)].loc[norm_df['query_label'] == object_number, 'normdist_sketch'] #inter-category sketch distance

#     print('Intra-category image distance', value1.mean())
#     print('Intra-category skeleton distance', value2.mean())
#     print('Inter-category image distance', value3.mean())
#     print('Inter-category skeleton distance', value4.mean())
#     print('\n\n')
    # plot distances
    
    fig, (ax1, ax2) = plt.subplots(2, figsize=(15,15))
    ax1.hlines(y=y, xmin=value1, xmax=value3, color='grey', alpha=0.4)
    ax1.scatter(value1, y, color='skyblue', alpha=0.8, label='intra-category image distance')
    ax1.scatter(value3, y, color='darkslategrey', alpha=0.6 , label='Inter-category image distance')
    ax2.hlines(y=y, xmin=value2, xmax=value4, color='grey', alpha=0.4)
    ax2.scatter(value2, y, color='pink', alpha=1 , label='Intra-category skeleton distance')
    ax2.scatter(value4, y, color='darkorange', alpha=0.6, label='Inter-category skeleton distance') 
    ax1.legend()
    ax2.legend()
    ax1.set_xlim(0, 1)
    ax2.set_xlim(0, 1)
    ax1.set_yticks([])
    ax2.set_yticks([])
    plt.xlabel('Distance')
    plt.ylabel('Object number')
    im_name = str(n) + '_imvsskel.png'
    plt.savefig(im_name)
    
    # means

#     diff_intra = value1.mean() - value2.mean()
#     diff_inter = value3.mean() - value4.mean()
#     diff_im.append(mean_im)
#     diff_sk.append(mean_sk)
#     diff_3.append(diff_intra)
#     diff_4.append(diff_inter)
#     print('Inter-category im dist - intra-category im dist =', mean_im)
#     print('Inter-category sketch dist - intra-category sketch dist =', mean_sk)
