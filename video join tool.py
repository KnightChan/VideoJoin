__author__ = 'Qingjun'

import video_join_mainui
from PyQt4 import QtGui

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    window = video_join_mainui.VideoJoinMainUI()
    window.show()
    app.exit(app.exec_())