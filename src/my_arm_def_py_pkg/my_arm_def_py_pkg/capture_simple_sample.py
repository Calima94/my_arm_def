from my_arm_def_py_pkg import mod_sig_emg as mse
import numpy as np
import pandas as pd

def main(new_data):
    #Parameters of the code
    freq_of_capture = 200.0# in hz
    time_between_captures_of_samples = (1/freq_of_capture) * 1000.0
    window_time = 250.0
    n_of_chanels = 8
    # Create a SOS matriz for low_pass_filter with the following characteristics:
    # 10hz bandstop and 15hz bandpass with 60db of attenuation
    # Iir Butterworth filter with 6th order
    sos_low_pass_ = np.array(
            [[
                1, -2, 1, 1, -1.740367670683557577149258577264845371246,
                0.93092862335376458382540931779658421874
            ],
            [
                1, -2, 1, 1, -1.629360431136253506423372527933679521084,
                0.80776668472892854122591188570368103683
            ],
            [
                1, -2, 1, 1, -1.535449319165865356140443509502802044153,
                0.703572808222718393267314240802079439163
            ],
            [
                1, -2, 1, 1, -1.457344522530261921033911676204297691584,
                0.616915954050245685102993320469977334142
            ],
            [
                1, -2, 1, 1, -1.393730553043875275420759862754493951797,
                0.546336595104689237700767989736050367355
            ],
            [
                1, -2, 1, 1, -1.343402365227919670331857560086064040661,
                0.490497739871769145025837133289314806461
            ],
            [
                1, -2, 1, 1, -1.305336827562876278463477319746743887663,
                0.448264229402160208071137503793579526246
            ],
            [
                1, -2, 1, 1, -1.278726258361997381030050746630877256393,
                0.418739945183796424821309756225673481822
            ],
            [
                1, -2, 1, 1, -1.262991469218308848709853009495418518782,
                0.401282280776567523705722351223812438548
            ], [1, -1, 0, 1, -0.628892547371665888711333991523133590817, 0.0]])

    sos_bandstop_ = np.array([
            [
                1, 0.622946104851632931342919619055464863777, 1, 1,
                0.409261284246611789505720935267163440585,
                0.944930685706123152378665963624371215701
            ],
            [
                1, 0.622946104851632931342919619055464863777, 1, 1,
                0.790937366004399455832185594772454351187,
                0.948426893239073809382944091339595615864
            ],
            [
                1, 0.622946104851632931342919619055464863777, 1, 1,
                0.711063241242363974770057666319189593196,
                0.863346362516600351888484965456882491708
            ],
            [
                1, 0.622946104851632931342919619055464863777, 1, 1,
                0.441523156151951257086807345331180840731,
                0.856895681601938186133793351473286747932
            ],
            [
                1, 0.622946104851632931342919619055464863777, 1, 1,
                0.612695780882883012097295249986927956343,
                0.814392565084377184625452628097264096141
            ],
            [
                1, 0.622946104851632931342919619055464863777, 1, 1,
                0.515815447012487493516630365775199607015,
                0.811296756704375288116182218800531700253
            ],
        ])
    # Parameters of the Wavelet filter
    filter_to_use = "db7"
    levels_to_use = 4
    layers_to_catch = [1, 2]
    # Type of filtering
    type_matrix = "mav"
    # Process data
    new_data = mse.process_data(new_data)
    ##standardize the class
    classes = mse.standardize_classes(classes=new_data,
                                      time_between_captures_of_samples=time_between_captures_of_samples,
                                      window_time=window_time)
    
    # Sample the classes
    class_mod_ = mse.sample_classes_(classes=classes,
                                 time_between_captures_of_samples=time_between_captures_of_samples,
                                 window_time=window_time,
                                 n_of_chanels=n_of_chanels
                                 )
    # Filter the signals with high pass filter
    class_mod_ = mse.filter_signal(class_mod_=class_mod_,
                           sos=sos_low_pass_,
                           n_of_chanels=n_of_chanels)
    # Filter the signals with bandstop filter
    class_mod_ = mse.filter_signal(class_mod_=class_mod_,
                           sos=sos_bandstop_,
                           n_of_chanels=n_of_chanels)
    
    # filter the signals with Wavelet filter
    class_mod_ = mse.select_wavelet_layer_x(class_mod_=class_mod_,
                                        filter_to_use=filter_to_use,
                                        levels_to_use=levels_to_use,
                                        layers_to_catch=layers_to_catch,
                                        n_of_chanels=n_of_chanels
                                        )
    # Extract the RMVS or MAV values of the samples
    m_matrix_ = mse.matrix_m(type_matrix=type_matrix,
                         class_mod_=class_mod_,
                         time_between_captures_of_samples=time_between_captures_of_samples,
                         window_time=window_time,
                         n_of_chanels=n_of_chanels
                         )
    # Predict the category of the signal
    p = mse.predict_data(m_matrix_)

    return p, True
