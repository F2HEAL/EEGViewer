# controller.py
"""
Controls real-time EEG signal processing and GUI updates.
"""
from PyQt5.QtWidgets import QApplication, QWidget
from modules.ui import GraphUI
from modules.plot_manager import PlotManager
from modules.filters import GraphFilters
from brainflow.board_shim import BoardShim
import sys


class GraphController:
    def __init__(self, board_shim):
        self.app = QApplication(sys.argv)
        self.board_shim = board_shim
        self.board_id = board_shim.get_board_id()
        self.exg_channels = BoardShim.get_exg_channels(self.board_id)[:8]
        self.virtual_channel_index = len(self.exg_channels)
        self.exg_channels.append(-1)  # Add virtual channel for C3–C4
        self.sampling_rate = 512

        self.filters = GraphFilters(self.sampling_rate, self.exg_channels)
        self.ui = GraphUI(self.filters)
        self.main_widget = QWidget()

        self.virtual_index = 9

        self.plot_manager = PlotManager(
            self.ui, self.board_shim, self.filters,
            self.exg_channels, self.virtual_channel_index,
            self.sampling_rate, self.main_widget
        )

        self.main_widget.show()

    def run(self):
        self.app.exec_()


