import os

# change this!
subreddit = 'dankmemes'
working_dir = f'reddit_data/{subreddit}/'
media_dir = os.path.join(working_dir, 'media')
mosaic_dir = os.path.join(working_dir, 'mosaics')
output_dir = 'ouput/'
image_lookup_file = os.path.join(working_dir, 'media.json.gz')

# these files don't exist yet
logits_file = os.path.join(working_dir, 'image_features.csv.gz')
knn_file = os.path.join(working_dir, 'knn.pkl')
file_animation = os.path.join(output_dir,'/doppler_mosaic.mp4')

for _dir in [working_dir, media_dir, output_dir, mosaic_dir]:
    os.makedirs(_dir, exist_ok=True)
    
# shared variables
skip_hash = ['NOHASH', '0000000000000000', 'nan']
n_dimensions = 2048 # features from resnet50
cols_conv_feats = [f'conv_{n}' for n in range(n_dimensions)]
