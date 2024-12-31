nuitka \
--standalone \
--follow-imports \
--enable-plugin=pyside6 \
--include-qt-plugins=qml \
--assume-yes-for-downloads \
--output-dir=build \
--linux-icon=src/resources/icons/br.com.justcode.Qt.png \
./src/app/main.py