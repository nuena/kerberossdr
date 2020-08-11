from gnuradio import gr, analog, filter, blocks
from gnuradio.filter import firdes
import pmt


class ais_processor:

    def __init__(self, samp_rate, center_freq, data_in):
        ##################################################
        # Variables
        ##################################################
        if center_freq != 162e6:
            return

        self.samp_rate = samp_rate
        self.xlate_filter_taps = xlate_filter_taps = firdes.low_pass(1, samp_rate, 15000, 20000, firdes.WIN_HAMMING, 6.76)
        self.ch2_offset = ch2_offset = 25e3
        self.ch1_offset = ch1_offset = -25e3

        ##################################################
        # Blocks
        ##################################################
        self.rational_resampler_xxx_1_0 = filter.rational_resampler_fff(
                interpolation=48,
                decimation=50,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_1 = filter.rational_resampler_fff(
                interpolation=48,
                decimation=50,
                taps=None,
                fractional_bw=None,
        )
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.freq_xlating_fir_filter_xxx_0_0 = filter.freq_xlating_fir_filter_ccc(20, (xlate_filter_taps), ch2_offset, samp_rate)
        self.freq_xlating_fir_filter_xxx_0 = filter.freq_xlating_fir_filter_ccc(20, (xlate_filter_taps), ch1_offset, samp_rate)
        self.blocks_interleave_0 = blocks.interleave(gr.sizeof_short*1, 1)
        self.blocks_float_to_short_0_0 = blocks.float_to_short(1, 16000)
        self.blocks_float_to_short_0 = blocks.float_to_short(1, 16000)

        self.blocks_vector_source_x_0 = blocks.vector_source_c(data_in, False, 1, [])
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_short*1, 'aisfifo', True)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.analog_quadrature_demod_cf_0_0 = analog.quadrature_demod_cf(0.3)
        self.analog_quadrature_demod_cf_0 = analog.quadrature_demod_cf(0.3)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_quadrature_demod_cf_0, 0), (self.rational_resampler_xxx_1, 0))
        self.connect((self.analog_quadrature_demod_cf_0_0, 0), (self.rational_resampler_xxx_1_0, 0))
        self.connect((self.blocks_vector_source_x_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.freq_xlating_fir_filter_xxx_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.freq_xlating_fir_filter_xxx_0_0, 0))
        self.connect((self.blocks_float_to_short_0, 0), (self.blocks_interleave_0, 1))
        self.connect((self.blocks_float_to_short_0_0, 0), (self.blocks_interleave_0, 0))
        self.connect((self.blocks_interleave_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.analog_quadrature_demod_cf_0, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0_0, 0), (self.analog_quadrature_demod_cf_0_0, 0))
        self.connect((self.rational_resampler_xxx_1, 0), (self.blocks_float_to_short_0, 0))
        self.connect((self.rational_resampler_xxx_1_0, 0), (self.blocks_float_to_short_0_0, 0))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_xlate_filter_taps(firdes.low_pass(1, self.samp_rate, 15000, 20000, firdes.WIN_HAMMING, 6.76))

    def get_xlate_filter_taps(self):
        return self.xlate_filter_taps

    def set_xlate_filter_taps(self, xlate_filter_taps):
        self.xlate_filter_taps = xlate_filter_taps
        self.freq_xlating_fir_filter_xxx_0_0.set_taps((self.xlate_filter_taps))
        self.freq_xlating_fir_filter_xxx_0.set_taps((self.xlate_filter_taps))

    def get_ch2_offset(self):
        return self.ch2_offset

    def set_ch2_offset(self, ch2_offset):
        self.ch2_offset = ch2_offset
        self.freq_xlating_fir_filter_xxx_0_0.set_center_freq(self.ch2_offset)

    def get_ch1_offset(self):
        return self.ch1_offset

    def set_ch1_offset(self, ch1_offset):
        self.ch1_offset = ch1_offset
        self.freq_xlating_fir_filter_xxx_0.set_center_freq(self.ch1_offset)


def run(samp_rate, center_freq, data_in):

    tb = ais_processor(samp_rate, center_freq, data_in)
    tb.Start(True)
    #tb.Wait()


#if __name__ == '__main__':
#    main()
