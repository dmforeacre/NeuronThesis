import pickle

model_metadata_dict = pickle.load(open("NMDA_TCN__DWT_7_128_153__training.pickle","rb"),encoding='latin1')

with open('training_pickle_readable.dat','w') as f:
    f.write(str(model_metadata_dict))

print("training file translated")

morphology_dict = pickle.load(open("morphology_dict.pickle","rb"), encoding='latin1')

with open('morphology_pickle_readable.dat','w') as f:
    f.write(str(morphology_dict))

print("morphology file translated")
