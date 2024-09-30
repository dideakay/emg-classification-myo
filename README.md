# emg-classification-myo

This repository is aimed to acquire raw emg signals and then classify them using RMS and Variace features with KNN and SVM classification methods.

## Signal acquisition

- Code: [signal-acquisition](signal-acquisition.py)



- Note: You should wait 2 minutes for the armband to warm up 

## Processing and Plotting
 - Raw data: [raw_plots](raw_plots.ipynb)

![image](https://github.com/dideakay/emg-classification-myo/assets/59506252/6eb36fde-5a31-48a1-995a-e53118e62fbe)


 
 - RMS: [rms_plot.ipynb](rms_plot.ipynb)

![image](https://github.com/dideakay/emg-classification-myo/assets/59506252/0287e52e-ae67-4b00-b562-a3ae669af096)

- Detecting starting points: [merge_rms_data](knn_classification_all_participants.ipynb)

![image](https://github.com/dideakay/emg-classification-myo/assets/59506252/88d1dcff-d525-4760-9e9e-7aff40a56085)


## Classification
- KNN : [knn_classification](svm_classification.ipynb)
- SVM : [svm_classification](svm_classification_person1.ipynb)

## Results
- The results achieved a mean accuracy rate of 93%.

## Next Steps
- The next step is to use these models in a serious game designed for rehabilitation. 

