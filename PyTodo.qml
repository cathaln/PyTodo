import QtQuick 2.12
import QtQuick.Controls 2.5
import QtQuick.Controls.Material 2.12

ApplicationWindow {

    id: window

    minimumWidth: 800
    minimumHeight: 550
    visible: true

    Material.primary: "#607D8B"
    Material.background: "#B0BEC5"
    Material.accent: "#ffffff"

    header: ToolBar {
        contentHeight: toolButton.implicitHeight

        ToolButton {
            id: toolButton
            Text {
                id: name
                text: stackView.depth > 1 ? "\u25C0" : "\u2630"
                font.pixelSize: Qt.application.font.pixelSize * 1.6
                color: '#ffffff'
                anchors.centerIn: parent
            }

            onClicked: {
                if (stackView.depth > 1) {
                    stackView.pop()
                } else {
                    drawer.open()
                }
            }
        }

        Label {
            text: stackView.currentItem.title
            anchors.centerIn: parent
        }
    }

    Drawer {
        id: drawer
        width: window.width * 0.66
        height: window.height

        Column {
            anchors.fill: parent
            width: parent.width

            ItemDelegate {

                width: parent.width
                Text {
                    text: qsTr("About")
                    width: parent.width
                    color: '#ffffff'
                    font.pointSize: 14
                    anchors.verticalCenter: parent.verticalCenter
                    leftPadding: 20
                }

                onClicked: {
                    stackView.push(aboutPage)
                    drawer.close()
                }
            }
        }
    }

    StackView {
        id: stackView
        anchors.fill: parent
        initialItem: TodoBoard {}
    }
}
