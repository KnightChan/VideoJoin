# -*- coding: utf-8 -*-

__author__ = 'Qingjun'

from video_join_ui import Ui_videoJoinForm
from PyQt4 import QtGui
import os

import flv_join
import mp4_join


class VideoJoinMainUI(QtGui.QWidget, Ui_videoJoinForm):

    def __init__(self):
        super(VideoJoinMainUI, self).__init__()
        self.setupUi(self)
        self.addVideoButton.clicked.connect(self.addVideoButtonClicked)
        self.delVideoButton.clicked.connect(self.delVideoButtonClicked)
        self.selectedVideoUpButton.clicked.connect(self.selectedVideoUpButtonClicked)
        self.selectedVideoDownButton.clicked.connect(self.selectedVideoDownButtonClicked)
        self.startVideoJoinButton.clicked.connect(self.startVideoJoinButtonClicked)
        self.outputPathSelectButton.clicked.connect(self.outputPathSelectButtonClicked)
        formatstr = self.formatSelectComboBox.currentText()
        if formatstr == '*.flv':
            self.outputPathLineEdit.setText(os.curdir + "\\output.flv")
            self.outputPathLineEdit.setToolTip(os.curdir + "\\output.flv")
        elif formatstr == '*.mp4':
            self.outputPathLineEdit.setToolTip(os.curdir + "\\output.mp4")
            self.outputPathLineEdit.setText(os.curdir + "\\output.mp4")
        self.formatSelectComboBox.setEnabled(False)

    def startVideoJoinButtonClicked(self):
        self.addMsg("开始拼接")
        videos = []
        for i in range(0, self.videoListWidget.count()):
            videos.append(u8str(self.videoListWidget.item(i).toolTip().toUtf8()))

        formatstr = self.formatSelectComboBox.currentText()
        output = ""
        if formatstr == '*.flv':
            self.addMsg("\tflv拼接")
            for video in videos:
                self.addMsg("\t\t" + os.path.basename(video))
            output = flv_join.concat_flvs(self, videos, u8str(self.outputPathLineEdit.toolTip().toUtf8()))
        elif formatstr == '*.mp4':
            self.addMsg("\tmp4拼接")
            for video in videos:
                self.addMsg("\t\t" + os.path.basename(video))
            output = mp4_join.concat_mp4s(self, videos, u8str(self.outputPathLineEdit.toolTip().toUtf8()))
        else:
            self.addMsg("\tnot flv or mp4")
        self.addMsg("\t" + output + u" 拼接完成")
        self.addMsg("")

    def outputPathSelectButtonClicked(self):
        self.addMsg("selected output path:")
        formatstr = self.formatSelectComboBox.currentText()
        outputPath = QtGui.QFileDialog.getSaveFileName(None, u"保存文件", "", formatstr)
        self.outputPathLineEdit.setText(outputPath)
        self.outputPathLineEdit.setToolTip(outputPath)
        self.addMsg("\t" + outputPath.toUtf8())
        self.addMsg("")

    def selectedVideoDownButtonClicked(self):
        self.addMsg("move selected videos down:")
        selectedIndexes = self.getVideoListSelectedIndexes()
        if len(selectedIndexes) == 0:
            return
        selectedIndexes.sort(reverse=True)
        prenotin = self.videoListWidget.count() - 1
        minindex = selectedIndexes[len(selectedIndexes) - 1]
        while prenotin in selectedIndexes:
                prenotin -= 1
        nowin = prenotin
        while prenotin > minindex:
            while nowin not in selectedIndexes and nowin >= minindex:
                prenotin = nowin
                nowin -= 1
            if nowin < minindex:
                break
            item = self.videoListWidget.takeItem(nowin)
            self.videoListWidget.insertItem(prenotin, item)
            self.videoListWidget.setCurrentRow(prenotin)
            prenotin -= 1
            nowin = prenotin - 1
        self.addMsg("")

    def selectedVideoUpButtonClicked(self):
        self.addMsg("move selected videos up:")
        selectedIndexes = self.getVideoListSelectedIndexes()
        if len(selectedIndexes) == 0:
            return
        selectedIndexes.sort()
        prenotin = 0
        maxindex = selectedIndexes[len(selectedIndexes) - 1]
        while prenotin in selectedIndexes:
                prenotin += 1
        nowin = prenotin
        while prenotin < maxindex:
            while nowin not in selectedIndexes and nowin <= maxindex:
                prenotin = nowin
                nowin += 1
            if nowin > maxindex:
                break
            item = self.videoListWidget.takeItem(nowin)
            self.videoListWidget.insertItem(prenotin, item)
            self.videoListWidget.setCurrentRow(prenotin)
            prenotin += 1
            nowin = prenotin + 1
        self.addMsg("")

    def delVideoButtonClicked(self):
        self.addMsg("delete selected videos:")
        selectedItems = self.videoListWidget.selectedItems()
        if len(selectedItems) == 0:
            return
        for selectedItem in selectedItems:
            self.addMsg("\t" + selectedItem.text().toUtf8() + " deleted!")
            self.videoListWidget.takeItem(self.videoListWidget.row(selectedItem))
        self.addMsg("")

    def addVideoButtonClicked(self):
        self.addMsg("add videos:")
        formatstr = self.formatSelectComboBox.currentText()
        paths = QtGui.QFileDialog.getOpenFileNames(None, u"选择需要合并的视频文件", "", formatstr)
        for i in range(0, len(paths)):
            name = os.path.basename(paths[i].toUtf8())
            name = u8str(name)
            self.addMsg("\t" + name + " added!")
            self.addVideo(name, u8str(paths[i].toUtf8()))
        self.addMsg("")

    def addVideos(self, names, paths):
        for i in range(0, len(names)):
            self.addVideo(names[i], paths[i])

    def addVideo(self, name, path):
        newItem = QtGui.QListWidgetItem(name)
        newItem.setToolTip(path)
        self.videoListWidget.addItem(newItem)

    def addMsg(self, msg):
        self.msgTextBrowser.append(u8str(msg))

    def getVideoListSelectedIndexes(self):
        selectedIndexes = []
        selectedItems = self.videoListWidget.selectedItems()
        for selectedItem in selectedItems:
            selectedIndexes.append(self.videoListWidget.row(selectedItem))
        return selectedIndexes


def u8str(s):
    try:
        s = unicode(s, 'utf-8', 'ignore')
    except:
        pass
    return s


