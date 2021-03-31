import os
import sys
import markdown
from PyQt5.QtCore import Qt, QMetaObject, QFile, QIODevice
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QStyleFactory, QWidget, QMainWindow, QMessageBox, \
    QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView
from version import __version__ as VERSION
import resources

if sys.platform == "darwin":
    if getattr(sys, "frozen", False) and getattr(sys, "executable", False):
        executableDir = os.path.join(os.path.dirname(sys.executable))
        webEngineProcessLocation = os.path.join(executableDir, 'lib', 'PyQt5', 'Qt5', 'lib',
                                                'QtWebEngineCore.framework', 'Helpers', 'QtWebEngineProcess.app',
                                                'Contents', 'MacOS', 'QtWebEngineProcess')
        os.environ['QTWEBENGINEPROCESS_PATH'] = webEngineProcessLocation


class AboutWindow(QMainWindow):

    window_title = 'About DERIVA Client Tools %s' % VERSION

    def __init__(self):
        super(AboutWindow, self).__init__()
        self.ui = AboutWindowUI(self)


class AboutWindowUI(object):

    def __init__(self, MainWin):
        # Main Window
        MainWin.setObjectName("AboutWindow")
        MainWin.setWindowIcon(QIcon(":/images/deriva-white.png"))
        MainWin.setWindowTitle(MainWin.tr(MainWin.window_title))
        MainWin.resize(640, 480)
        self.centralWidget = QWidget(MainWin)
        self.centralWidget.setObjectName("centralWidget")
        MainWin.setCentralWidget(self.centralWidget)
        self.verticalLayout = QVBoxLayout(self.centralWidget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.webview = QWebEngineView(MainWin)
        self.verticalLayout.addWidget(self.webview)
        data = get_resource_file_data()
        html = markdown.markdown(data.data().decode("utf-8"))
        self.webview.setHtml(html)
        # finalize UI setup
        QMetaObject.connectSlotsByName(MainWin)


def get_resource_file_data(filename=":/text/about.md"):
    file = QFile(filename)
    if not file.open(QIODevice.Text | QIODevice.ReadOnly):
        data = "Unable to display resource text"
    else:
        data = file.readAll()
        file.close()
    return data


def excepthook(etype, value, tb):
    traceback.print_tb(tb)
    print(format_exception(value), file=sys.stderr)
    msg = QMessageBox()
    msg.setText(str(value))
    msg.setStandardButtons(QMessageBox.Close)
    msg.setWindowTitle("Unhandled Exception: %s" % etype.__name__)
    msg.setIcon(QMessageBox.Critical)
    msg.setDetailedText('\n'.join(traceback.format_exception(etype, value, tb)))
    msg.exec_()


def main():
    sys.excepthook = excepthook
    QApplication.setDesktopSettingsAware(False)
    QApplication.setStyle(QStyleFactory.create("Fusion"))
    app = QApplication(sys.argv)
    app.setAttribute(Qt.AA_UseHighDpiPixmaps)
    about_window = AboutWindow()
    about_window.show()
    ret = app.exec_()
    return ret


if __name__ == '__main__':
    sys.exit(main())
