import ais_processor as ais

class signal_decoder:
    def __init__(self, center_freq, sample_rate, iq_samples):
        #for i in range(4):
        self.decoders = ais.run(center_freq, sample_rate, iq_samples(1))  # create four decoders, one for each KerberosSDR.

#    def decode_signal(self, iq_samples):
#            self.decoders(i).decode(iq_samples(i))
