import splitfolders

input_folder = 'imgs/'


'''
splitfolders.ratio(input_folder, output="imgs1", seed=42,
                      ratio=(.7,.2,.1),group_prefix=None)
'''

splitfolders.fixed(input_folder, output="imgs3", seed=42, fixed=(50,30),
                   oversample = True, group_prefix=None)
