import numpy as np
from scipy import signal
import pywt

def process_data(data):
    data = np.array(data)
    return data

def standardize_classes(classes, time_between_captures_of_samples, window_time ):
    n_of_samples = window_time // time_between_captures_of_samples
    lenght_ = int((len(classes) // n_of_samples) * n_of_samples)
    classes = classes[:lenght_]
    return classes

def sample_classes_(classes, time_between_captures_of_samples, window_time, n_of_chanels):
    n_samples = int(window_time / time_between_captures_of_samples)
    len_ = int(len(classes) / n_samples)
    class_mod_ = np.zeros([len_, n_samples, n_of_chanels])
    for k in range(len_):
        for l in range(n_samples):
            class_mod_[k, l, :] = classes[l + k * n_samples] [:]
    return class_mod_


def filter_signal(class_mod_, sos, n_of_chanels):
    for k, l  in enumerate(class_mod_):
        for m in range(n_of_chanels):
            class_mod_[k, :, m] = signal.sosfilt(sos, class_mod_[k, :, m])
    return class_mod_

def wav_filter(signal, filter_to_use, levels_to_use, layers_to_catch):
    a = 1
    Coeffs = pywt.wavedec(signal, filter_to_use, level=levels_to_use)
    for i in range(1,-1,-(levels_to_use + 1)):
        if -i not in layers_to_catch:
            Coeffs[i] = np.zeros_like(Coeffs[i])
    Rec = pywt.waverec(Coeffs, filter_to_use)
    return Rec

def select_wavelet_layer_x(class_mod_, filter_to_use, levels_to_use,
                           layers_to_catch, n_of_chanels):
    for k, l in enumerate(class_mod_):
        for m in range(n_of_chanels):
            class_mod_[k, :, m] = wav_filter(signal=class_mod_[k, :, m],
                                             filter_to_use=filter_to_use,
                                             levels_to_use=levels_to_use,
                                             layers_to_catch=layers_to_catch
                                             )
    return class_mod_

def m_mav_values_(class_mod_, time_between_captures_of_samples, window_time, n_of_chanels):
    n_of_samples = int(window_time / time_between_captures_of_samples)
    acum_x = 0
    l_class_ = int(len(class_mod_))
    s = [l_class_, n_of_chanels]
    m_class_ = np.zeros(s)
    for k in range(l_class_):
        for l in range(n_of_chanels):
            for m in range(n_of_samples):
                acum_x += abs(class_mod_[k, m, l])/n_of_samples
            m_class_[k, l] = acum_x
            acum_x = 0
    
    return m_class_

def m_rms_values_(class_mod_, time_between_captures_of_samples, window_time, n_of_chanels):
    acum_x = 0
    l_class_ = int(len(class_mod_))
    s = [l_class_, n_of_chanels]
    m_class_ = np.zeros(s)
    for k in range(l_class_):
        for l in range(n_of_chanels_and_category):
            for m in range(n_of_samples):
                acum_x += ((class_mod_[k, m, l])**2) / n_of_samples
            m_class_[k, l] = math.sqrt(acum_x)
            acum_x = 0
    return rms_table_

def matrix_m(type_matrix,class_mod_, time_between_captures_of_samples, window_time, n_of_chanels):
    #from sklearn.preprocessing import StandardScaler
    #scaler = StandardScaler()
    if type_matrix == "rms":
        m_matrix_ = m_rms_values_(class_mod_, time_between_captures_of_samples, window_time, n_of_chanels)
    elif type_matrix == "mav":
        m_matrix_ = m_mav_values_(class_mod_, time_between_captures_of_samples, window_time, n_of_chanels)
    #m_matrix_[:,0:-1] = scaler.fit_transform(m_matrix_[:,0:-1])
    return m_matrix_


def predict_data(data_):
    from joblib import load
    clf = load('/home/caio/my_arm_def/neigh_teste.joblib')
    p = clf.predict(data_)
    return p[0]
