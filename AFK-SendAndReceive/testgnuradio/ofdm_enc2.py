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

from gnuradio import blocks
import numpy
from gnuradio import digital
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
from PyQt5 import Qt
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
        self.samp_rate = samp_rate = 32000
        self.fft_len = fft_len = 128

        ##################################################
        # Blocks
        ##################################################
        self.digital_ofdm_carrier_allocator_cvc_0 = digital.ofdm_carrier_allocator_cvc( fft_len, ((4,5,6,7,9,10,11,12,14,15),), ((3,8,13),), ((1+0j,1+0j,1+0j),), ((0j+-0.17,0j+0.29,0j+-0.66,0j+-0.62,0j+-0.97,0j+0.62,0j+0.58,0j+0.47,0j+-0.31,0j+0.33,0j+0.27,0j+-0.39,0j+0.19,0j+0.11,0j+-0.55,0j+-0.15,0j+0.42,0j+-0.17,0j+0.26,0j+-0.00,0j+-0.85,0j+0.86,0j+-0.46,0j+0.65,0j+0.26,0j+0.62,0j+0.40,0j+-0.06,0j+0.12,0j+-0.45,0j+0.57,0j+-0.76,0j+-0.88,0j+0.68,0j+-0.47,0j+-0.89,0j+-0.75,0j+-0.86,0j+-0.42,0j+-0.72,0j+-0.48,0j+0.79,0j+0.85,0j+-0.07,0j+0.57,0j+-0.87,0j+0.85,0j+-0.88,0j+0.85,0j+0.42,0j+-0.84,0j+0.82,0j+-0.26,0j+0.63,0j+-0.28,0j+-0.95,0j+0.81,0j+0.44,0j+0.77,0j+-0.60,0j+-0.07,0j+0.11,0j+0.53,0j+-0.84,0j+0.04,0j+-0.87,0j+-0.23,0j+0.38,0j+0.96,0j+0.45,0j+-0.43,0j+0.38,0j+0.21,0j+0.91,0j+-0.08,0j+-0.24,0j+0.85,0j+0.51,0j+0.52,0j+-0.96,0j+0.90,0j+0.04,0j+-0.28,0j+0.18,0j+-0.76,0j+0.38,0j+-0.02,0j+0.60,0j+-0.34,0j+-0.82,0j+0.98,0j+-0.33,0j+-0.55,0j+-0.41,0j+-0.62,0j+0.51,0j+0.04,0j+-0.08,0j+0.65,0j+0.17,0j+0.66,0j+-0.74,0j+-0.62,0j+-0.52,0j+0.81,0j+-0.13,0j+0.67,0j+0.85,0j+-0.77,0j+-0.27,0j+0.73,0j+1.00,0j+-0.81,0j+-0.90,0j+-0.59,0j+0.90,0j+-0.29,0j+0.33,0j+0.34,0j+0.52,0j+-0.61,0j+-0.37,0j+-0.27,0j+-0.35,0j+0.86,0j+0.23,0j+-0.05,0j+0.48),), "packet_len", True)
        self.digital_chunks_to_symbols_xx_0 = digital.chunks_to_symbols_bc((0j+1,1j+0,0j-1,0-1j), 9)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_char*1, 20,True)
        self.blocks_tag_debug_0_0 = blocks.tag_debug(gr.sizeof_gr_complex*fft_len, '', "")
        self.blocks_tag_debug_0_0.set_display(True)
        self.blocks_tag_debug_0 = blocks.tag_debug(gr.sizeof_gr_complex*1, '', "")
        self.blocks_tag_debug_0.set_display(True)
        self.blocks_stream_to_tagged_stream_0 = blocks.stream_to_tagged_stream(gr.sizeof_char, 1, 10, "packet_len")
        self.analog_random_source_x_0 = blocks.vector_source_b(list(map(int, numpy.random.randint(0, 3, 100))), False)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_random_source_x_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_stream_to_tagged_stream_0, 0), (self.digital_chunks_to_symbols_xx_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_stream_to_tagged_stream_0, 0))
        self.connect((self.digital_chunks_to_symbols_xx_0, 0), (self.blocks_tag_debug_0, 0))
        self.connect((self.digital_chunks_to_symbols_xx_0, 0), (self.digital_ofdm_carrier_allocator_cvc_0, 0))
        self.connect((self.digital_ofdm_carrier_allocator_cvc_0, 0), (self.blocks_tag_debug_0_0, 0))


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
