# -*- coding: utf-8 -*-
"""."""

import sys

import resources_rc
from PySide6 import QtCore, QtGui, QtQml
from ui.MainWindow import MainWindow

RESOURCES_RC = resources_rc

APPLICATION_NAME = 'br.com.justcode.Qt'
ORGANIZATION_NAME = APPLICATION_NAME.split('.')[2]
ORGANIZATION_DOMAIN = '.'.join(APPLICATION_NAME.split('.')[0:3])


def main() -> None:
    application = QtGui.QGuiApplication(sys.argv)
    application.setApplicationDisplayName(APPLICATION_NAME)
    application.setApplicationName(APPLICATION_NAME)
    application.setDesktopFileName(APPLICATION_NAME)
    application.setOrganizationName(ORGANIZATION_NAME)
    application.setOrganizationDomain(ORGANIZATION_DOMAIN)

    loc = QtCore.QLocale.system()
    translator = QtCore.QTranslator(application)
    if translator.load(
        QtCore.QLocale(loc), APPLICATION_NAME, '.', ':/locales'
    ):
        application.installTranslator(translator)

    if QtCore.QSysInfo.productType() == 'windows':
        from ctypes import windll

        windll.shell32.SetCurrentProcessExplicitAppUserModelID(
            APPLICATION_NAME,
        )

    mainWindow = MainWindow()

    engine = QtQml.QQmlApplicationEngine()
    engine.rootContext().setContextProperty('mainWindow', mainWindow)
    engine.load(QtCore.QUrl('qrc:/ui/MainWindow.qml'))

    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(application.exec())


if __name__ == '__main__':
    main()
