import QtQuick
import QtQuick.Layouts
import QtQuick.Controls as Controls
import org.kde.kirigami as Kirigami

Kirigami.ApplicationWindow {
    id: root

    height: 720
    minimumHeight: 640
    minimumWidth: 360
    title: 'PySide'
    visible: true
    width: 1280

    pageStack.initialPage: Kirigami.Page {
        title: "Python Kirigami"

        ColumnLayout {
            anchors.fill: parent

            Controls.Label {
                id: label

                Layout.fillHeight: true
                Layout.fillWidth: true
                horizontalAlignment: Qt.AlignHCenter
                text: qsTr("Type something in the text field!")
                verticalAlignment: Qt.AlignVCenter
            }

            Controls.TextField {
                id: textField

                Layout.fillWidth: true
                placeholderText: qsTr("Type something.")
            }

            Controls.Button {
                id: button

                Layout.fillWidth: true
                text: qsTr("Click here")

                onClicked: {
                    let text = textField.text;
                    if (text.len === 0 || text.trim() === "") {
                        showPassiveNotification(qsTr("textField is empty."));
                    } else {
                        let pythonText = mainWindow.to_upper(text);
                        text += pythonText;
                        label.text = text;
                    }
                }
            }
        }
    }
}
