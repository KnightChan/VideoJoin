# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\WorkSpaces\python-svn\Python\VideoJoin\video_join_ui.ui'
#
# Created: Fri Aug 22 14:28:38 2014
#      by: PyQt4 UI code generator 4.11.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_videoJoinForm(object):
    def setupUi(self, videoJoinForm):
        videoJoinForm.setObjectName(_fromUtf8("videoJoinForm"))
        videoJoinForm.resize(748, 548)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(videoJoinForm.sizePolicy().hasHeightForWidth())
        videoJoinForm.setSizePolicy(sizePolicy)
        videoJoinForm.setMinimumSize(QtCore.QSize(748, 548))
        videoJoinForm.setMaximumSize(QtCore.QSize(748, 548))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("video icon.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        videoJoinForm.setWindowIcon(icon)
        self.addVideoButton = QtGui.QPushButton(videoJoinForm)
        self.addVideoButton.setGeometry(QtCore.QRect(180, 30, 91, 41))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addVideoButton.sizePolicy().hasHeightForWidth())
        self.addVideoButton.setSizePolicy(sizePolicy)
        self.addVideoButton.setObjectName(_fromUtf8("addVideoButton"))
        self.formatSelectLabel = QtGui.QLabel(videoJoinForm)
        self.formatSelectLabel.setGeometry(QtCore.QRect(40, 30, 51, 41))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.formatSelectLabel.setFont(font)
        self.formatSelectLabel.setAutoFillBackground(False)
        self.formatSelectLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.formatSelectLabel.setObjectName(_fromUtf8("formatSelectLabel"))
        self.formatSelectComboBox = QtGui.QComboBox(videoJoinForm)
        self.formatSelectComboBox.setGeometry(QtCore.QRect(100, 30, 61, 41))
        self.formatSelectComboBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.formatSelectComboBox.setObjectName(_fromUtf8("formatSelectComboBox"))
        self.formatSelectComboBox.addItem(_fromUtf8(""))
        self.formatSelectComboBox.addItem(_fromUtf8(""))
        self.videoListWidget = QtGui.QListWidget(videoJoinForm)
        self.videoListWidget.setGeometry(QtCore.QRect(30, 80, 281, 381))
        self.videoListWidget.setDragEnabled(True)
        self.videoListWidget.setDragDropMode(QtGui.QAbstractItemView.InternalMove)
        self.videoListWidget.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.videoListWidget.setObjectName(_fromUtf8("videoListWidget"))
        self.selectedVideoUpButton = QtGui.QPushButton(videoJoinForm)
        self.selectedVideoUpButton.setGeometry(QtCore.QRect(330, 110, 41, 121))
        self.selectedVideoUpButton.setObjectName(_fromUtf8("selectedVideoUpButton"))
        self.selectedVideoDownButton = QtGui.QPushButton(videoJoinForm)
        self.selectedVideoDownButton.setGeometry(QtCore.QRect(330, 310, 41, 121))
        self.selectedVideoDownButton.setObjectName(_fromUtf8("selectedVideoDownButton"))
        self.startVideoJoinButton = QtGui.QPushButton(videoJoinForm)
        self.startVideoJoinButton.setGeometry(QtCore.QRect(490, 420, 151, 81))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startVideoJoinButton.sizePolicy().hasHeightForWidth())
        self.startVideoJoinButton.setSizePolicy(sizePolicy)
        self.startVideoJoinButton.setObjectName(_fromUtf8("startVideoJoinButton"))
        self.msgTextBrowser = QtGui.QTextBrowser(videoJoinForm)
        self.msgTextBrowser.setGeometry(QtCore.QRect(410, 80, 311, 301))
        self.msgTextBrowser.setLineWrapMode(QtGui.QTextEdit.NoWrap)
        self.msgTextBrowser.setReadOnly(True)
        self.msgTextBrowser.setObjectName(_fromUtf8("msgTextBrowser"))
        self.msgLabel = QtGui.QLabel(videoJoinForm)
        self.msgLabel.setGeometry(QtCore.QRect(420, 40, 81, 31))
        self.msgLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.msgLabel.setObjectName(_fromUtf8("msgLabel"))
        self.delVideoButton = QtGui.QPushButton(videoJoinForm)
        self.delVideoButton.setGeometry(QtCore.QRect(330, 250, 41, 41))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delVideoButton.sizePolicy().hasHeightForWidth())
        self.delVideoButton.setSizePolicy(sizePolicy)
        self.delVideoButton.setObjectName(_fromUtf8("delVideoButton"))
        self.outputPathLabel = QtGui.QLabel(videoJoinForm)
        self.outputPathLabel.setGeometry(QtCore.QRect(30, 470, 51, 51))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.outputPathLabel.setFont(font)
        self.outputPathLabel.setAutoFillBackground(False)
        self.outputPathLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.outputPathLabel.setObjectName(_fromUtf8("outputPathLabel"))
        self.outputPathLineEdit = QtGui.QLineEdit(videoJoinForm)
        self.outputPathLineEdit.setGeometry(QtCore.QRect(80, 480, 231, 31))
        self.outputPathLineEdit.setReadOnly(True)
        self.outputPathLineEdit.setObjectName(_fromUtf8("outputPathLineEdit"))
        self.outputPathSelectButton = QtGui.QPushButton(videoJoinForm)
        self.outputPathSelectButton.setGeometry(QtCore.QRect(320, 480, 41, 31))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.outputPathSelectButton.sizePolicy().hasHeightForWidth())
        self.outputPathSelectButton.setSizePolicy(sizePolicy)
        self.outputPathSelectButton.setObjectName(_fromUtf8("outputPathSelectButton"))

        self.retranslateUi(videoJoinForm)
        QtCore.QMetaObject.connectSlotsByName(videoJoinForm)

    def retranslateUi(self, videoJoinForm):
        videoJoinForm.setWindowTitle(_translate("videoJoinForm", "视频合并工具", None))
        self.addVideoButton.setText(_translate("videoJoinForm", "添加视频", None))
        self.formatSelectLabel.setText(_translate("videoJoinForm", "视频格式", None))
        self.formatSelectComboBox.setItemText(0, _translate("videoJoinForm", "*.flv", None))
        self.formatSelectComboBox.setItemText(1, _translate("videoJoinForm", "*.mp4", None))
        self.selectedVideoUpButton.setText(_translate("videoJoinForm", "↑", None))
        self.selectedVideoDownButton.setText(_translate("videoJoinForm", "↓", None))
        self.startVideoJoinButton.setText(_translate("videoJoinForm", "开始", None))
        self.msgLabel.setText(_translate("videoJoinForm", "消息窗", None))
        self.delVideoButton.setText(_translate("videoJoinForm", "删除", None))
        self.outputPathLabel.setText(_translate("videoJoinForm", "输出路径", None))
        self.outputPathSelectButton.setText(_translate("videoJoinForm", "...", None))

