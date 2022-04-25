#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# Author: adahlhoff
# GNU Radio version: 3.10.2.0

from packaging.version import Version as StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import blocks
import numpy
from gnuradio import digital
from gnuradio import fft
from gnuradio.fft import window
from gnuradio import filter
from gnuradio import gr
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation



from gnuradio import qtgui

class ofdm_enc2(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Not titled yet", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Not titled yet")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "ofdm_enc2")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 24000
        self.fft_len = fft_len = 128

        ##################################################
        # Blocks
        ##################################################
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
            2048, #size
            24000, #samp_rate
            "", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('Y', "")

        self.qtgui_time_sink_x_0.enable_tags(True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0.enable_grid(True)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.mmse_resampler_xx_0 = filter.mmse_resampler_ff(0.0, samp_rate/48000)
        self.fft_vxx_0 = fft.fft_vcc(fft_len, False, (), False, 1)
        self.digital_ofdm_cyclic_prefixer_0 = digital.ofdm_cyclic_prefixer(
            fft_len,
            fft_len + fft_len//4,
            4,
            '')
        self.digital_ofdm_carrier_allocator_cvc_0 = digital.ofdm_carrier_allocator_cvc( fft_len, [(4,5,6,7,9,10,11,12,14,15),(16,5,6,7,9,10,11,12,14,15)], [(3,8,13),(3,8,13)], [(1+0j,1+0j,1+0j),(1+0j,1+0j,1+0.2j)], ((0j+0.00,0j+0.00,0j+0.00,0j+0.12,0j+0.89,0j+-1.00,0j+0.24,0j+-0.64,0j+0.84,0j+-0.96,0j+-0.27,0j+-0.16,0j+-0.28,0j+-0.08,0j+0.27,0j+-0.50,0j+0.95,0j+0.82,0j+0.82,0j+0.53,0j+0.57,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00,0j+0.00),), "packet_len", False)
        self.digital_chunks_to_symbols_xx_0 = digital.chunks_to_symbols_bc((0j+1,1j+0,0j-1,0-1j), 1)
        self.blocks_wavfile_sink_0 = blocks.wavfile_sink(
            '/tmp/muell.wav',
            1,
            48000,
            blocks.FORMAT_WAV,
            blocks.FORMAT_PCM_16,
            False
            )
        self.blocks_throttle_0_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_stream_to_tagged_stream_0 = blocks.stream_to_tagged_stream(gr.sizeof_char, 1, 20, "packet_len")
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_float*1)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_ff(0.075)
        self.blocks_complex_to_float_0 = blocks.complex_to_float(1)
        self.analog_random_source_x_0 = blocks.vector_source_b(list(map(int, numpy.random.randint(0, 3, 2500))), False)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_random_source_x_0, 0), (self.blocks_stream_to_tagged_stream_0, 0))
        self.connect((self.blocks_complex_to_float_0, 0), (self.blocks_throttle_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_wavfile_sink_0, 0))
        self.connect((self.blocks_stream_to_tagged_stream_0, 0), (self.digital_chunks_to_symbols_xx_0, 0))
        self.connect((self.blocks_throttle_0_0, 0), (self.blocks_null_sink_0, 0))
        self.connect((self.blocks_throttle_0_0, 0), (self.mmse_resampler_xx_0, 0))
        self.connect((self.blocks_throttle_0_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.digital_chunks_to_symbols_xx_0, 0), (self.digital_ofdm_carrier_allocator_cvc_0, 0))
        self.connect((self.digital_ofdm_carrier_allocator_cvc_0, 0), (self.fft_vxx_0, 0))
        self.connect((self.digital_ofdm_cyclic_prefixer_0, 0), (self.blocks_complex_to_float_0, 0))
        self.connect((self.fft_vxx_0, 0), (self.digital_ofdm_cyclic_prefixer_0, 0))
        self.connect((self.mmse_resampler_xx_0, 0), (self.blocks_multiply_const_vxx_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "ofdm_enc2")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0_0.set_sample_rate(self.samp_rate)
        self.mmse_resampler_xx_0.set_resamp_ratio(self.samp_rate/48000)

    def get_fft_len(self):
        return self.fft_len

    def set_fft_len(self, fft_len):
        self.fft_len = fft_len




def main(top_block_cls=ofdm_enc2, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
